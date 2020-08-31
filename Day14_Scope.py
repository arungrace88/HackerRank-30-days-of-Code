class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0
    # Add your code here
    def computeDifference(self):
        for r in range(0,len(self.__elements)-1):
          for c in range(r+1,len(self.__elements)):
            max = abs(self.__elements[r]-self.__elements[c])
            if max > self.maximumDifference: 
              self.maximumDifference = max
        
# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)