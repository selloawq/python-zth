#Program to display fibonacci sequence using recursion

def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = int(input("Enter the number of terms (greater than 0): "))

#Check if number of terms is valid
if nterms <= 0:
    print("Please input a positive integer")
else:
    print("Fibonacci sequence: ")
    for i in range(nterms):
        print(recur_fibo(i), end=" ")