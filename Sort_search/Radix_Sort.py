#!/usr/bin/env python
# encoding: utf-8

"""

@author: Jessie

@email: jessie.JNing@gmail.com
"""

import math
def radix_sort(a, radix=10):

    K = int(math.ceil(math.log(max(a), radix))) # 用K位数可表示任意整数
    bucket = [[] for i in range(radix)] # 不能用 [[]]*radix
    for i in range(1, K+1): # K次循环
        for val in a:
            bucket[val%(radix**i)/(radix**(i-1))].append(val) # 析取整数第K位数字 （从低到高）
        del a[:]
        for each in bucket:
            a.extend(each) # 桶合并
        bucket = [[] for i in range(radix)]
    return a

if __name__ == "__main__":
    unsorted = [54,26,93,17,77,31,44,55,20]
    print "heap_sort:" , radix_sort(unsorted)


