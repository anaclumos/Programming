# Microsoft180501.py

###### Developed by Sunghyun Cho on May 1st, 2018.

### Problem

##### Microsoft University Student Interview Question from Mailprogramming.com

Find the median of the array everytime when new integer is added.

### Code

```python
def insertionSort(array):
    for x in range(len(array)):
        tmp = array[x]
        std = x-1
        while std >=0 and array[std] > tmp:
            array[std+1] = array[std];
            std -= 1
        array[std+1] = tmp;

def getMedianOf(array):
    size = int(len(array))
    if size%2==1:
        return array[int(size/2)]
    return (array[int(size/2)-1]+array[int(size/2)])/2


array = []
while(True):
    print("")
    i = int(input("input : "))
    array.append(i)
    insertionSort(array)
    print(array)
    print("output:",getMedianOf(array))
    print("")
```
