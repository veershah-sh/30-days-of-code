class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumdifference = None

    def computeDifference(self):
        lengthElem = len(self.__elements)
        maximum = 0 
        for i in range(lengthElem):
            for j in range(lengthElem):
                value = abs(self.__elements[i] - self.__elements[j])
                if(maximum < value):
                    maximum = value
        self.maximumDifference = maximum
        

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)