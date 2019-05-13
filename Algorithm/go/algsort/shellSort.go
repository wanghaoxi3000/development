package algsort

import "math"

/*
希尔排序
1. 选择一个增量序列 t1，t2，……，tk，其中 ti > tj, tk = 1
2. 按增量序列个数 k，对序列进行 k 趟排序
3. 每趟排序，根据对应的增量 ti，将待排序列分割成若干长度为 m 的子序列，分别对各子表进行直接插入排序。仅增量因子为 1 时，整个序列作为一个表来处理，表长度即为整个序列的长度。

平均复杂度: O(n log n)
最好情况: O(n log^2 n)
最坏情况: O(n log^2 n)
空间复杂度: O(1)
排序方式: In-place
稳定性: 不稳定
*/
func shellSort(sourceList [100]int) [100]int {
	gap := 1
	for gap < len(sourceList) {
		gap = gap*3 + 1
	}

	for gap > 0 {
		for i := gap; i < len(sourceList); i++ {
			tmp := sourceList[i]
			j := i - gap
			for j >= 0 && sourceList[j] > tmp {
				sourceList[j+gap] = sourceList[j]
				j -= gap
			}
			sourceList[j+gap] = tmp
		}
		gap = int(math.Floor(float64(gap) / 3))
	}

	return sourceList
}
