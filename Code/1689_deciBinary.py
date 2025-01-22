# https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/

def minPartitions(n):
    deci_n = max([c for c in n])
    return deci_n


n = "32"
print(minPartitions(n))
n = "82734"
print(minPartitions(n))
n = "27346209830709182346"
print(minPartitions(n))



