'''Idea
Step 1 create a count of all character from pattern and a unique cnt variable for disticnt charaters
Step 2 read the given string and decrement the count as the character you read
if total count of character is zero decrement cnt variable signifying that we have read all the 
characters of pattern in the given string
if cnt ==0
measure the length of the string read and store if minimum
gradually move the left pointer while incrementing the character count in the string(the count mostly is negative
for the string not in pattern zero for the characters in pattern)
So if a charater from the left is removed that is in pattern then its count value is 1 therefore 
we increment cnt variable to say that we require that character and right pointer is incremented till
that character is found 
'''


def minWindow(s,p):
    mp= [0]*256
    for ch in p:
        mp[ord(ch)]+=1
    cnt = len({i for i in p})
    l,j,minlen=-1,0,999999
    for i,ch in enumerate(s):
        mp[ord(ch)] -=1
        if(mp[ord(ch)]==0): cnt-=1
        while cnt ==0 :
            ans = i-j+1
            if ans < minlen:
                minlen=ans
                l=j
            mp[ord(s[j])] +=1
            if mp[ord(s[j])] == 1 : cnt +=1
            j+=1
    if l==-1 : return ""
    return s[l:l+minlen]


print(minWindow("this is a test string","tist"))