## [659 · Encode and Decode Strings](https://www.lintcode.com/problem/659/)

**Description**

Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Please implement `encode` and `decode`

**Example**

**Example1**

```
Input: ["lint","code","love","you"]
Output: ["lint","code","love","you"]
Explanation:
One possible encode method is: "lint:;code:;love:;you"
```

**Example2**

```
Input: ["we", "say", ":", "yes"]
Output: ["we", "say", ":", "yes"]
Explanation:
One possible encode method is: "we:;say:;:::;yes"
```



## Solution

- Approach 1: `length#strs[i]` 

```go
// length#strs[i]
func encode(strs []string) string {
	var sb strings.Builder
	for _, s := range strs {
		sb.WriteString(strconv.Itoa(len(s)) + "#" + s)
	}
	return sb.String()
}

func decode(str string) []string {
	var result []string
	i := 0
	for i < len(str) {
		j := i
		for str[j] != '#' {
			j++
		}
		length, _ := strconv.Atoi(str[i:j])
		result = append(result, str[j+1:j+1+length])
		i = j+1+length
	}

	return result
}
```



- Approach 2: Escape

> Choose a delimiter, say `#`, escape `#` in strings with `/#` and escape `/` with `//`.

```go
// # -> /#
// / -> //
func encode(strs []string) string {
	n := len(strs)
	var sb strings.Builder
	for i, s := range strs {
		for _, c := range s {
			if c == '#' || c == '/' {
				sb.WriteByte('/')
			}
			sb.WriteRune(c)
		}
		if i < n-1 {
			sb.WriteByte('#')
		}
	}
	return sb.String()
}

func decode(str string) []string {
	var result []string
	var sb strings.Builder
	for i := 0; i < len(str); i++ {
		if str[i] == '#' {
			result = append(result, sb.String())
			sb.Reset()
			continue
		}

		if str[i] == '/' {
			i++
		}
		sb.WriteByte(str[i])
	}
	result = append(result, sb.String())
	return result
}
```



