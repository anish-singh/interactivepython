'''
Created on Apr 9, 2016

@author: anishsingh1
'''

def bubblesort(nums):
    
    print len(nums)
    for i in range(len(nums)-1, -1, -1):
        for j in range(0,i+1):
            if(nums[j] > nums[i]):  nums[j], nums[i] = nums[i], nums[j]
    
    print nums
   

def mergesort(nums):
    
    if len(nums) == 1: return nums
    
    mid = len(nums)//2
    
    l = mergesort(nums[0:mid])
    r = mergesort(nums[mid:])
    
    
    i,j,k = 0,0,0
        
    while i< len(l) and j < len(r):
        
        if l[i] < r[j]: 
            nums[k] = l[i]
            i +=1
        else: 
            nums[k] = r[j]
            j+=1
        k+=1
        
    while i < len(l):
        nums[k] = l[i]
        i+=1
        k+=1
    
    while j < len(r):
        nums[k] = r[j]
        j+=1
        k+=1
        
        
    print nums
    return nums
    
    
def quicksort(nums):
    qshelp(nums,0,len(nums)-1)
    return nums
    
def qshelp(nums, first, last):
   
    if first >= last : return nums
     
    p = partition(nums, first, last)
    qshelp(nums, first, p-1)
    qshelp(nums,p+1, last)
    
    
def partition(nums, first, last):
    
    elem = nums[first]
    
    l, r = first+1, last
    
    while l <= r and nums[l] <=elem:
        l+=1
    while l <= r and nums[r] >=elem:
        r-=1
        
    if (r < l):
        nums[first], nums[r] = nums[r], nums[first]
    else:
        nums[l], nums[r] = nums[r], nums[l]
        
    return r
        
    
    

def main():
    bubblesort([3,2])
    #print mergesort([3,2,5,1])
    #print quicksort([3,2,5,1,0])
                
if __name__ == '__main__':
    main()