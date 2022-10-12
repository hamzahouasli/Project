#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Question 1")
H=input("Entrez la Hauteur de Barrage en metre:")
try:
    MVeau=1000
    g=9.80
    H=float(H)
    P=MVeau*g*H
    print("La pression en bas du barrage est:",P,)
except:
    print("La valeur d'hauteur n'est pas correct")
print("Question 2")
S=input("Entrez la surface du barrage en metre carré:")
try:
    S=float(S)
    F=S*P
    print("La force exercées sur la surface du barrage est",F,)
except:
    print("La valeur de surface n'est pas correct")
    
    


# In[ ]:




