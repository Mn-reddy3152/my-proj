def findSum(n, k):  
   # Find the last multiple of N 
    val = (k // (n - 1)) * n; 
    rem = k % (n - 1); 
    # Find the K-th non-multiple of N 
    if (rem == 0): 
        val = val - 1; 
    else: 
        val = val + rem; 
   # Calculate the sum of 
    # all elements from 1 to val 
    sum = (val * (val + 1)) // 2; 
    # Calculate the sum of 
    # all multiples of N 
    # between 1 to val 
    x = k // (n - 1); 
sum_of_multiples = (x * (x + 1) * n) // 2; 
sum -= sum_of_multiples; 
return sum; 
# Driver code 
n = 7; k = 13; 
print(findSum(n, k))