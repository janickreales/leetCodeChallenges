# https://leetcode.com/problems/longest-substring-without-repeating-characters/

def lengthOfLongestSubstring(s):
    lst = [c for c in s]

    lst_2 = []
    for i in range(len(lst)):

        sublst = []
        for j in range(i,len(lst)):
            if lst[j] in sublst:
                break
            sublst.append(lst[j])
        lst_2.append(sublst)
    
    lst_len = [len(sl) for sl in lst_2]

    try:
        max_len = max(lst_len)
        id_len = lst_len.index(max_len)

        str_out = "".join(lst_2[id_len])
    except:
        max_len = 0
        str_out = ""

    return f'Longest substring is "{str_out}" - with a lenght of {max_len}'

print(lengthOfLongestSubstring('abcabcbb'))
print(lengthOfLongestSubstring('bbbbb'))
print(lengthOfLongestSubstring('pwwkew'))
print(lengthOfLongestSubstring('jarstoauglsgjw'))
print(lengthOfLongestSubstring(''))


