#chapter7
n=10
for i in range(1,11):
    print(i)

n=10
for i in range(1,11):
     print(f"{n} x {i}={n*i}")

names=["sheer","she","run"]
for name in names:
     if(name.startswith("s")):
        print(f"hello {name}")

# table using while
n=5
i=1
while(i<=n):
    print(f"{n} x {i}={n*i}")
    i+=1
    
# Q4. Prime or not
num = 7
is_prime = True
for i in range(2, num):
    if(num % i == 0):
        is_prime = False
        break
print("Prime" if is_prime else "Not Prime")

# Q5. Sum of n naturals using while
n = 5
sum = 0
i = 1
while(i<=n):
    sum+=i
    i+=1
print(sum)

# Q6. Factorial using for
n = 5
fact = 1
for i in range(1, n+1):
    fact*=i
print(fact)

# Q10. Table reversed
n = 5
for i in range(10, 0, -1):
    print(f"{n} x {i} = {n*i}")


#chapter8
# Q1. Greatest of 3 using function
def greatest(a, b, c):
    if(a>b and a>c):
        return a
    elif(b>c):
        return b
    else:
        return c

print(greatest(10, 25, 7))

# Q2. C to F
def c_to_f(c):
    return (c * 9/5) + 32

print(c_to_f(0)) # 32F

# Q3. No newline print
print("Hello", end=" ")
print("Mawa") # Hello Mawa same line lo vastundi

# Q4. Recursive sum n
def sum_n(n):
    if(n==1):
        return 1
    return n + sum_n(n-1)

print(sum_n(5)) # 15

# Q5. Star pattern function
def pattern(n):
    for i in range(n):
        print("*" * (i+1))

pattern(3)