## Sorting in Go

```go
// sort (ascending order)
sort.Ints(A)
//sort.Sort(sort.IntSlice(A))

// sort in descending order
//sort.Sort(sort.Reverse(sort.IntSlice(A)))
sort.Slice(A, func(i, j int) bool {
    return A[i] > A[j]
})
```

`sort.Interface` 

```go
package sort
type Interface {
    Len() int
    Less(i, j int) bool	// i, j are indices of sequence elements
    Swap(i, j int)
}
```

