#include <linux/fs.h>
#include <linux/cdev.h>
#include <linux/pci.h>
#include <asm/uaccess.h>
#include <mach/map.h>
#include <mach/regs-gpio.h>
#include <mach/gpio-bank-m.h>

#define DEVICE_NAME "s3c6410_leds"
#define DEVICE_COUNT 1
#define LEDS_MAJOR 0
#define LEDS_MINOR 234
#define PARAM_SIZE 3


static int major = LEDS_MAJOR;
static int minor = LEDS_MINOR;

static unsigned char mem[4];			//保存4个LED的设置状态
static char *params[] = {"string1", "string2", "string3"};  //数组类型的模块参数的默认值
static int param_size = PARAM_SIZE;	//数组类型的模块参数值的个数
static int leds_state = 1;			//当前LED的状态，通过模块参数传入

static dev_t dev_number;
static struct class *leds_class = NULL;	//LED字符设备结构体


/**
*处理LED驱动的命令，cmd表示开关LED，1表示打开LED
*arg表示LED的需要，从0到3
**/
static long leds_ioctl(struct file *filp, unsigned int cmd, unsigned long arg)
{
	switch(cmd)
	{
		unsigned tmp;
		case 0:
		case 1:
			if(arg > 4)
			{
				return -EINVAL;
			}

			//读取GPMDAT寄存器当前的值
			tmp = ioread32(S3C64XX_GPMDAT);
			
			if(1 == cmd)	//打开arg指定的LED
			{
				tmp &= (~(1 << arg));
			}
			else			//关闭arg指定的LED
			{
				tmp |= (1 << arg);
			}	

			//向GPMDAT寄存器写入数据
			iowrite32(tmp, S3C64XX_GPMDAT);
			return 0;

		default:
			return -EINVAL;
	}
}

/**
*接收向LED驱动文件(/dev/s3c6410_leds)写入的数据
**/
static ssize_t leds_write(struct file *file, const char __user *buf, 
							size_t count, loff_t *ppos)
{
	unsigned tmp = count;
	unsigned long i = 0;

	//LED状态清零
	memset(mem, 0, 4);

	if(count > 4)
	{
		tmp = 4;
	}

	//将数据从用户空间复制到内核空间
	if(__copy_from_user(mem, buf, tmp))
	{
		return -EFAULT;
	}
	else
	{
		//控制4个LED的状态
		for(i = 0; i < 4; i++)
		{
			tmp = ioread32(S3C64XX_GPMDAT);
			if(mem[i] == '1')
			{
				tmp &= (~(1 << i));
			}
			else
			{
				tmp |= (1 << i);
			}
			iowrite32(tmp, S3C64XX_GPMDAT);
		}
		return count;
	}
}

//定义file_operations结构体
static struct  file_operations dev_fops =
{
	.owner = THIS_MODULE,
	.unlocked_ioctl = leds_ioctl,
	.write = leds_write
};

//定义cdev结构体，用于描述字符设备
static struct cdev leds_cdev;

//创建设备文件(/dev/s3c6410_leds)
static int leds_create_device(void)
{
	int ret = 0;
	int err = 0;

	//初始化cdev成员,并建立cdev和file_operations之间的连接
	cdev_init(&leds_cdev, &dev_fops);
	leds_cdev.owner = THIS_MODULE;

	if(major > 0)
	{
		//获取设备号(主设备号和次设备号)
		dev_number = MKDEV(major, minor);
		//注册字符设备区
		err = register_chrdev_region(dev_number, DEVICE_COUNT, DEVICE_NAME);
		if(err < 0)
		{
			printk(KERN_WARNING "registrt_chrdev_region() failed\n");
			return err;
		}
	}
	else
	{
		//随机分配设备号，并注册字符设备区
		err = alloc_chrdev_region(&leds_cdev.dev, 10, DEVICE_COUNT, DEVICE_NAME);
		if(err < 0)
		{
			printk(KERN_WARNING "alloc_chrdev_region() fail\n");
			return err;
		}

		major = MAJOR(leds_cdev.dev);
		minor = MINOR(leds_cdev.dev);
		dev_number = leds_cdev.dev;
	}

	//添加字符设备
	ret = cdev_add(&leds_cdev, dev_number, DEVICE_COUNT);
	leds_class = class_create(THIS_MODULE, DEVICE_NAME);

	//创建设备文件
	device_create(leds_class, NULL, dev_number, NULL, DEVICE_NAME);
	
	return ret;
}

//初始化寄存器
static void leds_init_gpm(int leds_default)
{
	int tmp = 0;

	//初始化端口配置寄存器
	tmp = ioread32(S3C64XX_GPMCON);
	tmp &= (~0xFFFF);
	tmp |= 0x1111;	//0001000100010001
	iowrite32(tmp, S3C64XX_GPMCON);

	//初始化端口上拉电阻寄存器
	tmp = ioread32(S3C64XX_GPMPUD);
	tmp &= (~0xFF);
	tmp |= 0xAA;	//01010101
	iowrite32(tmp, S3C64XX_GPMPUD);

	//初始化端口数据寄存器
	tmp = ioread32(S3C64XX_GPMDAT);
	tmp &= (~0xF);
	tmp |= leds_default;
	iowrite32(tmp, S3C64XX_GPMDAT);
}

//初始化LED驱动
static int leds_init(void)
{
	int ret;
	
	ret = leds_create_device();
	leds_init_gpm(~leds_state);
	printk(DEVICE_NAME "\tinitialized\t");

	printk("param0\t%s\n", params[0]);
	printk("param1\t%s\n", params[1]);	
	printk("param1\t%s\n", params[2]);

	return ret;
}

//销毁字符设备
static void leds_destroy_device(void)
{
	//销毁字符设备
	device_destroy(leds_class, dev_number);

	//销毁class结构体
	if(leds_class)
	{
		class_destroy(leds_class);
	}

	//注销字符设备区
	unregister_chrdev_region(dev_number, DEVICE_COUNT);

	return;
}

//卸载LED驱动
static void leds_exit(void)
{	
	leds_destroy_device();
	printk(DEVICE_NAME "\texit!\n");
}

//指定LED驱动的初始化函数
module_init(leds_init);
//指定LED驱动的卸载函数
module_exit(leds_exit);
//指定int类型的模块参数
module_param(leds_state, int, S_IRUGO|S_IWUSR);
//指定数组类型的模块参数
module_param_array(params, charp, &param_size, S_IRUGO|S_IWUSR);
//指定开源协议
MODULE_LICENSE("GPL");
//作者
MODULE_AUTHOR("whx");
