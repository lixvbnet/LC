## MergeSort

```go
package main

import "fmt"

func main() {
	nums := []int{3,1,2,7,0}
	mergeSort(nums, 0, len(nums)-1)
	fmt.Println(nums)
}

func mergeSort(nums []int, p, q int) {
    if p < q {
        m := (p+q)/2
        mergeSort(nums, p, m)
        mergeSort(nums, m+1, q)
        merge(nums, p, m, q)
    }
}

func merge(nums []int, p, m, q int) {
    tmp := make([]int, q-p+1)
    index := 0
    i, j := p, m+1
    for i <= m || j <= q {
        if i > m || (j <= q && nums[j] < nums[i]) {
            tmp[index] = nums[j]
            index++; j++
        } else {
            tmp[index] = nums[i]
            index++; i++
        }
    }
    // copy back
    copy(nums[p:], tmp)
}
```

> Alternatively, we can do Reverse Merge, i.e., start the pointers from last elment and merge larger ones first.

