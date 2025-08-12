def bubble_sort(lst):
    # Your code goes here
    start = 0
    end = len(lst)
    for index in range(len(lst)):
        i = 0 
        while i<len(lst)-1:
            start =i
            adjacent = start +1 
            if not lst[start]< lst[adjacent]:
                lst[start],lst[adjacent] = lst[adjacent],lst[start]
            i+=1
    return lst
result= bubble_sort([1,4,50,5,2,0])
print(result)