#!/usr/bin/env python
# coding: utf-8

# ## Geometry Analysis Project

# In[13]:


import os
import numpy
import sys

# In[2]:


pwd


# In[33]:


file_location = sys.argv[1]
xyz_file = numpy.genfromtxt(fname=file_location, skip_header=2, dtype='unicode')
symbols = xyz_file[:,0]
coordinates = xyz_file[:,1:]
#print(symbols)
#print(coordinates)
coordinates = coordinates.astype(numpy.float)
num_atoms = len(symbols)
for num1 in range(0, num_atoms):
    for num2 in range(0, num_atoms):
        if num1>num2:
            x_distance = coordinates[num1,0]-coordinates[num2,0]
            y_distance = coordinates[num1,1]-coordinates[num2,1]
            z_distance = coordinates[num1,2]-coordinates[num2,2]
            distance_12= numpy.sqrt(x_distance**2 + y_distance**2 + z_distance**2)
            if distance_12<1.5:
                print(F'{symbols[num1]} to {symbols[num2]} : {distance_12:.3f}')


# In[44]:


def calculate_distance(coords1, coords2):
    """
    This function accepts coordinates of two atoms and calculates the distance between two atoms. AKA this function
    has two arguments, the coordinates of two atoms. It returns the distance between atoms.
    """
    x_distance = coords1[0] - coords2[0]
    y_distance = coords1[1] - coords2[1]
    z_distance = coords1[2] - coords2[2]
    distance_12= numpy.sqrt(x_distance**2 + y_distance**2 + z_distance**2)
    return distance_12


# In[ ]:





# ### def function_name(parameters):
# ###   ***code goes***
# ###   return value_to_return
# # Functions BRO!

# In[45]:


file_location = os.path.join('water.xyz')
xyz_file = numpy.genfromtxt(fname=file_location, skip_header=2, dtype='unicode')
symbols = xyz_file[:,0]
coordinates = xyz_file[:,1:]
#print(symbols)
#print(coordinates)
coordinates = coordinates.astype(numpy.float)
num_atoms = len(symbols)
for num1 in range(0, num_atoms):
    for num2 in range(0, num_atoms):
        if num1>num2:
            distance_12 = calculate_distance(coordinates[num1], coordinates[num2])
                print(F'{symbols[num1]} to {symbols[num2]} : {distance_12:.3f}')



# In[46]:


help(calculate_distance)


# In[52]:


def bond_check(distance,minimum,maximum):
    """
    Checks a distance to see if it's a bond.
    """
    if distance>minimum and distance<maximum:
        return True
    else:
        return False


# In[ ]:
