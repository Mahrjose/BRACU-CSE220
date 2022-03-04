# Introduction
## Types of Data Structures

* Arrays
* Linked Lists
* Queues
* Stacks

## Prerequisities
* Linear Arrays ( `List` in Python )
* Objects and Classes (Good grip on the OOP concepts)

# Arrays

## Linear Arrays

* What is Linear Arrays?
> An array is a collection of a fix number of items where all the items are of the same data type.

* Arrays consist of :

    * **Element** - Each item stored in an array is called an element.
    * **Index** - Each location of an element in an array has a numerical value, which is used to access its corresponding element.

Liner Array:

Elements | 50 | 60 | 70 | 80 | 90 | 100 |
| :---|---: | :---|---: | :---|---: | :---
Index | 0 | 1 | 2 | 3 | 4 | 5 | 

We can declare a liner array (in python a `list`),
```py
arr = [0, 1, 2, 3, 4, 5]
```
This way an adress is created in the memory where the array is stored. We can see the memory location in Python3 with the `id()` and `hex()` methods.

> `id()` -> prints the memroy adress of an object.  
> `hex()` -> converts the memory adress to hexadecimal representation.

```py
>> print(hex(id(arr)))
0x7f3bec064ec0
```
So, whenever we're typing `arr`, we're not actually referencing the array itself. We're referencing a variable that has the reference of the memory location where the array is stored. 

### Copying an array

### Something to remember :
* Although in python we can change the array / list size anytime, however, in other programming languages such as C++ or Java, the size is fixed from the get go. So, in this course for learning purposes we'll always fix the size of the arrays / list from the get go too. It'll help us understand thigs more easily. For example,

```py
>> arr = [0] * 10
>> print(arr)
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
```
This will create an array of length 10. The value `0` indicate that the value of that index is empty.

### Array Traversal
Array traversal is accessing the elements of an array one by one. (Basicly, `for loop`)

In python3,
```py
>> arr = [0,1,2,3,4,5]
>> for i in arr:
>>     print(i, end=" ")
0 1 2 3 4 5
```
### Reverse printing an Array
We have an array and we need to print it's values in reverse order.

```py
# with for loop
def print_array_reverse(arr):
   for i in range(len(arr) - 1, -1, -1):
       print(arr[i], end=" ")

# with while loop
def print_array_reverse(arr):
   i = len(arr) - 1
   while i >= 0:
       print(arr[i], end=" ")
       i -= 1

>> print_array_reverse([0,1,2,3,4,5])
5 4 3 2 1 0
```
### Resizing an Array

### Shifting an array Left
### Shifting an array Right
### Inserting an element into an Array
We have an array for example, `arr = [1 ,20 ,5 ,78 ,30 ,0]` (Here, `0` means empty value). We need to insert a value for example, `100` in the `2`<sup>nd</sup> index. So that the resulting array will looks like,
`arr = [1 ,20 ,200, 5, 78, 30]`

So, we can achieve this by,
* Shift all the values 1 index to right (we have some empty space to the right)
* After shifting all the values to the right, index `2` will be empty. Simply, insert the value into index `2`

![Gif](https://media.giphy.com/media/aJg1xxk4TR3Csvp9St/giphy.gif)

In python3,

```py
def insert(arr, index, value, size):
    if size == len(arr):
        print("No space in array!")
        return

    if index < 0 or index > size:
        print("Wrong Index!")
        return

    else:
        for i in range(size, index - 1, -1):
            arr[i] = arr[i - 1]

        arr[index] = value
        print(arr)

>> arr = [1, 20, 5, 78, 30, 0]
>> insert(arr, 2, 100, 5))
[1, 20, 100, 5, 78, 30]
```
### Removing an element from an array
### Rotating an array Left
### Rotating an array Right

## Circular Arrays:

* In Linear arrays the first value always start from the 0<sup>th</sup> index.