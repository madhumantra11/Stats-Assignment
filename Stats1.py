#!/usr/bin/env python
# coding: utf-8

# Problem Statement 1:
# 
# You survey households in your area to find the average rent they are paying. Find the 
# standard deviation from the following data: 
#  
# $1550, $1700, $900, $850, $1000, $950. 
#  
#  

# In[1]:


import numpy as np
dataset = [1550,1700,900,850,1000,950]
np.std(dataset)


# Problem Statement 2: 
#  
# Find the variance for the following set of data representing trees in California (heights in feet): 
#  
# 3, 21, 98, 203, 17, 9 
#  
#  

# In[2]:


import numpy as np
dataset = [3,21,98,203,17,9]
np.var(dataset)


# Problem Statement 3: 
#  
# In a class on 100 students, 80 students passed in all subjects, 10 failed in one subject, 7 failed in two subjects and 3 failed in three subjects. Find the probability distribution of the variable for number of subjects a student from the given class has failed in. 
#  
#  

# Total students=100
# Students passed in all subjects = 80
# Therefore, Students failed in 0 subjects = 80
# failed in 1 subject = 10
# failed in 2 subject = 7
# failed in 3 subjects = 3
# 
# Probability of -
# Failing in 0 subjects = 80/100
# Failing in 1 subject = 10/100
# Failing in 2 subjects = 7/100
# Failing in 3 subjects = 3/100
# 
# Expected number of subjects a student has failed = 0(80/100) + 1(10/100) + 2(7/100) + 3(3/100)
#                                                  =(0+10+14+9)/100 = 33/100 = 0.33
