package algsort

/*
快速排序
1. 从数列中挑出一个元素，称为 “基准”（pivot）;
2. 重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。在这个分区退出之后，该基准就处于数列的中间位置。这个称为分区（partition）操作；
3. 递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序；

平均复杂度: O(n log n)
最好情况: O(n log n)
最坏情况: O(n^2)
空间复杂度: O(log n)
排序方式: In-place
稳定性: 不稳定
*/

func quickSort(sourceList [100]int) [100]int {
	var sortfunc func(arr []int, left int, right int)

	sortfunc = func(arr []int, left int, right int) {
		if left < right {
			pivot := left
			index := pivot + 1
			for i := index; i <= right; i++ {
				if arr[i] < arr[pivot] {
					arr[i], arr[index] = arr[index], arr[i]
					index++
				}
			}
			arr[pivot], arr[index-1] = arr[index-1], arr[pivot]
			index--
			sortfunc(arr, left, index-1)
			sortfunc(arr, index+1, right)
		}
	}

	sortfunc(sourceList[:], 0, len(sourceList)-1)
	return sourceList
}
