
# coding: utf-8

# In[29]:


def is_prime(num_in):
    if num_in <= 1:
        return False
    else:
        bound=round(num_in**0.5)
        for num in range(2,bound+1):
            if num_in % num ==0:
                return False
        return True
    
def is_prime2(num_in):
    if num_in <= 1:
        return False
    if num_in%2 ==0:
        return True
    else:
        bound=round(num_in**0.5)
        bound=(bound-1)//2
        for num in range(1,bound+1):
            if num_in % (2*num+1) ==0:
                return False
        return True

import random
    
def is_prime3(n):
    """
    return True if num_in is probably prime by Miller-Rabin primary test.
    : param n : int (natural number)
    """
    NumTrial = 100 # Miller-Rabin法での試行回数、素数判定を誤る確率は4^(-NumTrial)
    
    if n <= 0: return False
    if n == 2: return True
    if n == 1 or n & 1 == 0: return False
    
    d = (n - 1) >> 1
    while d & 1 == 0:
        d >>= 1

    for k in range(NumTrial):
        a = random.randint(1, n - 1)
        t = d
        y = pow(a, t, n)

        while t != n - 1 and y != 1 and y != n - 1:
            y = (y * y) % n
            t <<= 1

        if y != n - 1 and t & 1 == 0:
            return False

    return True

