"""
Given an array output true if the eleemnt are either non decresing or non increasing 
"""
'''
if length <= 1 return true
else
bool is increasing
compare a[0] and a[1]
if equal return false
if a[1] > a[] isincreasing = true else false
if(is increasing) then traverse till last element and make sure everything is increaseing if not return true
'''

def monotonic(arr):
    if len(arr) <= 1:
        return True
    else:
        isincreasing=True
        if arr[1] < arr[0] :isincreasing= False
        elif arr[1] == arr[0]: return True

        if isincreasing:
            for i in range(1,len(arr)):
                if(arr[i] <= arr[i-1]): return True
            return False
        else:
            for i in range(1,len(arr)):
                if(arr[i] >= arr[i-1]): return True
            return False

print(monotonic([1,-2,-3,4,5,6]))