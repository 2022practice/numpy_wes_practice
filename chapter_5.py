# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.14.0
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %%
import numpy as np
import pandas as pd

# %%
from pandas import Series,DataFrame

# %%
obj = pd.Series([1,7,8,9])

# %%
obj2 = pd.Series([4,7,-5,3], index=['d','b','a','c']) #le podes dar el indice que quieras
obj2, obj2.index # es medio una mezcla entre zip y enumerate!

# %%
sdata = {'Ohio': 35000, 'Texas': 71000, 'Utah': 5000, 'Oregon': 16000}
obj3 = pd.Series(sdata)

# %%
# podes elegir el indice pasandole como parametro otro iterable, pero se 'perderian'
# las keys si lo que le pasas es un dict

# %%
obj3.name = 'population'
obj3.index.name = 'state'
obj3

# %%
# Data Frame

# %%
# hay distintas maneras de crear un data frame, pero la mas comun/utilizada
# es a partir de un diccionario que sus keys tienen como value
# una lista de misma longitud


# %%
data = {'state':['Ohio','Ohio','Ohio','Nevada','Nevada','Nevada'],
        'year':[2000,2001,2002,2001,2002,2003],
        'pop':[1.5,1.7,3.6,2.4,2.9,3.2]}
frame = pd.DataFrame(data)
frame.head(), frame.tail() # head = los primeros 5, tail = los ultimos 5

# %%
# aca podes hacer tipo sorted, ahorrandote la lambda
pd.DataFrame(data,columns=['year','state','pop'])

# %%
frame['debt'] = 16.5 # es como los dicts, si asignas uno que no estaba
# lo agrega, pero este como tiene que rellenar, le agrega a todos ese valor
frame, frame.to_numpy() # se puede pasar a numpy!!!

# %%
#----------------------------------

# %%
obj = pd.Series([4.5,7.2,-5.3,3.6], index= ['d','b','a','c'])

# %%
obj.reindex(['a','b','c','d','e'])

# %%
obj3 = pd.Series(['blue','purple','yellow'], index=[0,2,4])

# %%
obj3.reindex(np.arange(6), method='ffill')

# %%
frame = pd.DataFrame(np.arange(9).reshape((3,3)),
                     index=['a','c','d'],
                     columns=['Ohio','Texas','California'])

# %%
frame

# %%
frame2 = frame.reindex(index=['a','b','c','d'])

# %%
frame2

# %%
states = ['Texas','Utah','California']
frame.reindex(columns=states)

# %%
