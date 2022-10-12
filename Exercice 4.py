#!/usr/bin/env python
# coding: utf-8

# In[1]:


P=input("Entrez la valeur de la pression en pascal:")
S=input("Entrez la valeur de la surface en metre carré")
try:
    P=float(P)
    S=float(S)
    F=P*S
    print("la force exercées est",F,)
except:
    print("la valeur de pression et/ou surface n'est pas correct" )


# In[ ]:




