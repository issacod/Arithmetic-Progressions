# This program inputs a positive integer M and outputs the total number of positive integer
# arithmetic progressions which sum to N for N ranging from 1 to M.

import math

M = int(input('M = '))

if M == 1:
    print('1: 1')
else:
    for N in range(1,M+1):
        count = 1
        for n in range(2,N+1):
            q = N/n
            if n%2 == 0 and q.is_integer() and N%2 == 0:
                upper_k = math.floor((q-1)/(n-1))           
                if upper_k >= 1:
                    count += upper_k
            elif n%2 == 0 and (2*q).is_integer():
                upper_k = math.floor((2*(q-1)+n-1)/(2*(n-1)))
                if upper_k >= 1:
                    count += upper_k
            elif n%2 == 1 and q.is_integer():
                upper_k = math.floor((2*q-1)/(n-1))
                if upper_k >= 1:
                    count += upper_k
        print(str(N)+': '+str(count))