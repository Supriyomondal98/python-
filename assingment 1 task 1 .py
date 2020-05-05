#!/usr/bin/env python
# coding: utf-8

# In[38]:


l=range (20,50)
m=[]
for i in l:
    if (type (i/7)== int) and (type (i/5)== float):
        m.append(i)
        
print(m)


# In[41]:


l= range (2000,3201)
m=[]
for i in l:
    if (i%7==0) and (i%5>0):
        m.append(i)
print(m)


# In[40]:


a= str(input("insert last name: "))
print(a[::-1])


# In[48]:


a= int(input("your desired radius(in cm)="))
v=4/3*22/7*a*a*a
print("volume(in cm^3) =", v)


# In[49]:


a=12
v=4/3*22/7*a*a*a
print("volume=",v)


# In[ ]:





# In[ ]:





# In[ ]:




