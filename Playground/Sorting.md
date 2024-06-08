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

`sort.IntSlice` 

```go
// IntSlice attaches the methods of Interface to []int, sorting in increasing order.
type IntSlice []int

func (x IntSlice) Len() int           { return len(x) }
func (x IntSlice) Less(i, j int) bool { return x[i] < x[j] }
func (x IntSlice) Swap(i, j int)      { x[i], x[j] = x[j], x[i] }
```

`sort.Reverse` 

```go
type reverse struct {
	Interface
}

// Less returns the opposite of the embedded implementation's Less method.
func (r reverse) Less(i, j int) bool {
	return r.Interface.Less(j, i)
}

// Reverse returns the reverse order for data.
func Reverse(data Interface) Interface {
	return &reverse{data}
}
```

