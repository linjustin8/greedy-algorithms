
import random

def sequence_generator():
    n = int(input("Enter the number of requests: "))
    for i in range(n):
        print(f"{random.randint(1, 10)} ", end="")

if __name__ == "__main__":
    sequence_generator()
    