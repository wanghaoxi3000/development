## 算法
### 排序算法 https://mp.weixin.qq.com/s/vn3KiV-ez79FmbZ36SX9lg
![image](https://mmbiz.qpic.cn/mmbiz_png/D67peceibeISwc3aGibUlvZ0XqVnbWtBRiaKhGcwh6KibXbSiadtHqwgjmmzBYCa2DNuj5Vhw3lHc96z1wge3ZbDAeg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

#### 关于时间复杂度：
1. 平方阶 (O(n2)) 排序 各类简单排序：直接插入、直接选择和冒泡排序。
2. 线性对数阶 (O(nlog2n)) 排序 快速排序、堆排序和归并排序；
3. O(n1+§)) 排序，§ 是介于 0 和 1 之间的常数。 希尔排序
4. 线性阶 (O(n)) 排序 基数排序，此外还有桶、箱排序。

#### 关于稳定性：
1. 稳定的排序算法：冒泡排序、插入排序、归并排序和基数排序。
2. 不是稳定的排序算法：选择排序、快速排序、希尔排序、堆排序。

#### 冒泡排序
##### 算法步骤
1. 比较相邻的元素。如果第一个比第二个大，就交换他们两个。
2. 对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数。
3. 针对所有的元素重复以上的步骤，除了最后一个。

持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。

#### 动画演示
![image](https://mmbiz.qpic.cn/mmbiz_gif/D67peceibeISwc3aGibUlvZ0XqVnbWtBRiaC1S2jpXRzXcZVn0aP6BYnkO2FJicNstxicHmf9wMIic5FV0I75ptv5jYA/640?wx_fmt=gif&tp=webp&wxfrom=5&wx_lazy=1)

#### 选择排序
##### 算法步骤
1. 首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置
2. 再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
3. 重复第二步，直到所有元素均排序完毕。

##### 动画演示
![image](https://mmbiz.qpic.cn/mmbiz_gif/D67peceibeISwc3aGibUlvZ0XqVnbWtBRiaB2dW1vA5SganRPChytYTFiaJL2PkXlL7XmhYmqIAzBHj0VvgJZs0vmA/640?wx_fmt=gif&tp=webp&wxfrom=5&wx_lazy=1)

#### 插入排序
##### 算法步骤
1. 将第一待排序序列第一个元素看做一个有序序列，把第二个元素到最后一个元素当成是未排序序列。
2. 从头到尾依次扫描未排序序列，将扫描到的每个元素插入有序序列的适当位置。（如果待插入的元素与有序序列中的某个元素相等，则将待插入元素插入到相等元素的后面。）

##### 动画演示
![image](https://mmbiz.qpic.cn/mmbiz_gif/D67peceibeISwc3aGibUlvZ0XqVnbWtBRiaiatKZU4exjwcluduiclJOdZB0oZQicCrpIEaSJJg8iaia58viauSK3nhofqA/640?wx_fmt=gif&tp=webp&wxfrom=5&wx_lazy=1)