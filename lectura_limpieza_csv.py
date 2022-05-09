#1) Comenzamos importando pandas para poder leer nuestros archivos csv
#2) Nos damos cuenta de que en nuestros archivos csv los elementos de las filas vienen separados por puntos y cmas;
#por lo tanto es necesario indicar el separador (sep =";") para que sea posible la lectura de nuestro archivo csv.
from lib2to3.pgen2 import driver
from urllib.parse import urlparse
import pandas as pd
import re
df_conversiones= pd.read_csv(r"C:/Users/andre/OneDrive/Escritorio/Programación/fresas_con_yogur/conversiones (4).csv", sep = ";")


df_navegacion = pd.read_csv(r"C:/Users/andre/OneDrive/Escritorio/Programación/fresas_con_yogur/navegacion (4).csv", sep = ";")


#a continuación limpairemos el dataset, para esto emplearemos el método dropna de pandas, que nos permitirá eliminar aquellas filas que cuenten con algún valor nulo
df_conversiones=df_conversiones.dropna()
df_navegacion = df_navegacion.dropna()

#print (df_conversiones)
#print(df_navegacion)

#Pasamos a la fase 1.2, ahora debemos obtener la siguiente información a partir de nuestra URL (camp: campaña; adg:adgroup; adv:advertisement; sl:sielink)


#a continuación elaboraremos las funciones que nos permitan obtener dicha información a partir de las url 
#En la primera función necesitamos extraer todas las url de nuestro dataset
def extraerURL (DataFramen_column =[]): #Nuestra función actuará sobre la columna del dataframe introducida 
    i=int(input("Itroduzca un número entero: ")) #damos un valor entero a i

    if i < len(DataFramen_column): #mientras i esté en el rango de la lista
        Url = DataFramen_column[i]
        return Url #nuestra función nos devuelve el elemento de la columna del dataframe en esta posición 
    else:
        print("Nuestro dataset no cuenta con elementos en dicha posición, por favor introduzca otro valor") #en caso contrario se da un mensaje que nos indica que estamos buscando una posición que no existe en nuestra lista 
        return extraerURL(DataFramen_column) #la función se repite hasta introducir un valor válido 

#extraccion_URL =extraerURL(df_navegacion["url_landing"])
#print(extraccion_URL)
