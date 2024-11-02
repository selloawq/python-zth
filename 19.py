#Printing the Fibonacci Sequence
nterms = int(input("How many terms: "))

#first two terms
n1, n2 = 0, 1; count = 0

#Check if number of terms is valid
if nterms <= 0:
    print("Please enter a positive integer")
#if there's only one term, return n1
elif nterms == 1:
    print("Fibonacci sequence upto", nterms, ":")
    print(n1)
#generating the fib sequence
else:
    print("Fibonacci sequence:", end=" ")
    while count < nterms: ###<---- this is the condition for the while loop. As soon as 'count' has counted values > nterms, it terminates.
        print(n1, end=" ")
        nth = n1 + n2
        #update values
        n1 = n2
        n2 = nth
        count += 1
