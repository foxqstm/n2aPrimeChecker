
# coding: utf-8

# In[9]:


import sys

def result_factorization(N,factors):
    """
    return True if non-trivial divisor of N is found
    :param N : int (natural number)
    :param factors : (list of factors of N, len(factors)=2)
    """
    if len(factors) !=2:
        print("len(factors) != 2")
        sys.exit()

    if N != factors[0] * factors[1]:
        print("factors[0]×factors[1] != N @print_factors in ModulesFactorization")
        sys.exit()

    if factors[0] ==1:
        print("自明な約数しか見つかりませんでした。")
        return False
    else:
        print("{0}={1}×{2}".format(N,factors[0],factors[1]))
        return True


# In[1]:


import sys
import math

def is_square(N):
    """
    return True if N is square number
    :param N : int (natural number)
    """
    if N < 0:
        print("N is negative number @is_square in ModulesFactorization.")
        sys.exit()

    sqrt_N=round(math.sqrt(N))
    if N == sqrt_N*sqrt_N:
        return True
    else:
        return False


# In[2]:


import sys
import math
import numpy as np

def GenerateCoprimes(N):
    """
    retruns list of numbers which is relatively prime to N
    :param N :int (Natural number)
    """
    if N <= 0:
        print("N <= 0 @GenerateCoprimes in ModulesFactorization")
        sys.exit()
        
    Coprimes = list() # Nまでの数と互いに素な数のリスト
    for num in range(1,N+1):
        if math.gcd(N,num) == 1:
            Coprimes.append(num)
    return Coprimes


# In[3]:


def FactorInList(N, List):
    """
    return factor of N in PrimeList if exists
    :param N: int (Natural number)
    :param List: list of int (Candidate of factors)
    """
    a = 1
    b = N  
    for num in List:
        if N % num == 0:
            a = num
            b = N//num
            break
        
    return [a, b]


# In[4]:


import sys

def PositiveInt(N_str):
    """
    return positive integer N for string N_str
    :param N_str: string 
    """
    try:
        N = int(N_str)
    except ValueError:
        print("整数を入力してください。")
        sys.exit()

    if N <= 0:
        print("0以下の整数です。1以上の自然数を入力してください。")
        sys.exit()

    return N

