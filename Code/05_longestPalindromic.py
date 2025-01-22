# https://leetcode.com/problems/longest-palindromic-substring/

import time

# ORIGINAL CODE (mine)
def longestPalindrome(s):
    lst = [c for c in s]
    lst_2 = []

    if (lst==list(reversed(lst))):
        return s
   
    for i in range(len(lst)):
        sublst = [lst[i]]
        lst_2.append((list(lst[i]),1))

        for j in range(i+1,len(lst)):
            sublst.append(lst[j])
            val = (sublst==list(reversed(sublst)))

            if val:
                lst_2.append((list(sublst), len(sublst)))
                continue

    if len(lst_2) > 0:
        l1 = [l[1] for l in lst_2]
        id_len = l1.index(max(l1))
        output = ''.join(lst_2[id_len][0])
    else:
        output = ''

    return output


### CHAT GPT OPTIMIZATION OF THE PREVIOUS CODE
def longestPalindrome_gpt(s):
    if s == s[::-1]:
        return s
    
    n = len(s)
    max_len = 0
    start = 0

    for i in range(n):
        
        if i - max_len >= 1 and s[i - max_len - 1:i + 1] == s[i - max_len - 1:i + 1][::-1]:
            start = i - max_len - 1
            max_len += 2
            continue

        if i - max_len >= 0 and s[i - max_len:i + 1] == s[i - max_len:i + 1][::-1]:
            start = i - max_len
            max_len += 1

    return s[start:start + max_len]


s ="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
# print(longestPalindrome(s))
# s = "cbbd"
# print(longestPalindrome(s))
# s = "a"
# print(longestPalindrome(s))
# s = ""
# print(longestPalindrome(s))
# s = "ac"
# print(longestPalindrome(s))
# s = "ccc"
# print(longestPalindrome(s))
# s = "bananas"

t1 = time.time()
print(longestPalindrome(s))
print('Duración sin GPT: ', time.time()-t1)

t1 = time.time()
print(longestPalindrome_gpt(s))
print('Duración con GPT: ', time.time()-t1)

# https://leetcode.com/problems/longest-palindromic-substring/

# def longestPalindrome(s):
#     lst = [c for c in s]
#     lst_2 = []

#     if (lst==list(reversed(lst))):
#         return s
   
#     for i in range(len(lst)):
#         sublst = [lst[i]]
#         lst_2.append((list(lst[i]),1))

#         for j in range(i+1,len(lst)):
#             sublst.append(lst[j])
#             val = (sublst==list(reversed(sublst)))

#             if val:
#                 lst_2.append((list(sublst), len(sublst)))
#                 continue

#     if len(lst_2) > 0:
#         l1 = [l[1] for l in lst_2]
#         id_len = l1.index(max(l1))
#         output = ''.join(lst_2[id_len][0])
#     else:
#         output = ''

#     return output

### CHAT GPT OPTIMIZATION OF THE PREVIOUS CODE
# https://leetcode.com/problems/longest-palindromic-substring/

import time

# ORIGINAL CODE (mine)
def longestPalindrome(s):
    lst = [c for c in s]
    lst_2 = []

    if (lst==list(reversed(lst))):
        return s
   
    for i in range(len(lst)):
        sublst = [lst[i]]
        lst_2.append((list(lst[i]),1))

        for j in range(i+1,len(lst)):
            sublst.append(lst[j])
            val = (sublst==list(reversed(sublst)))

            if val:
                lst_2.append((list(sublst), len(sublst)))
                continue

    if len(lst_2) > 0:
        l1 = [l[1] for l in lst_2]
        id_len = l1.index(max(l1))
        output = ''.join(lst_2[id_len][0])
    else:
        output = ''

    return output


### CHAT GPT OPTIMIZATION OF THE PREVIOUS CODE
def longestPalindrome_gpt(s):
    if s == s[::-1]:
        return s
    
    n = len(s)
    max_len = 0
    start = 0

    for i in range(n):
        print(i, start, max_len,s[i - max_len:i + 1])

        
        if i - max_len >= 1 and s[i - max_len - 1:i + 1] == s[i - max_len - 1:i + 1][::-1]:
            start = i - max_len - 1
            max_len += 2
            continue

        if i - max_len >= 0 and s[i - max_len:i + 1] == s[i - max_len:i + 1][::-1]:
            start = i - max_len
            max_len += 1

    return s[start:start + max_len]


# s ="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
s ="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

# print(longestPalindrome(s))
# s = "cbbd"
# print(longestPalindrome(s))
# s = "a"
# print(longestPalindrome(s))
# s = ""
# print(longestPalindrome(s))
# s = "ac"
# print(longestPalindrome(s))
# s = "ccc"
# print(longestPalindrome(s))
s = "bananas"
print(longestPalindrome(s))

# ls_l = ['a','b','c','d']
# print(ls_l)
# print(ls_l[::-1])
# print(ls_l[0:1])

# s = "bananas"
t1 = time.time()
print(longestPalindrome(s))
print('Duración sin GPT: ', time.time()-t1)

t1 = time.time()
print(longestPalindrome_gpt(s))
print('Duración con GPT: ', time.time()-t1)
