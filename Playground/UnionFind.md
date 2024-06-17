## UnionFind

```go
func countComponents(M [][]int) int {
	n := len(M)
	var uf UnionFind
	uf.Init(n)
	for i := 0; i < n; i++ {
		for j := i+1; j < n; j++ {
			if M[i][j] == 1 {
				uf.Union(i, j)

			}
		}
	}
	return uf.count
}


// UnionFind type definition
type UnionFind struct {
	parent, rank []int
	count int
}

// Init
func (u *UnionFind) Init(n int) {
	u.count = n
	u.rank = make([]int, n)
	u.parent = make([]int, n)
	for i := range u.parent {
		u.parent[i] = i
	}
}

// Find root
func (u *UnionFind) Find(x int) int {
	if u.parent[x] != x {
		u.parent[x] = u.Find(u.parent[x])	// path compression
	}
	return u.parent[x]
}

// Union two nodes
func (u *UnionFind) Union(x, y int) {
	xroot, yroot := u.Find(x), u.Find(y)
	if xroot == yroot {
		return
	}
	if u.rank[xroot] >= u.rank[yroot] {
		u.parent[yroot] = xroot
		if u.rank[xroot] == u.rank[yroot] {
			u.rank[xroot]++
		}
	} else {
		u.parent[xroot] = yroot
	}
	u.count--
}
```

