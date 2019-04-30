package algsort

/*
插入排序
1. 将第一待排序序列第一个元素看做一个有序序列，把第二个元素到最后一个元素当成是未排序序列。
2. 从头到尾依次扫描未排序序列，将扫描到的每个元素插入有序序列的适当位置。（如果待插入的元素与有序序列中的某个元素相等，则将待插入元素插入到相等元素的后面。）

平均复杂度: O(n^2)
最好情况: O(n)
最坏情况: O(n^2)
空间复杂度: O(1)
排序方式: In-place
稳定性: 稳定
*/

func insertSort(sourceList [100]int) [100]int {
	for i := 1; i < len(sourceList); i++ {
		for j := i; j > 0; j-- {
			if sourceList[j] < sourceList[j-1] {
				sourceList[j], sourceList[j-1] = sourceList[j-1], sourceList[j]
			} else {
				break
			}
		}
	}

	return sourceList
}
