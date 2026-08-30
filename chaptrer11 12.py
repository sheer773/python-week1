#chapter11
# Q1. 2D + 3D vector
class TwoDVector:
    def __init__(self, i, j):
        self.i = i
        self.j = j

class ThreeDVector(TwoDVector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k
    def show(self):
        print(f"{self.i}i + {self.j}j + {self.k}k")

v = ThreeDVector(1,2,3)
v.show()

# Q4. Complex (a+bi)
class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __add__(self, other):
        return Complex(self.a + other.a, self.b + other.b)
    def __str__(self):
        return f"{self.a} + {self.b}i"

c1 = Complex(1,2)
c2 = Complex(3,4)
print(c1 + c2)
#chapter12
# Q1. 3 files open try except
for i in range(1, 4):
    try:
        with open(f"file{i}.txt") as f:
            print(f.read())
    except FileNotFoundError:
        print(f"file{i}.txt ledu mawa")

# Q2. 3rd 5th 7th using enumerate
l = [10, 20, 30, 40, 50, 60, 70, 80]
for index, item in enumerate(l):
    if(index==2 or index==4 or index==6): # 3rd, 5th, 7th
        print(item)

# Q3. Table list comprehension
n = 5
table = [n*i for i in range(1, 11)]
print(table)

# Q4. a/b infinite if b=0
try:
    a = int(input("a: "))
    b = int(input("b: "))
    print(a/b)
except ZeroDivisionError:
    print("Infinite")