# Recursion

## I. Simple recursion as a replacement for a loop

Problems in this section will use recursion as an alternative to a procedural loop. They will be typically concerned with flat structures such as lists, rather then inherently recursive ones like trees.

### A. Simple problems


#### 1. List filtering


Prerequisites:
 - List unpacking, e.g. `fst, *rest = list` and the like
 - Lambdas, e.g. `lambda x: x > 0`
 - Passing functions as arguments to other functions
 - Joining lists with `+`

The problem

Write a function `list_filter(lst, pred)`, which takes a list `lst` of elements of arbitrary type, and a predicate function `pred`, which must returna boolean (`True` or `False`) on any single element of `lst`, and returns a new list, whose elements are all those of `lst` for which `pred` returns `True`.

The implementation of `list_filter(lst, pred)` should use recursion, loops are not allowed. Performance is not a consideration at this point.

Examples of use:

    list_filter([1, 2, 3, 4, 5, 6, 7, 8], lambda x: x % 3 == 0) -->  [3, 6]
    
    list_filter([1, 3, 2, 4, 0, 3, 6, -1, 8], lambda x: x >= 3) -->   [3, 4, 3, 6, 8]
    
    list_filter(
        ["ciaos", "pools", "nones", "mashed", "braes", "trip", "harry", "kooked", "mavens", "arrow"], 
        lambda word: "o" in word
    ) --> ['ciaos', 'pools', 'nones', 'kooked', 'arrow']


#### 2.  Lengths of runs of same elements in a list   

Prerequisites
 - List unpacking, e.g. `fst, *rest = list` and the like
 - Joining lists with `+`
 - List indexing, e.g. `lst[start:]` or `lst[:end]`
 - `enumerate()` (optional)


The problem

Write a function `count_runs(lst)`, which would take a list of elements (restricted for a purpose of this problem to types which 
can be compared with `==` operator, e.g. numbers, strings, etc.), and return a list of lengths of consecutive runs of the same elements in a list.

The implementation should use recursion, loops are not allowed. Performance is not a consideration at this point.

Examples of use:

    count_runs([1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 4, 5, 5]) --> [2, 3, 1, 5, 2]
