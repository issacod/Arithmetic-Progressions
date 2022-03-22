# This program inputs a positive integer N and outputs a list, ap_list, of positive integer
# arithmetic progressions which sum to N.

import math

N = int(input('N = '))

ap_list = [[N]]

if N != 1:
    for n in range(2,N+1):
        q = N/n
        if n%2 == 0 and q.is_integer() and N%2 == 0:
            upper_k = math.floor((q-1)/(n-1))               # upper_k is determined by requiring first_num >= 1
            if upper_k >= 1:
                for k in range(1,upper_k + 1):
                    gap = int(2*k)
                    first_num = int(q-k*(n-1))
                    last_num = int(q+k*(n-1))               # last_num = first_num + gap*(n-1)
                    ap_list.append(list(range(first_num,last_num+1,gap)))
        elif n%2 == 0 and (2*q).is_integer():
            upper_k = math.floor((2*(q-1)+n-1)/(2*(n-1)))
            if upper_k >= 1:
                for k in range(1,upper_k + 1):
                    gap = int(2*k-1)
                    first_num = int(q-((2*k-1)*(n-1))/2)
                    last_num = int(q+((2*k-1)*(n-1))/2)
                    ap_list.append(list(range(first_num,last_num+1,gap)))
        elif n%2 == 1 and q.is_integer():
            upper_k = math.floor((2*q-1)/(n-1))
            if upper_k >= 1:
                for k in range(1,upper_k + 1):
                    gap = int(k)
                    first_num = int(q-(k*(n-1))/2)
                    last_num = int(q+(k*(n-1))/2)
                    ap_list.append(list(range(first_num,last_num+1,gap)))

print('ap_list = '+str(ap_list)+'\n')

print("Number of arithmetic progressions = "+str(len(ap_list))+'\n')
    
for index in range(len(ap_list)):
    print(str(ap_list[index]).replace(', ','+')[1:-1])