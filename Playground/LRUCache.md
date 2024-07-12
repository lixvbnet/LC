## [146. LRU Cache](https://leetcode.com/problems/lru-cache/) 

```go
type Node struct {
    Key, Val int
    Pre, Next *Node
}

type LRUCache struct {
    capacity int
    // map: key -> node
    m map[int]*Node
    head, tail *Node
}

func (l *LRUCache) Init(capacity int) {
    l.capacity = capacity
    l.m = make(map[int]*Node)
    l.head, l.tail = &Node{}, &Node{}
    l.head.Next = l.tail
    l.tail.Pre = l.head
}

func (l *LRUCache) remove(node *Node) {
    delete(l.m, node.Key)
    pre, next := node.Pre, node.Next
    pre.Next = next
    next.Pre = pre
}

func (l *LRUCache) insertFirst(node *Node) {
    l.m[node.Key] = node
    first := l.head.Next
    l.head.Next = node
    node.Pre = l.head
    node.Next = first
    first.Pre = node
}

func (l *LRUCache) moveToFirst(node *Node) {
    l.remove(node)
    l.insertFirst(node)
}


func Constructor(capacity int) LRUCache {
    var l LRUCache
    l.Init(capacity)
    return l
}

func (l *LRUCache) Get(key int) int {
    node := l.m[key]
    if node == nil {
        return -1
    }
    l.moveToFirst(node)
    return node.Val
}

func (l *LRUCache) Put(key int, value int)  {
    // if already exists, update
    if l.Get(key) != -1 {   // order updated
        l.m[key].Val = value
        return
    }
    // if size reaches capacity, remove last node
    if len(l.m) == l.capacity {
        l.remove(l.tail.Pre)
    }
    // insert newNode
    l.insertFirst(&Node{Key: key, Val: value})
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * obj := Constructor(capacity);
 * param_1 := obj.Get(key);
 * obj.Put(key,value);
 */
```

