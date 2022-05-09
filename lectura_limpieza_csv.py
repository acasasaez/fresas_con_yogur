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

print (df_conversiones)
print(df_navegacion)

#Pasamos a la fase 1.2, ahora debemos obtener la siguiente información a partir de nuestra URL (camp: campaña; adg:adgroup; adv:advertisement; sl:sielink)
#Para eso comenzamos importando urllib 

#a continuación elaboraremos las funciones que nos permitan obtener dicha información a partir de las url 
def obtener_camp(): 
    campos =[]
    for i in df_navegacion["url_landing"]:
        url = i 
        url = url.split("&")
        campos.append(url[3])
    return campos
campos = obtener_camp()
print(campos)