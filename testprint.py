#!/usr/bin/env python3
#外边一层循环控制行数
#i是行数
i=1
while i<=9:
     #里面一层循环控制每一行中的列数
     j=1
     while j<=i:
          mut =j*i
          print("%d*%d=%d"%(j,i,mut), end="  ")
          j+=1
     print("")
     i+=1