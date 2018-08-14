# D180813.py

###### Developed by Sunghyun Cho on August 13th, 2018.

### Problem

Given a 2D integer array, print all elements in a circular spiral shape starting from [0][0].

### Example

```
input: [[1, 2, 3],
        [8, 9, 4],
        [7, 6, 5]]
 
Output: 1, 2, 3, 4, 5, 6, 7, 8, 9
```

### Code

```python
def spiralify(twoDarray):

    # Check if the 2D array is intact.
    for row in twoDarray:
        if len(row) != len(twoDarray[0]):
            return "Error. 2D array is not rectangle form."

    # Spiral print
    answer = []
    rowlen = len(twoDarray)
    collen = len(twoDarray[0])

    colloc = 0
    rowloc = 0

    compass = 0
    # Tells the direction where to go.
    # 0 goes right, 1 goes down, 2 goes left, 3 goes up

    for x in range(collen * rowlen):

        answer.append(twoDarray[rowloc][colloc])
        twoDarray[rowloc][colloc] = None

        if compass == 0:
            if colloc == collen - 1 or twoDarray[rowloc][colloc+1] == None:
                compass = 1
                rowloc = rowloc + 1

            else:
                colloc = colloc + 1

        elif compass == 1:
            if rowloc == rowlen - 1 or twoDarray[rowloc+1][colloc] == None:
                compass = 2
                colloc = colloc - 1
            else:
                rowloc = rowloc + 1

        elif compass == 2:
            if colloc == 0 or twoDarray[rowloc][colloc-1] == None:
                compass = 3
                rowloc = rowloc - 1
            else:
                colloc = colloc - 1

        else:
            if rowloc == 0 or twoDarray[rowloc-1][colloc] == None:
                compass = 0
                colloc = colloc + 1
            else:
                rowloc = rowloc - 1

    return(answer)

userArray = [[  1,  2,  3,  4],
             [ 12, 13, 14,  5],
             [ 11, 16, 15,  6],
             [ 10,  9,  8,  7]]

print(spiralify(userArray))
```
