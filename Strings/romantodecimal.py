# Given a string in roman no format (s)  your task is to convert it to an integer . Various symbols and their values are given below.
# I 1
# V 5
# X 10
# L 50
# C 100
# D 500
# M 1000

# Example 1:

# Input:
# s = V
# Output: 5
# Example 2:

# Input:
# s = III 
# Output: 3

#IDEA
'''there are two cases here here
the ratio of current and previous charater < 1 : add case ex XI
the ratio of current and previous charater >1 and <10 : subtaction case ex IX
'''
def RomanToDecimal(roman):
    value=dict({'I':1},
    V = 5,
    X = 10,
    L = 50,
    C = 100,
    D = 500,
    M = 1000
    )
    rank=dict({'I':1},
    V = 2,
    X = 3,
    L = 4,
    C = 5,
    D = 6,
    M = 7
    )
    res=0
    for i,ch in enumerate(roman):
        if i == 0: res+=value[ch]
        else:
            if value[ch] / value[roman[i-1]] >1 and value[ch] / value[roman[i-1]] <= 10:
                res = res - value[roman[i-1]]
                toadd = value[ch]-value[roman[i-1]]
                res+=toadd
            elif value[ch] / value[roman[i-1]] <= 1:
                res = res  + value[ch]
            else: return -1
    return res


st = "CI"
print(RomanToDecimal(st))


