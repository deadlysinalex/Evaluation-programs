Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def getSum(n):
...     
...     sum = 0
...     while (n != 0):
...        
...         sum = sum + (n % 10)
...         n = n//10
...        
...     return sum
... 
>>> getSum(1231)
7
