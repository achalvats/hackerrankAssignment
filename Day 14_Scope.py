class Difference:
    def __init__(self, a):
        self.__elements = a

    # Add your code here
    difference = []
    maximumDifference = 0

    def computeDifference(self):
        for i in range(len(self.__elements)):
            for element in self.__elements:
                self.difference.append(abs(self.__elements[i]-element))
                self.maximumDifference = max(self.difference)




# End of Difference class
_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
