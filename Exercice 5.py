#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Question 1")
MV1=input("Entrez la valeur de la masse volumique de la partie inférieur en gramme pae mètre cube")
MV2=input("Entrez la valeur de la masse volumique de la partie supérieur en gramme pae mètre cube")
try:
    MV=13.6
    MV1=float(MV1)
    MV2=float(MV2)
    min=(MV1-MV)//(MV-MV2)
    print("La valeur minimale du rapport h2/h1 est:",min,)
except:
    print("La valeur des masses volumique n'est pas correct")
print("Question 2")
import numpy as np
coeff=[1,-2.4,-3.62]
sol=np.roots(coeff)
print(sol[0].real)
print("la valeur maximal du rapport h2/h1 est:",max,)


# In[2]:


print("Question 1")
MV1=input("Entrez la valeur de la masse volumique de la partie inférieur en gramme pae mètre cube")
MV2=input("Entrez la valeur de la masse volumique de la partie supérieur en gramme pae mètre cube")
try:
    MV=1000
    MV1=float(MV1)
    MV2=float(MV2)
    min=(MV1-MV)//(MV-MV2)
    print("La valeur minimale du rapport h2/h1 est:",min,)
except:
    print("La valeur des masses volumique n'est pas correct")
print("Question 2")
import numpy as np
coeff=[1,-2.4,-3.62]
sol=np.roots(coeff)
print(sol[0].real)
print("la valeur maximal du rapport h2/h1 est:",max,)


# In[ ]:




