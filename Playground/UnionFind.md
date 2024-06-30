## UnionFind

> UnionFind with path compression, and simple union function. -- **Good for quick implementation**

```go
func main() {
  n := 3
  var uf UnionFind
  uf.Init(n)
  
  uf.Union(0, 1)
  uf.Union(1, 2)
}


type UnionFind struct {
    parent []int
    count int
}

func (u *UnionFind) Init(n int) {
    u.count = n
    u.parent = make([]int, n)
    for i := range u.parent {
        u.parent[i] = i
    }
}

func (u *UnionFind) Find(x int) int {
    if u.parent[x] != x {
        u.parent[x] = u.Find(u.parent[x])	// path compression
    }
    return u.parent[x]
}

func (u *UnionFind) Union(x, y int) {
    xroot, yroot := u.Find(x), u.Find(y)
    u.parent[xroot] = yroot
    u.count--
}
```



## Union by rank

> "rank" is height of a tree. The goal is to make tree heights as small as possible.

```go
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



## Union by size

> With path compression, "Union by rank" and "Union by size" are very similar.

If we need to get sizes of the components, use following variant instead:

> See [2316. Count Unreachable Pairs of Nodes in an Undirected Graph](https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/) 

```go
func countPairs(n int, edges [][]int) int64 {
    var uf UnionFind
    uf.Init(n)
    for _, edge := range edges {
        uf.Union(edge[0], edge[1])
    }
    var result int64
    for i := 0; i < n; i++ {
        result += int64(n - uf.size[uf.Find(i)])
    }
    return result / 2
}


type UnionFind struct {
    parent, size []int
}

func (u *UnionFind) Init(n int) {
    u.parent = make([]int, n)
    u.size = make([]int, n)
    for i := 0; i < n; i++ {
        u.parent[i] = i
        u.size[i] = 1
    }
}

func (u *UnionFind) Find(x int) int {
    if u.parent[x] != x {
        u.parent[x] = u.Find(u.parent[x])
    }
    return u.parent[x]
}

func (u *UnionFind) Union(x, y int) {
    xroot, yroot := u.Find(x), u.Find(y)
    if xroot == yroot {
        return
    }
    if u.size[xroot] >= u.size[yroot] {
        u.parent[yroot] = xroot
        u.size[xroot] += u.size[yroot]
    } else {
        u.parent[xroot] = yroot
        u.size[yroot] += u.size[xroot]
    }
}
```

