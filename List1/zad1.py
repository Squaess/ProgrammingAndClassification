#!/usr/bin/env python
# coding: utf-8

# # Introduction to Python Programming Language

# ### 1. Ask the user for a number. Check if the input is an integer. Depending on whether the number is odd or even, print out an appropriate message to the user.

# In[2]:


user_in = input('Please insert number: ')
try:
    parsed = int(user_in)
except ValueError:
    print(f"Value Error occured. Couldn't parse {user_in} to int")
else:
    if parsed % 2 == 0:
        print(f"'{parsed}' is an even number")
    else:
        print(f"'{parsed}' is an odd number")
finally:
    print("This will execute anyway!!")


# ### 2. enerate 20 integers in the range 10−99 at random and return their mean value and maximal value.

# In[2]:


import random


# In[3]:


# Without repetition
no_rep = random.sample(range(10,100),20)
with_rep = random.choices(range(10,100), k=20)
print(no_rep, with_rep, sep="\n")


# In[4]:


print(f"max(no_rep): {max(no_rep)}")
print(f"max(with_rep): {max(with_rep)}")


# In[5]:


print(sum(no_rep)/len(no_rep))
import numpy as np
print(np.mean(no_rep))


# ### 3. Write a function that computes cosine of the angle between two d-dimensional vectors
# 
# Formula to calculate $\cos$ of two vectors $\vec{v}$ and $\vec{d}$.
# 
# $ \cos(\theta) = \frac{\vec{v} * \vec{d} }{ ||\vec{v}|| * ||\vec{d}|| }$, where $\theta$ is an angle between thease two vectors.

# In[6]:


import math

def vec_length(a):
    """
    Args:
        a (list): Vector like list
    Returns:
        float: Length of the vector 'a'
    """
    return math.sqrt(sum(map(lambda x: x**2, a)))


# In[7]:


# test vec_length function
print(vec_length([12, 1, 3]))


# In[8]:


def primitive_cosine(a, b):
    """
    Args:
        a (list): First vector.
        b (list): Second vector.

    Returns:
        float: Cosine value between thease two vectors
    """
    assert len(a) == len(b), "Vectors should be the same dimension"
    
    # calculate dot product
    dot_prod = 0
    for x, y in zip(a, b):
        dot_prod += x*y
    
    #multiplication of vector length
    return dot_prod / (vec_length(a) * vec_length(b))
    


# In[9]:


print(primitive_cosine([1, 2, 3], [3, 2, 0]))


# In[10]:


import numpy as np

def cosine(a, b):
    """
    Args:
        a (list): First vector.
        b (list): Second vector.
    """
    assert len(a) == len(b), "Vectors should be the same dimension"
    
    a = np.array(a)
    b = np.array(b)
    
    return  np.dot(a,b) / (np.sqrt((a*a).sum()) * np.sqrt((b*b).sum()))


# In[11]:


print(cosine([1, 2, 3], [3, 2, 0]))


# In[12]:


# elementwise
np.array([1,2,3]) * np.array([3,2,1])


# ### 4. Write a function that for a given set of integers {a, . . . , b} and an integer c lists all integers greater than a and smaller than b that are divisible by c.

# In[4]:


def beetween_and_divisible(numbers, divisor):
    """ I assume that 'numbers'
        are in proper order, so if number[0] > number[-1]
        there will be no results
        
    Args:
        numbers (list): List of numbers
        divisor (int): Int number
    Return:
        (list): List of numbers that are between a nd b and are divisible by c
    """
    if len(numbers) < 2:
        raise IndexError("List of numbers should contain at least 2 elements.")
    
    a = numbers[0]
    b = numbers[-1]
    return list(filter(lambda x: a < x < b and x%divisor == 0, numbers))


# In[5]:


assert beetween_and_divisible(range(10), 2) == [2, 4, 6, 8]


# ### 5. Write a program that for two lists x and y (possibly of different sizes) returns a list of elements that are common between the lists.

