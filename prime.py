#to check if a number is prime number

n = int(input("Enter the number:"))

def check_prime(n):
    for i in range(2,int(n/2)+1):
        if n%i == 0:
            return False
        else:
            continue
    return True

print(check_prime(n))

