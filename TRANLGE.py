NUM = int(input("Input a number: "))

def centered_triangle(n):
    for i in range(1,n+1):
        print(" "*(n-i) + "*"*(2*i-1) + " "*(n-i))

centered_triangle(NUM)
