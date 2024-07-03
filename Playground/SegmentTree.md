## SegmentTree

(Image from [Youtube video](https://www.youtube.com/watch?v=e_bK-dgPvfM&t=1732s)) 

![segment-tree](_image/segment-tree.jpg)

> [Why does 4 * N space have to be allocated for a segment tree, where N is the size of the original array?](https://www.quora.com/Why-does-4-*-N-space-have-to-be-allocated-for-a-segment-tree-where-N-is-the-size-of-the-original-array) 
>
> For array `A` of size `n` , the segment tree `st` has `2n-1` non-empty nodes. But it is a **full binary tree** , the actual space we need:
>
> |                          | Actual space needed                                          | Tree height |
> | ------------------------ | ------------------------------------------------------------ | ----------- |
> | if `n` is power of 2     | $S(n) = 2n-1$                                                | $log_2 n$   |
> | if `n` is NOT power of 2 | $S(n) = 2x-1$, where $x > n$ is <br />next integer that is power of 2. | $log_2 x$   |
>
> For example,
>
> - if `n` is power of 2, `st` will have `2n-1` nodes (`n` leaf nodes and `n-1` internal nodes)
> - if we increase only 1 element to `A` , `st` gets doubled. (`n` leaf nodes, `n-1` internal nodes, and `2(n-1)-2` nodes are unused. -- Close to `4n` (upper bound) nodes in total.)
>
> Conclusion without proof: ==4 is the smallest $k$ that it's safe to assume the space is sufficient for usage==.

```go
package main

import "fmt"

func main() {
	nums := []int{1,3,5}
	var s ST
	s.Init(nums)
	fmt.Println(s)

	fmt.Println(s.SumRange(0,2))
	s.Update(1, 2)
	fmt.Println(s.SumRange(0,2))
}


// ST type definition
type ST struct {
	nums []int
	tree []int
}

// Init
func (s *ST) Init(nums []int) {
	n := len(nums)
	s.nums = nums
	s.tree = make([]int, n*4)
	s.build(0, 0, n-1)
}

// Update nums[i]
func (s *ST) Update(i, val int) {
	s.update(i, val, 0, 0, len(s.nums)-1)
}

// SumRange nums[L...R] inclusive
func (s *ST) SumRange(L, R int) int {
	return s.sum(L, R, 0, 0, len(s.nums)-1)
}

func (s *ST) build(node, start, end int) {
	if start == end {
		s.tree[node] = s.nums[start]
		return
	}
	leftNode, rightNode := 2*node+1, 2*node+2
	mid := (start+end)/2
	s.build(leftNode, start, mid)
	s.build(rightNode, mid+1, end)
	s.tree[node] = s.tree[leftNode] + s.tree[rightNode]
}

func (s *ST) update(i, val int, node, start, end int) {
	if start == end {
		s.nums[i] = val
		s.tree[node] = val
		return
	}
	leftNode, rightNode := 2*node+1, 2*node+2
	mid := (start+end)/2
	if i <= mid {
		s.update(i, val, leftNode, start, mid)
	} else {
		s.update(i, val, rightNode, mid+1, end)
	}
	s.tree[node] = s.tree[leftNode] + s.tree[rightNode]
}

func (s *ST) sum(L, R int, node, start, end int) int {
	if L == start && R == end {
		return s.tree[node]
	}
	leftNode, rightNode := 2*node+1, 2*node+2
	mid := (start+end)/2
	if R <= mid {
		return s.sum(L, R, leftNode, start, mid)
	}
	if L > mid {
		return s.sum(L, R, rightNode, mid+1, end)
	}
	return s.sum(L, mid, leftNode, start, mid) + s.sum(mid+1, R, rightNode, mid+1, end)
}
```

