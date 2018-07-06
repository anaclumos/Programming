# Thanos.py

###### Developed by Sunghyun Cho on May 27th, 2018.

### Problem

Thanos snapped his finger, after collecting all six Infinity stones.
Are you alive?

Everyone should have same result, whenever they input their name.

### Code

```python
def snap(name):
    result = 1
    for character in name.lower():
        result += ord(character)
    return result%2==1

while(True):
    print("")
    name = input("Input Full Legal Name: ")
    print(name, "survived." if snap(name) else "died.")
```