# In[6]:


def common(x, y):
    """
    Args:
        x (list):
        y (list):
        
    Return:
        (list): List of common elements
    """
    x = list(set(x))
    y = list(set(y))
    return [i for i in x if i in y]

def common2(x, y):
    """ This function will also work 
        for dictionaries in list, 
        so unhasable objects
    Args:
        x (list):
        y (list):
        
    Return:
        (list): List of common elements
    """

    common = []
    for i in x:
        for j in y:
            if j in x and j not in common:
                common.append(j)
    return common


# In[7]:


print(common([4,4,4,4,5,"",12,102,-5, "str", "nie_str"], ["str", "ala", 4, -5]))
print(common([4,4,4,4,5,"",12,102,-5, "str", "nie_str"], ["str", "ala", {1: "Jeden"}, 4, -5]))


# In[8]:


print(common2([4,4,4,4,5,"",12,102,-5, {1: "Jeden"}, "str", "nie_str"], ["str", "ala", {1: "Jeden"}, 4, -5]))


# ### 6. Write a function that removes all a letters form a given string x . For example, for x = abracadabra we expect x = brcdbr.

# In[18]:


def removes(word):
    """
    Args:
        word (str): Given word
    Return:
        (str): 'word' without character 'a'
    """
    return list(filter(lambda a: a != 'a', word))


# In[19]:


removes("abracadabra")


# ### 7. Write a program that accepts a sentence and calculates the number of letters and digits. Hint: you can use functions isalpha() and isdigit().

# In[20]:


from collections import defaultdict

def sentence_statistics(sentence):
    """
    Args:
        sentence (str): Whole sentence in one string
    Return:
        (dict): Number of letters and digits combined into dic
    """
    
    statistic = defaultdict(int, {"letter": 0, "digit": 0})
    for c in sentence:
        if c.isalpha():
            statistic['letter'] += 1
            statistic[c] += 1
        elif c.isdigit():
            statistic['digit'] += 1
            statistic[c] += 1
            
    return statistic
    


# In[21]:


sentence_statistics("This is some long sentence with numbers 12 344556566")


# ### 8. Write a program that lists all subsets of the set {a, b, c, d}.

# In[9]:


def subsets(numbers):
    """
    Args:
        numbers (set): Set of the numbers
    """
    n = len(numbers)
    pattern = 2**n - 1
    while pattern >= 0:
        print("{", end=" ")
        bin_pattern = format(pattern, f"0{n}b")
        for take, number in zip(bin_pattern, numbers):
            if take == "1":
                print(number, end=", ")
        print("}")
        pattern = pattern - 1


# In[10]:


subsets(set([1,2,3,4]))


# ### 9. Write a program that returns the most frequent letter in a string.

# In[24]:


def frequent_letter(word):
    """
    Args:
        word (string): string
    Return:
        (string): Most frequent letter in word
    """
    c = defaultdict(int)
    for i in word:
        c[i.lower()] += 1
    
    return min(c, key=c.get)

def frequent_letter2(word):
    """
    Args:
        word (string): string
    Return:
        (string): Most frequent letter in word
    """
    c = defaultdict(int)
    for i in word:
        c[i] += 1
        
    minimal = min(c, key=c.get)
    
    
    return list(filter(lambda x: c[x] == c[minimal], c))


# In[25]:


print(frequent_letter("mala"))
print(frequent_letter2("mala"))


# ### 10. Convert a number represented as a sequence of decimal digits to the binary representation.

# In[11]:


def to_bin(number):
    """
    Args:
        number (int): Numbar that will be represented as binary
    Return:
        (string): Bionary representation of 'number'
    """
    # return bin(number)
    # return format(number, "b")
    binary = ""
    while number > 0:
        if number % 2:
            binary = "1" + binary
        else:
            binary = "0" + binary
        number = number >> 1
    return binary


# In[12]:


to_bin(7)


# In[ ]:




