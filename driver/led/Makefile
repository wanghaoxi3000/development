ifeq ($(KERNELRELEASE),)

PWD := $(shell pwd)
KERNELDIR ?= /home/whx/eabi/linux/linux-3.0.1
#INSTALLDIR ?= /home/whx/

modules:
	$(MAKE) -C $(KERNELDIR) M=$(PWD) modules

#modules_install:
#	$(MAKE) -C $(KERNELDIR) M=$(PWD) INSTALL_MOD_PATH=$(INSTALLDIR) modules_install
clean:
	rm -rf *.o *.ko *.mod.c .*.cmd modules.order Module.symvers .tmp_versions

else

obj-m := led_drive.o

endif
