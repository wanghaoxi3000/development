package algsort

/*
选择排序
1. 首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置
2. 再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
3. 重复第二步，直到所有元素均排序完毕。

平均复杂度: O(n^2)
最好情况: O(n^2)
最坏情况: O(n^2)
空间复杂度: O(1)
排序方式: In-place
稳定性: 不稳定
*/

func selectionSort(sourceList [100]int) [100]int {
	for minIndex := 0; minIndex < len(sourceList)-1; minIndex++ {
		for selectIndex := minIndex + 1; selectIndex < len(sourceList); selectIndex++ {
			if sourceList[selectIndex] < sourceList[minIndex] {
				sourceList[selectIndex], sourceList[minIndex] = sourceList[minIndex], sourceList[selectIndex]
			}
		}
	}

	return sourceList
}
