## Trie

If only consists lower-case letters, we can use an array to store children map.

```go
type Trie struct {
    isEnd bool
    children [26]*Trie
}

func NewTrie() *Trie {
    return &Trie{}
}

func (t *Trie) Insert(word string)  {
    cur := t
    for _, c := range word {
        c -= 'a'
        if cur.children[c] == nil {
            cur.children[c] = NewTrie()
        }
        cur = cur.children[c]
    }
    cur.isEnd = true
}

func (t *Trie) Search(word string) bool {
    cur := t
    for _, c := range word {
        c -= 'a'
        if cur.children[c] == nil {
            return false
        }
        cur = cur.children[c]
    }
    return cur.isEnd
}


func (t *Trie) StartsWith(prefix string) bool {
    cur := t
    for _, c := range prefix {
        c -= 'a'
        if cur.children[c] == nil {
            return false
        }
        cur = cur.children[c]
    }
    return true
}
```



For more general scenarios, use a hashmap:

```go
type Trie struct {
    isEnd bool
    children map[rune]*Trie
}

func NewTrie() *Trie {
    return &Trie{children: make(map[rune]*Trie)}
}

func (t *Trie) Insert(word string)  {
    cur := t
    for _, c := range word {
        if cur.children[c] == nil {
            cur.children[c] = NewTrie()
        }
        cur = cur.children[c]
    }
    cur.isEnd = true
}

func (t *Trie) Search(word string) bool {
    cur := t
    for _, c := range word {
        if cur.children[c] == nil {
            return false
        }
        cur = cur.children[c]
    }
    return cur.isEnd
}

func (t *Trie) StartsWith(prefix string) bool {
    cur := t
    for _, c := range prefix {
        if cur.children[c] == nil {
            return false
        }
        cur = cur.children[c]
    }
    return true
}
```

