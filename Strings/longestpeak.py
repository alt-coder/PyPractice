"""Given an find a size of longest peak , a peak is a element
such that on its left and right all element are strictly decreasing
"""
"""
Idea
traverse through the from left to right and by keep a track of differnce as soon it get negative keep 
carry on noting till it get zero or positve """
# def longestpeak(arr):
#     l,r=0,1
#     peak = -1
#     n= len(arr)
#     while r < n:
#         count =0
#         b = False                             #didn't consider the case when slope is negative
#         #going up the hill
#         while r < n and arr[r] > arr[r-1]:
#             r+=1
#         #check if we reach a flat surface if so then restart the process
#         if r< n and  arr[r] - arr[r-1] == 0 : l=r 
#         # making sure r is atleast greater by 2
#         if r-l >= 2:
#             #move down the hill
#             while r < n and arr[r] < arr[r-1] :
#                 r+=1
#                 b=True                #require this variable to make sure we move down the hill
#             if r-l+1 > peak and b:
#                 peak = (r-l)
#                 if r<n and arr[r] == arr[r-1] : l=r
#                 else: l = r-1
#         r+=1
#     return peak if peak >=3 else 0

def longestpeak(arr):
    l,r,endpt=0,0,0
    peak = 0
    n= len(arr)
    while r < n-1:
        # ignore the number till the slope is negative or zero
        while(r < n-1 and arr[r+1] <= arr[r]):
            r+=1
            l=r
            endpt=l
        #up the hill
        while r < n-1 and arr[r+1] > arr[r]:
            r+=1
        # down the hill
        while r < n-1 and arr[r+1] < arr[r]:
            r+=1
            endpt =r # update if journey is downhill
        if (endpt-l)+1 > peak : peak = (endpt-l)+1
        #ignore the number if the slope is zero in after uphill or downhill
        if r < n-1 and arr[r+1] == arr[r]: 
            l=r+1
            endpt =l
            r=l
            continue
        l=r
        endpt=l
    return 0 if peak < 3 else peak
            
        
        

def longestMountain(arr) -> int:
    res = 0
    curMT = 0
    slope = 0
    for i in range(len(arr)-1):
        if arr[i] < arr[i+1]:
            if slope == 1:
                curMT +=1       #as slope is posive keep on add
            else:
                curMT = 2       #we have taken first up step
            slope = 1
        elif arr[i] > arr[i+1]:
            if curMT > 1:       #current height >1 meaning we were clibing mountain
                curMT += 1      #therefore keep on incrementing
                res = max(res, curMT)
            slope = -1          #slope is negative now
        else:
            curMT = 0
            slope = 0
    return res


arr = [2,1,4,7,3,2,5]
a2 = [9,8,7,6,5,4,3,2,1,0]
print(longestpeak(arr))
print(longestpeak(a2))

