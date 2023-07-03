# https://leetcode.com/problems/find-the-highest-altitude/

gain = [-5,1,5,0,-7]

def largestAltitude(gain):
    altidude = [0]
    for i in range(len(gain)):
        altidude.append(gain[i]+altidude[i])
    
    return f'The altitudes are: {altidude} \nMaxAltitude = {max(altidude)}\n'

gain = [-5,1,5,0,-7]
print(largestAltitude(gain))
gain = [-4,-3,-2,-1,4,3,2]
print(largestAltitude(gain))        