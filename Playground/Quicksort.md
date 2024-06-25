## 🍺 Quicksort & Quickselect using Hoare Partition

Hoare partition works best in most cases. Even when there are many **duplicate** numbers, it can still partition the numbers evenly. But it is much harder to understand and implement.

> Refer to [QuickSelect with Hoare partition scheme](https://stackoverflow.com/questions/58331986/quickselect-with-hoare-partition-scheme) 
>
> `partition` function:
>
> The first half `A[p..m]` <= pivot, and the second half `A[m+1..n)` >= pivot.

```go
package main

import "fmt"

func main() {
    nums := []int{3, 2, 6, 8, 3, 1, 5}
    quicksort(nums, 0, len(nums)-1)
    fmt.Println(nums)

    for k := range nums {
      fmt.Print(" ", quickselect(nums, k))
    }
}

func quicksort(nums []int, p, q int) {
	if p < q {
		m := partition(nums, p, q)
		quicksort(nums, p, m)
		quicksort(nums, m+1, q)
	}
}

func quickselect(nums []int, k int) int {
	p, q := 0, len(nums)-1
	for p <= q {
		m := partition(nums, p, q)
		if p == q {
			return nums[q]
		}
		if m >= k {
			q = m
		} else {
			p = m+1
		}
	}
	return -1
}

func partition(nums []int, p, q int) int {
	pivot := nums[p]
	i, j := p-1, q+1
	for {
		i++; j--
		for nums[i] < pivot { i++ }
		for nums[j] > pivot { j-- }
		if i >= j {
			return j
		}
		nums[i], nums[j] = nums[j], nums[i]
	}
}
```

> Choosing number in the middle as pivot would make it better, i.e. `pivot := nums[(p+q)/2]` . Or even better, we can choose pivot randomly:
>
> ```go
> func quicksort(nums []int, k int) int {
> 	// initialize rand
> 	rand.Seed(time.Now().UnixNano())
> 
> 	// ...
> }
> 
> func partition(nums []int, p, q int) int {
> 	// choose a random location and swap to first
> 	r := p + rand.Intn(q-p+1)
> 	nums[p], nums[r] = nums[r], nums[p]
> 
> 	// ...
> }
> ```
>



## 🍺 Time Complexity of Quickselect

Get kth smallest element of `nums`. (k is 0-based)

Average Time Complexity: $n + n/2 + n/4 + ... + n/n = 2n-1 = O(n)$ 

Worst Time Complexity: $O(n^2)$ 







---

## Appendix: Quicksort & Quickselect in TextBooks

This approach is more intuitive and easier to implement. But when there are many **duplicates** in the array, the partition cannot divide the array evenly, so we will unavoidably hit worst case $O(n^2)$  -- Choosing pivot randomly won't help.

> `partition` function:
>
> The first half `A[p..m-1]` <= pivot, the middle `A[m]` = pivot, and the second half `A[m+1..n)` > pivot.

```go
package main

import "fmt"

func main() {
    nums := []int{3, 2, 6, 8, 3, 1, 5}
    quicksort(nums, 0, len(nums)-1)
    fmt.Println(nums)

    for k := range nums {
      fmt.Print(" ", quickselect(nums, k))
    }
}

func quicksort(nums []int, p, q int) {
  if p < q {
    m := partition(nums, p, q)
    quicksort(nums, p, m-1)
    quicksort(nums, m+1, q)
  }
}

func quickselect(nums []int, k int) int {
	p, q := 0, len(nums)-1
	for p <= q {
		m := partition(nums, p, q)
		if m == k {
			return nums[m]
		}
		if m > k {
			q = m-1
		} else {
			p = m+1
		}
	}
	return -1
}

func partition(nums []int, p, q int) int {
	pivot := nums[q]
	m := p
	for i := p; i < q; i++ {
		if nums[i] <= pivot {
			nums[i], nums[m] = nums[m], nums[i]
			m++
		}
	}
	// swap pivot to right position 'm'
	nums[q], nums[m] = nums[m], nums[q]
	return m
}
```

