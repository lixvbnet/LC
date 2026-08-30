## [920 · Meeting Rooms](https://www.lintcode.com/problem/920/) 

**Description** 

Given an array of meeting time intervals consisting of start and end times `[[s1,e1],[s2,e2],...] (si < ei)`, determine if a person could attend all meetings.

Note: (0,8),(8,10) is not conflict at 8

**Example** 

**Example1**

```
Input: intervals = [(0,30),(5,10),(15,20)]
Output: false
Explanation: 
(0,30), (5,10) and (0,30),(15,20) will conflict
```

**Example2**

```
Input: intervals = [(5,8),(9,15)]
Output: true
Explanation: 
Two times will not conflict 
```



## Solution

- Sorting	$Time: O(nlogn)$ 

> Note: In LintCode, we need to add the `import` statements on our own.

```go
/**
 * Definition of Interval:
 * type Interval struct {
 *     Start, End int
 * }
 */

import "sort"

func CanAttendMeetings(intervals []*Interval) bool {
    // sort
    sort.Slice(intervals, func(i, j int) bool {
        return intervals[i].Start < intervals[j].Start
    })

    for i := 1; i < len(intervals); i++ {
        if intervals[i].Start < intervals[i-1].End {
            return false
        }
    }
    return true
}
```

