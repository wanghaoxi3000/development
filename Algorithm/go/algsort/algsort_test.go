package algsort

import (
	"math/rand"
	"sort"
	"testing"
	"time"
)

func TestBubbleSort(t *testing.T) {
	randomList := [100]int{}
	sortedList := [100]int{}
	var testList [100]int

	rand.Seed(time.Now().UnixNano())
	var num int
	for i := range randomList {
		num = rand.Intn(100)
		randomList[i] = num
		sortedList[i] = num
	}
	sort.Ints(sortedList[:])

	testList = bubbleSort(randomList)
	if testList != sortedList {
		t.Errorf("test bubble sort fail, sort ret: %v", testList)
	}

	testList = selectionSort(randomList)
	if testList != sortedList {
		t.Errorf("test selection sort fail, sort ret: %v", testList)
	}

	testList = insertSort(randomList)
	if testList != sortedList {
		t.Errorf("test insert sort fail, sort ret: %v", testList)
	}

	testList = shellSort(randomList)
	if testList != sortedList {
		t.Errorf("test short sort fail, sort ret: %v", testList)
	}

	testList = quickSort(randomList)
	if testList != sortedList {
		t.Errorf("test quick sort fail, sort ret: %v", testList)
	}
}
