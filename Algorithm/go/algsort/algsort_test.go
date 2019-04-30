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
		t.Errorf("test bubble sort fail, sort ret: %v", sortedList)
	}

	testList = selectionSort(randomList)
	if testList != sortedList {
		t.Errorf("test selection sort fail, sort ret: %v", sortedList)
	}

	testList = insertSort(randomList)
	if testList != sortedList {
		t.Errorf("test insert sort fail, sort ret: %v", sortedList)
	}
}
