## Heap & PriorityQueue

One less efficient approach for [347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) , but useful to demonstrate how to use Heap/PriorityQueue in Go.

```go
func topKFrequent(nums []int, k int) []int {
	count := make(map[int]int)
	for _, num := range nums {
		count[num]++
	}

	q := new(PriorityQueue)
	for num, c := range count {
		*q = append(*q, &Item{num, c})
	}
	heap.Init(q)	// O(n)

	var result []int
	for i := 0; i < k; i++ {
		top := heap.Pop(q).(*Item)
		result = append(result, top.num)
	}
	return result
}


type Item struct {
	num		int
	count	int
}

// A PriorityQueue implements heap.Interface and holds Items.
type PriorityQueue []*Item

func (q PriorityQueue) Len() int {
	return len(q)
}
func (q PriorityQueue) Less(i, j int) bool {
	return q[i].count > q[j].count	// making it a MaxHeap for count
}
func (q PriorityQueue) Swap(i, j int) {
	q[i], q[j] = q[j], q[i]
}

func (q *PriorityQueue) Push(x interface{}) {
	item := x.(*Item)
	*q = append(*q, item)
}

func (q *PriorityQueue) Pop() interface{} {
	n := len(*q)
	item := (*q)[n-1]
	*q = (*q)[:n-1]
	return item
}
```

