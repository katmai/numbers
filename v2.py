import math

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Read the values of p and q
while True:
    p = int(input("Enter a prime number for p: "))
    if is_prime(p):
        break
    print("Invalid input! p must be a prime number.")
    
while True:
    q = int(input("Enter a prime number for q: "))
    if is_prime(q):
        break
    print("Invalid input! q must be a prime number.")
    
# Calculate N
N = p * q
print("N = p * q =", N)

# Read the value of g
while True:
    g = int(input("Enter a prime number for g (less than N): "))
    if is_prime(g) and g < N:
        break
    print("Invalid input! g must be a prime number less than N.")
    
# Create the table
print("{:<5} {:<10} {:<20} {:<15}".format("x", "g^x", "(g^x)/N", "Remainder"))
print("-" * 50)

x = 1
while True:
    gx = g ** x
    quotient, remainder = divmod(gx, N)
    print("{:<5} {:<10} {:<20} {:<15}".format(x, gx, quotient, remainder))
    if remainder == 1:
        break
    x += 1
