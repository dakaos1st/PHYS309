#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
from scipy import constants

plt.rcParams.update({"font.size":16, "axes.labelsize":16, "font.family":"sans-serif", 
                     "font.sans-serif":"Arial"})


# Recall that in PHYS 207, you were often asked to plot displacement as a function of time. For example, for a baseball thrown directly upward you would plot $y(t)$, and for a block on a horizontal spring you would plot $x(t)$. Here we will examine how the displacement and time axes "scissor together" at relativistic speeds.
# 
# Imagine that frame $K^{\prime}$ is moving in the $+x$ direction at speed $v$ relative to frame $K$. You are at rest in frame $K$. Let's figure out how the set of $(t^{\prime},x^{\prime})$ axes would look to you when the frames' origins $O$ and $O^{\prime}$ coincide.
# 
# <ol>
#     <li>Use the fact that $x^{\prime} = 0$ on the $t^{\prime}$ axis to define a line $x(t)$ in frame $K$ that follows the $t^{\prime}$ axis. Write a function that computes points on the line. $v$ will be one of your function inputs.</li>
# </ol>

# In[7]:


def t_prime_axis(t, v):
    x = v * t
    return t, x


# <ol start=2>
#     <li>Use the fact that $t^{\prime} = 0$ on the $x^{\prime}$ axis to define a line $x(t)$ that traces the $x^{\prime}$ axis in frame $K$. Write a second function that computes points on this line.</li>
# </ol>

# In[8]:


def x_prime_axis(x, v):
    gamma = 1 / np.sqrt(1 - (v**2))
    t = x / (v * gamma)
    return t, x


# <ol start=3>
#     <li>The code below creates a figure with centered $(ct,x)$ axes that have range $(-10^{10}, 10^{10})$. We are using $ct$ instead of just $t$ on our horizontal axis so that both axes have the same units. Use your functions from problems 1 and 2 to overplot the $t^{\prime}$ and $x^{\prime}$ axes <strong>as a function of $ct$</strong> for $v = 0.2c$. Make your $t^{\prime}$ and $x^{\prime}$ axes red, and label them in red.</li>
# </ol>

# In[12]:


c = 3e8  
v = 0.2*c

def t_prime_axis(t, v):
    x = v*t  
    return t, x

def x_prime_axis(t, v):
    gamma = 1/np.sqrt(1-(v/c)**2) 
    x = gamma*c*t  
    return t, x

# Set up plot
times = np.linspace(-100, 100, 201)  

fig, ax = plt.subplots(figsize=(7,7))

# Plot t' and x' axes
ax.plot(c*times, t_prime_axis(times, v)[1], color='red')    
ax.plot(c*times, x_prime_axis(times, v)[1], color='red')

# Format axes
ax.spines['left'].set_position(('data', 0))
ax.spines['bottom'].set_position(('data', 0)) 
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.set_aspect('equal')
ax.set_xlim([-1e10, 1e10])
ax.set_ylim([-1e10, 1e10])  

# Labels
ax.text(8e9, 0, r'$t^\prime$ Axis', color='red')
ax.text(0, 8e9, r'$x^\prime$ Axis', color='red')


# <ol start=4>
#     <li>Make a figure that plots $t^{\prime}$ and $x^{\prime}$ axes for $v = 0.25c$, $v = 0.5c$, and $v = 0.75c$. Use different colors for each pair of axes. Make a legend that shows which value of $v$ corresponds to each color.</li>
# </ol>

# In[13]:


c = 3e8
times = np.linspace(-100, 100, 201)  

fig, ax = plt.subplots(figsize=(8,8))

# v = 0.25c
v1 = 0.25*c  
ax.plot(c*times, t_prime_axis(times, v1)[1], color='blue')   
ax.plot(c*times, x_prime_axis(times, v1)[1], color='blue')

# v = 0.5c
v2 = 0.5*c
ax.plot(c*times, t_prime_axis(times, v2)[1], color='red')  
ax.plot(c*times, x_prime_axis(times, v2)[1], color='red')  

# v = 0.75c 
v3 = 0.75*c
ax.plot(c*times, t_prime_axis(times, v3)[1], color='green')
ax.plot(c*times, x_prime_axis(times, v3)[1], color='green')

# Format axes
ax.spines['left'].set_position(('data', 0)) 
ax.spines['bottom'].set_position(('data', 0))
ax.spines['right'].set_visible(False) 
ax.spines['top'].set_visible(False)
ax.set_aspect('equal')
ax.set_xlim([-1e10, 1e10])
ax.set_ylim([-1e10, 1e10])

# Legend
ax.legend(['v = 0.25c', 'v = 0.5c', 'v = 0.75c'])


# <ol start=5>
#     <li>Connect your graph from problem 4 with the discussion of world lines in Chapter 2 of your textbook. What kind of world line do your $(t^{\prime}, x^{\prime})$ axes approach as $v \rightarrow c$? Create a similar plot to problem 4, but this time plot $(t^{\prime}, x^{\prime})$ axes for $v = 0.5, 0.75, 0.875, 0.9375$. To illustrate the concept of taking a limit as $v \rightarrow c$, make each set of $(t^{\prime}, x^{\prime})$ axes a successively darker shade of gray. Plot the limiting world line in black. Add a legend to show which value of $v$ corresponds to which shade of gray. You may find it helpful to specify line colors like this: <tt>color='0.7'</tt>.</li>
# </ol>

# In[16]:


c = 3e8  
times = np.linspace(-100, 100, 201)  

fig, ax = plt.subplots(figsize=(8,8))

# v = 0.5c 
v1 = 0.5*c
ax.plot(c*times, t_prime_axis(times, v1)[1], color='0.9')
ax.plot(c*times, x_prime_axis(times, v1)[1], color='0.9')

# v = 0.75c
v2 = 0.75*c 
ax.plot(c*times, t_prime_axis(times, v2)[1], color='0.7')
ax.plot(c*times, x_prime_axis(times, v2)[1], color='0.7')

# v = 0.875c
v3 = 0.875*c
ax.plot(c*times, t_prime_axis(times, v3)[1], color='0.5') 
ax.plot(c*times, x_prime_axis(times, v3)[1], color='0.5')

# v = 0.9375c
v4 = 0.9375*c
ax.plot(c*times, t_prime_axis(times, v4)[1], color='0.25')  
ax.plot(c*times, x_prime_axis(times, v4)[1], color='0.25') 

# Light-like worldline limit 
ax.plot(c*times, c*times, color='black', linewidth=3)  

# Format axes
ax.legend(['v = 0.5c', 'v = 0.75c', 'v = 0.875c', 'v = 0.9375c', 'Light speed'],
          fontsize=12)  

ax.set_aspect('equal')
ax.spines['left'].set_position(('data', 0))  
ax.spines['bottom'].set_position(('data', 0))
ax.set_xlim([-1.5e10, 1.5e10]); ax.set_ylim([-1.5e10, 1.5e10])


# In[ ]:




