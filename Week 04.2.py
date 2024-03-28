class MySet:
    def __init__(self):
        self.elements = []

    def add(self, x):
        if x not in self.elements:
            if len(self.elements) == 0 or x < self.elements[0]:
                self.elements.insert(0, x)
            elif x > self.elements[-1]:
                self.elements.append(x)
            else:
                for i in range(len(self.elements) - 1):
                    if self.elements[i] < x < self.elements[i + 1]:
                        self.elements.insert(i + 1, x)
                        break

    def remove(self, x):
        if x in self.elements:
            self.elements.remove(x)

    def contains(self, x):
        return x in self.elements

# you should use that the array is already sorted. please, rewrite a code without using ready operations as "remove" etc. you should go through the array using the loop
