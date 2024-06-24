## Trie

```go
type Trie struct {
    isEnd bool
    children map[rune]*Trie
}


func Constructor() Trie {
    return Trie{children: make(map[rune]*Trie)}
}

func (t *Trie) Insert(word string)  {
    cur := t
    for _, c := range word {
        if cur.children[c] == nil {
            cur.children[c] = &Trie{children: make(map[rune]*Trie)}
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

We can use an array instead of hashmap:

```go
type Trie struct {
    isEnd bool
    children [26]*Trie
}

func Constructor() Trie {
    return Trie{}
}

func (t *Trie) Insert(word string)  {
    cur := t
    for _, c := range word {
        c -= 'a'
        if cur.children[c] == nil {
            cur.children[c] = &Trie{}
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

