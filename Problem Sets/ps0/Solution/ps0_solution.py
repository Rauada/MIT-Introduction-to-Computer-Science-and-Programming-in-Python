#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 15:10:26 2022

@author: rauada
"""

import numpy as np

# Ask user for number x.
x = int(input("Enter number x: "))

# Ask user for number y.
y = int(input("Enter number y: "))

# Raises x to the power of y.
print(f"x**y = {x**y}")

# Log (base 2) of x. 
print(f"log(x) = {int(np.log2(x))}")