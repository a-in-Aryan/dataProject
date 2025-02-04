#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np

def calculate(num):
    if len(input_list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    # Convert input list into 3x3 numpy array
    matrix = np.array(num).reshape(3, 3)
    
    # statistics
    calculations = {
        'mean': [matrix.mean(axis=0).tolist(), matrix.mean(axis=1).tolist(), matrix.mean().tolist()],
        'variance': [matrix.var(axis=0).tolist(), matrix.var(axis=1).tolist(), matrix.var().tolist()],
        'standard deviation': [matrix.std(axis=0).tolist(), matrix.std(axis=1).tolist(), matrix.std().tolist()],
        'max': [matrix.max(axis=0).tolist(), matrix.max(axis=1).tolist(), matrix.max().tolist()],
        'min': [matrix.min(axis=0).tolist(), matrix.min(axis=1).tolist(), matrix.min().tolist()],
        'sum': [matrix.sum(axis=0).tolist(), matrix.sum(axis=1).tolist(), matrix.sum().tolist()]
    }
    
    return calculations


num = list(map(int, input("Enter 9-digits separated by space").split()))

print(calculate(num))

