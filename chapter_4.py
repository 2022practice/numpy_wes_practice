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
import matplotlib.pyplot as plt

# %%
from numpy.linalg import inv, qr

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
arr = np.array([1,2,3,4,5])
arr.dtype

# %%
float_arr = arr.astype(np.float64)
float_arr.dtype

# %%
arr.dtype

# %%
arr = np.array([3.4,5.2,7.9,12.1,56.2])

# %%
arr.astype(np.int32) # en mi criterio hacer esto es como pasar a cada uno de los
# numeros por la funcion int()

# %%
numeric_str = np.array(['1.25','2.4','3.6'],dtype=np.string_)

# %%
numeric_str, numeric_str.astype(float)

# %%
int_array = np.arange(10)
calibers = np.array([.22,.25,.47,.50,.89,.380], dtype=np.float64)

# %%
int_array.astype(calibers.dtype) #aca estoy 'convirtiendo' al int_array
# al tipo de calibers

# %%
#si los arrays son del mismo tamaño, las operaciones se aplican 1 a 1
# es decir, el elemento 1 del primer array con el elemento 1 del primer array


# %%
arr = np.array([[1.,2.,3.],[4.,5.,6.]])
arr

# %%
arr * arr, arr - arr

# %%
# al 'vectorizar', o sea ahorrarte escribir for loops
# cuando aplicas una operacion al array, se aplica a todos los elementos de ese array


# %%
1 / arr

# %%
# osea recorre uno por uno y le aplica la operacion y devuelve un array nuevo
# y si queres comparar cosas entre 2 arrays y son DEL MISMO TAMAÑO
# podes usando solo el operador!!!!
# esto se llama 'broadcasting'

# %%
arr2 = np.array([[0.,4.,1.],[7.,2.,12.]])

# %%
arr2 > arr

# %%
#--------------------------------------------------

# %%
arr = np.arange(10)

# %%
arr[5:8] = 12 # le podes asignar un mismo valor a una seleccion de 
# elementos en un array
# cualquier modificacion de este estilo, CAMBIA EN EL ARRAY ORIGINAL
# NO DEVUELVE UNO NUEVO!

# %%
arr2d = np.array([[1,2,3],[4,5,6],[7,8,9]])

# %%
arr3d = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])

# %%
old_values = arr3d[0].copy() # si especificamente los quiero copiar, tengo que usar copy

# %%
x = arr3d[1] # lo que no entiendo aca es que si yo guardo ese elemento
# como no uso copy se guarda posta el elemento original?


# %%
arr2d

# %%
arr2d[:2,1:]

# %%
np.matrix([[1,2,3],[4,5,6],[7,8,9]])[:2,1:]

# %%
# podes hacer sclicing por columnas y filas!!!

# %%
lower_d_slice = arr2d[1,:2]

# %%
lower_d_slice.shape

# %%
#------------------------

# %%
names = np.array(['cami','mat','poli','poli','cami','mat','cami'])

# %%
data = np.array([[4,7],[0,2],[-5,6],[0,0],[1,2],[-12,-4],[3,4]])

# %%
names, data

# %%
names == 'cami'

# %%
data[names == 'cami'] # a data le estoy pasando un arrays de booleans
# osea 'cuales si' y 'cuales no' tiene que devolver

# %%
data[names =='cami', 1:]

# %%
#-----------------------------------

# %%
arr = np.zeros((8,4))
arr

# %%
for i in range(8):
    arr[i] = i
arr

# %%
# arr[[arr[4]-arr[3],3,0,6]] me la crei! 
# pense que tambien se podia operar con las filas/columnas
# y luego devolverlas pero no :(

# %%
arr = np.arange(32).reshape((8,4))
#esto esta bueno si queres pasarle una matriz tipo en lista y que solo 
# te lo 'ubique'
arr[[1,5,7,2],[0,3,1,2]] # la primer lista son las filas y la segunda los elementos a sacar de esas filas


# %%
#---------------------------

# %%
sam = np.random.standard_normal(size=(4,4))
sam # random de python solo te da UNO

# %%
rng = np.random.default_rng(seed=12) # no entiendo qué hacen los valores que le doy como seed
data = rng.standard_normal((2,3))
data

# %%
#-------------------------

# %%
points = np.arange(-5,5,0.01)
xs, ys =  np.meshgrid(points,points)
z = np.sqrt(xs ** 2 + ys ** 2)

# %%
plt.imshow(z,cmap=plt.cm.Blues, extent=[-5,5,-5,5]), plt.colorbar(), plt.title('image plot of $\sqrt{x² + y²}$ for a grid of values')

# %%
#------------------

# %%
xar = np.array([1.1,1.2,1.3,1.4,1.5])
yar = np.array([2.1,2.2,2.3,2.4,2.5])
cond = np.array([True, False,True,True,False])

# %%
result = np.where(cond,xar,yar)
result

# %%
# para reemplazar todos los valores negativos de una matriz,en este caso, esta buenisimo esto


# %% tags=[]
arr = rng.standard_normal((4,4))
arr, arr >0, np.where(arr > 0, 2, -2)

# %%
#--------------------------

# %%
