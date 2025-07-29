# l = [["hell",30],["hi",25],["beta",50],["alpha",50]]

# l.sort(key=lambda x:x[1])
# print(l)


# def is_perfect_square(x):
#     s = 0
#     while s * s < x:
#         s += 1
#     return s * s == x

# def is_fibonacci(n):
#     # A number is Fibonacci if one of (5*n*n + 4) or (5*n*n - 4) is a perfect square
#     return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)

# # Input from user
# num = int(input("Enter a number: "))

# if is_fibonacci(num):
#     print(num, "is a Fibonacci number.")
# else:
#     print(num, "is NOT a Fibonacci number.")



# Output:

# Enter a number: 21
# 21 is a Fibonacci number.

# Enter a number: 22
# 22 is NOT a Fibonacci number.

keys = [1,2,3,4,5]
values = ["one","two","three","four","five"]
        
print(list(zip(keys,values)))
