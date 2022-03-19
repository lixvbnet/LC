## [79 · Longest Common Substring](https://www.lintcode.com/problem/79/description)

**Description**

Given two strings, find the longest common substring.

Return the length of it.

Note: The characters in **substring** should occur continuously in original string. This is different with **subsequence**.

**Example**

**Example 1:**

Input:

```
stringA = "ABCD"
stringB = "CBCE"
```

Output:

```
2
```

Explanation:

Longest common substring is "BC"

**Example 2:**

Input:

```
stringA = "ABCD"
stringB = "EACB"
```

Output:

```
1
```

Explanation:

Longest common substring is 'A' or 'C' or 'B'

**Challenge**

O(n x m) time and memory.



## Solution

- Dynamic Programming	$Time: O(n*m), Space: O(n*m)$ or $O(m)$ or $O(1)$ ?

```go
// M(i, j): Length of Longest Common Substring that ends with index i-1 in A and j-1 in B
// If A[i-1]==B[j-1], then M(i, j) = 1 + M(i-1, j-1), else M(i, j) = 0
// M(0, j) = M(i, 0) = 0
func longestCommonSubstring (A string, B string) int {
    n, m := len(A), len(B)
    dp := make([][]int, n+1)
    for i := range dp {
        dp[i] = make([]int, m+1)
    }

    result := 0
    for i := 1; i <= n; i++ {
        for j := 1; j <= m; j++ {
            if A[i-1] == B[j-1] {
                dp[i][j] = 1 + dp[i-1][j-1]
            } else {
                dp[i][j] = 0
            }
            result = max(result, dp[i][j])
        }
    }
    return result
}

func max(x, y int) int {
    if x > y {
        return x
    }
    return y
}
```

Since the calculation only depends only values in last row, we can reduce memory usage by storing only one row. ⚠️ **Note: the inner loop should be in reverse order**.

```go
// M(i, j): Length of Longest Common Substring that ends with index i-1 in A and j-1 in B
// If A[i-1]==B[j-1], then M(i, j) = 1 + M(i-1, j-1), else M(i, j) = 0
// M(0, j) = M(i, 0) = 0
func longestCommonSubstring (A string, B string) int {
    n, m := len(A), len(B)
    dp := make([]int, m+1)

    result := 0
    for i := 1; i <= n; i++ {
        // iterate in reverse order
        for j := m; j >= 1; j-- {
            if A[i-1] == B[j-1] {
                dp[j] = 1 + dp[j-1]
            } else {
                dp[j] = 0
            }
            result = max(result, dp[j])
        }
    }
    return result
}

func max(x, y int) int {
    if x > y {
        return x
    }
    return y
}
```

**Possible further improvement**: When calculating M(i, j), we only need to reference M(i-1, j-1). So if we fill the `dp`  table in diagonal order, we can reduce memory usage to $O(1)$ .
