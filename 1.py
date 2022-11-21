class Base:
   def solve(self, n):
      sign = '-' if n<0 else ''
      n = abs(n)
      if n < 3:
         return str(n)
      s = ''
      while n != 0:
         s = str(n%3) + s
         n = n//3
      return sign+s
ob = Base()
k=int(input("enter a number:"))
print(ob.solve(k))
