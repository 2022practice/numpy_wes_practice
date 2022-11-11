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

# %%
my_arr = np.arange(1_000_000)

# %%
my_list = list(range(1_000_000))

# %%
# %timeit my_arr2 = my_arr*2

# %%
# %timeit my_list2 = [ x * 2 for x in my_list ]

# %%
data = np.array([[1.5,-0.1,3],[0,-3,6.5]]) 
#le estoy pasando una lista de listas
# si o si, los elementos de la lista 'externa' tienen que ser del mismo tipo, en este
#caso, son listas

# %%
data

# %%
data.shape, data.dtype

# %%
#esta es buenisima, podes crear arrays del size que le pases
# sin tener que hacer list comprehension
np.zeros(3),np.ones(2),np.empty(5), np.arange(4)

# %%
np.identity(4), np.eye(4) # que diferencia hay????

# %%
