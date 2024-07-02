## SegmentTree

![segment-tree](_image/segment-tree.jpg)

(Image from [Youtube video](https://www.youtube.com/watch?v=e_bK-dgPvfM&t=1732s)) 

```go
package main

import "fmt"

func main() {
	nums := []int{1,3,5}
	var s SegmentTree
	s.Init(nums)
	fmt.Println(s)

	fmt.Println(s.SumRange(0,2))
	s.Update(1, 2)
	fmt.Println(s.SumRange(0,2))
}


type SegmentTree struct {
	nums []int
	tree []int
}

func (s *SegmentTree) Init(nums []int) {
	n := len(nums)
	s.nums = nums
	s.tree = make([]int, n*4)
	s.build(0, 0, n-1)
}

func (s *SegmentTree) build(node, start, end int) {
	if start == end {
		s.tree[node] = s.nums[start]
		return
	}
	m := start + (end-start)/2
	leftNode, rightNode := 2*node+1, 2*node+2
	s.build(leftNode, start, m)
	s.build(rightNode, m+1, end)
	s.tree[node] = s.tree[leftNode] + s.tree[rightNode]
}

func (s *SegmentTree) Update(i, val int) {
	s.update(i, val, 0, 0, len(s.nums)-1)
}

func (s *SegmentTree) update(i, val, node, start, end int) {
	if start == end {
		s.tree[node] = val
		return
	}
	leftNode, rightNode := 2*node+1, 2*node+2
	m := start + (end-start)/2
	if i <= m {
		s.update(i, val, leftNode, start, m)
	} else {
		s.update(i, val, rightNode, m+1, end)
	}
	s.tree[node] = s.tree[leftNode] + s.tree[rightNode]
}

func (s *SegmentTree) SumRange(left, right int) int {
	return s.sum(left, right, 0, 0, len(s.nums)-1)
}

func (s *SegmentTree) sum(left, right int, node, start, end int) int {
	if left == start && right == end {
		return s.tree[node]
	}
	leftNode, rightNode := 2*node+1, 2*node+2
	m := start + (end-start)/2
	if right <= m {
		return s.sum(left, right, leftNode, start, m)
	}
	if left > m {
		return s.sum(left, right, rightNode, m+1, end)
	}
	return s.sum(left, m, leftNode, start, m) + s.sum(m+1, right, rightNode, m+1, end)
}
```

