# The following iterative sequence is defined for the set of positive integers:
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. 
# Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers 
# finish at 1.

# Which starting number, under one million, produces the longest chain?
# NOTE: Once the chain starts the terms are allowed to go above one million.
import time

limit = 1000000


def longest_chain(n):
    t = time.time()
    longest_start = 0
    longest_chain = 0
    

    for i in range(n):
        chain_length = 0
        num = i

        while num > 1:

            if num%2==0: #if even
                num = num/2
                chain_length+=1
            else: #if odd
                num = (3*num)+1
                chain_length+=1

        if chain_length > longest_chain:
            longest_chain = chain_length
            longest_start = i
            
    tt = time.time() - t
    print(f"ran in {tt:.5f}s \n")
    return longest_start


print(f"{longest_chain(limit)}")
