
# bubble sort
from re import template
from string import Template


def sort(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j]>nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp


nums = [4,9,8,3,5]
sort(nums)

print(nums)


print("--------------------------------------------------------")
# insertion sort




l = [8,11,3,1,2,5,6,9]

def insertion_sort(l):
    for outer_index in range(1,len(l)):
        
        temp =  l[outer_index]
        inner_index = outer_index
        
        while inner_index > 0 and l[inner_index-1] > temp:
            l[inner_index] = l[inner_index-1]
            inner_index -= 1
            
        l[inner_index] = temp

        
insertion_sort(l)

print(l)


print("--------------------------------------------------------")
# merge sort - ref w3s

def mergeSort(nlist):
    print("Splitting ",nlist)
    if len(nlist)>1:
        mid = len(nlist)//2
        lefthalf = nlist[:mid]
        righthalf = nlist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)
        i=j=k=0       
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                nlist[k]=lefthalf[i]
                i=i+1
            else:
                nlist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            nlist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            nlist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",nlist)

nlist = [14,46,43,27,57,41,45,21,70]
mergeSort(nlist)
print(nlist)