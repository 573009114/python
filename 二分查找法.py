# -*- coding: utf8 -*-
def binary_search(a,b):
    min_v=0
    max_v=len(a)-1
    while (min_v<=max_v):
        avg=(min_v+max_v)/2
        if a[avg]>b:
            max_v=int(avg-1)
        elif a[avg]<b:
            min_v=int(avg+1)
        else:
            return avg

if __name__ == '__main__':
    a = [1, 5, 7, 8, 22, 54, 99, 123, 200, 222, 444]
    b=input('input number: ')
    print(binary_search(a,b))
