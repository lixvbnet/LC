## Quicksort

First partition `nums` into two parts, then sort them by recursive calls.

![2018-12-27-20-26-11](_image/2018-12-27-20-26-11.jpg)

`partition` function:

![2018-12-27-20-44-29](_image/2018-12-27-20-44-29.jpg)

```go
func main() {
	nums := []int{3,1,2,7,0}
	quicksort(nums)
	fmt.Println(nums)
}

func quicksort(nums []int) {
	qsort(nums, 0, len(nums)-1)
}

func qsort(nums []int, p, q int) {
	if p >= q {
		return
	}

	r := partition(nums, p, q)
	qsort(nums, p, r-1)
	qsort(nums, r+1, q)
}

// A[p..r) always contains elements that are <= pivot
// Start with r = p, if A[i] <= pivot, then swap A[i] with A[r] and increment r
// Lastly, swap pivot to position r
func partition(nums []int, p, q int) int {
	r := p
	pivot := nums[q]	// here choose last element as pivot
	for i := p; i < q; i++ {
		if nums[i] <= pivot {
			nums[i], nums[r] = nums[r], nums[i]
			r++
		}
	}
	// swap pivot to right position 'r'
	nums[q], nums[r] = nums[r], nums[q]
	return r
}
```



## getKthElement

Get kth smallest element of `nums`. (k is 0-based)

> Make use of partition function, then use binary search.

- Recusive

```go
func getKthElement(nums []int, k int) int {
	return helper(nums, k, 0, len(nums)-1)
}

func helper(nums []int, k int, p, q int) int {
	r := partition(nums, p, q)
	if r == k {
		return nums[r]
	} else if r > k {
		return helper(nums, k, p, r-1)
	} else {
		return helper(nums, k, r+1, q)
	}
}

// A[p..r) always contains elements that are <= pivot
// Start with r = p, if A[i] <= pivot, then swap A[i] with A[r] and increment r
// Lastly, swap pivot to position r
func partition(nums []int, p, q int) int {
	r := p
	pivot := nums[q]	// here choose last element as pivot
	for i := p; i < q; i++ {
		if nums[i] <= pivot {
			nums[i], nums[r] = nums[r], nums[i]
			r++
		}
	}
	// swap pivot to its right position 'r'
	nums[q], nums[r] = nums[r], nums[q]
	return r
}
```

- Iterative

```go
func getKthElement(nums []int, k int) int {
	// A[low..high)
	low, high := 0, len(nums)
	for low < high {
		r := partition(nums, low, high-1)
		if r == k {
			return nums[r]
		}

		if r > k {
			high = r
		} else {
			low = r + 1
		}
	}
	return -1
}
```

Time Complexity:

$n + n/2 + n/4 + ... + n/n = 2n-1 = O(n)$ 

Worst Time Complexity: $O(n^2)$ 



We can choose random pivot each time:

```go
func getKthElement(nums []int, k int) int {
	// initialize rand
	rand.Seed(time.Now().UnixNano())

	// A[low..high)
	low, high := 0, len(nums)
	for low < high {
		r := partition(nums, low, high-1)
		if r == k {
			return nums[r]
		}
		if r > k {
			high = r
		} else {
			low = r + 1
		}
	}
	return -1
}

// A[p..r) always contains elements that are <= pivot
// Start with r = p, if A[i] <= pivot, then swap A[i] with A[r] and increment r
// Lastly, swap pivot to position r
func partition(nums []int, p, q int) int {
	// choose a random location and swap to last
	i := p + rand.Intn(q-p+1)
	nums[i], nums[q] = nums[q], nums[i]

	r := p
	pivot := nums[q]	// here choose last element as pivot
	for i := p; i < q; i++ {
		if nums[i] <= pivot {
			nums[i], nums[r] = nums[r], nums[i]
			r++
		}
	}
	// swap pivot to its right position 'r'
	nums[q], nums[r] = nums[r], nums[q]
	return r
}
```





---



## Quicksort using Hoare Partitioning

```go
package main

import "fmt"

func main() {
	nums := []int{3, 2, 6, 8, 3, 1, 5}
	quicksort(nums)
	fmt.Println(nums)
}


func quicksort(nums []int) {
	qsort(nums, 0, len(nums)-1)
}

func qsort(nums []int, low, high int) {
    if low < high {
        r := partition(nums, low, high)
        qsort(nums, low, r)
        qsort(nums, r+1, high)
    }
}

func partition(nums []int, low, high int) int {
    i := low-1
    j := high+1
    pivot := nums[low]

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



## getKthElement using Hoare Partitioning

```go
func getKthElement(nums []int, k int) int {
    k = k-1         // Why???
    i, j := 0, len(nums)-1
    for i <= j {
        if i == j {
            return nums[j]
        }
        r := partition(nums, i, j)
        if r > k {
            j = r
        } else {
            i = r+1
        }
    }
    return -1
}

func partition(nums []int, low, high int) int {
    i := low-1
    j := high+1
    pivot := nums[low]

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

> Yet another implementation
>
> ```go
> func getKthElement(nums []int, k int) int {
>     n := len(nums)
>     return quickselect(nums, k, 0, n-1)
> }
> 
> func quickselect(nums []int, k, l, r int) int {
>     if l == r{
>         return nums[k]
>     }
> 
>     pivot := nums[l]
>     i := l-1
>     j := r+1
>     for i < j {
>         i++; j--
>         for nums[i] < pivot { i++ }
>         for nums[j] > pivot { j-- }
>         if i < j {
>             nums[i], nums[j] = nums[j], nums[i]
>         }
>     }
>     if k <= j {
>         return quickselect(nums, k, l, j)
>     } else {
>         return quickselect(nums, k, j+1, r)
>     }
> }
> ```
>