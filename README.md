# fresas_con_yogur
Para esta tarea he creado un repositorio en GitHubcon el siguiente link:https://github.com/acasasaez/fresas_con_yogur.git

El examen final es una tarea en la que se nos pide hacer un estudio sobre la venta de coches. 

Para esto inicialmente se nos aportan 2 archivos csv. Uno sobre la navegación, en el que se encuentran  los datos de navegación (donde tenemos como dato principal de las páginas web de ventas de coche); y el de conversión, donde se nos dan datos sobre cómo algubos usuarios actúan tras visitar la página web. 

finalmente se nos realizan las siguientes preguntas:

Visitas que recibe el cliente al día 

Cuantas convierten y cuántas no

Porcentaje de usuarios recurrente

Coche más visitado

Para poder llevar a cabo la práctica es fundamental comenzar haciendo un estudio profundo sobre los datos de navegación.

Las URL los aportarán toda la información que necesitaremos para hacer el ejercicio, y aunque algunas de las columnas del dataset de navegación parecen aportar datols de utilidad, estos son incorrectos. 

Por esta razón, lo primerco que tendremos que hacer será quedarnos solo con aquellas columnas del dataset que cuenten con Url landing, para esto emplearfemos la función dropna de pandas. 

Ahora crearemos la función que nos permita la columna de URL landing y trozear la misma, extrayendo de la misma los datos que nos aporta y elaborando un nuevo csv que recoja dichos datos. 

A continuación, lipiaremos este nuevo csv quedándonos solo con aquellas filas que no cuenten con usuarios ni gclids repetidos. Obtenemos nuestro csv final.

El siguiente paso será comparar los datos de navegación con los de conversión, buscamos aquellos ususarios que coincidan en ambos csv en id user o gclid.

A mayores para poder responder a las preguntas relizaremos algunas funciones más: 

Una que nos permita contar el número de conversiones de cada tipo (call o form) y además esta función nos devolverá un gráfico de sectores donde se refleje el procentaje de conversiones FROM frente a CALL

Una que nos permita saber cuál ha sido el coche más buscado 

Una que nos permita calcular el porcentaje dde ususarios recurrentes y otra que nos lo muestre en una gráfica de sectores

El código de nuestra tarea es el siguiente, aquí aparece más detallado el funcionamiento del mismo:

```
#1) Comenzamos importando pandas para poder leer nuestros archivos csv
#2) Nos damos cuenta de que en nuestros archivos csv los elementos de las filas vienen separados por puntos y cmas;
#por lo tanto es necesario indicar el separador (sep =";") para que sea posible la lectura de nuestro archivo csv.
from http.client import CannotSendRequest
from lib2to3.pgen2 import driver
from pyexpat.errors import codes
from urllib.parse import urlparse
import pandas as pd
import re
import csv
import matplotlib.pyplot as plt
df_conversiones= pd.read_csv(r"C:/Users/andre/OneDrive/Escritorio/Programación/fresas_con_yogur/conversiones (4).csv", sep = ";")


df_navegacion = pd.read_csv(r"C:/Users/andre/OneDrive/Escritorio/Programación/fresas_con_yogur/navegacion (4).csv", sep = ";")
#3) Creamos una función para modificar nuestro dataset navegacion para sustituir los "None" por espacios en blanco 
def limpiar(dato =[]): #Para esta función se puede pasar por parámetro una variable o si no tomará el valor de una lista vacía
    for i in range (len(dato)): #recorremos la lista pasada por parámetro, i toma los valores desde 0 hasta el valor del número de elemetos de nuestra lista
        if dato[i] == "None": # si el elemento en posición i toma el valor de "None"
             dato [i]= " "
        #ese elemento se sustituye por un espacio en blanco 
    # finalmente nuestra función nos devuelve la lista con espacios en blanco en las posiciones donde antes teníamos el str "None"
limpiar (df_conversiones["id_user"]) #aplicamos la función sobre la columna de los id users del dataset conversiones
limpiar (df_conversiones["gclid"])# y sobre la columna de gclid, que son las que nos interesan 
#a continuación limpairemos el dataset, para esto emplearemos el método dropna de pandas, que nos permitirá eliminar aquellas filas que cuenten con algún valor nulo


new_df = pd.DataFrame(df_conversiones) #con los datos modificados de navegación creamos un Dataframe 
new_df.to_csv("nuevo_conversor_final.csv")#que guardaremos en el nuevo csv "nuevo_conversor_final"
df_nuevo_conversor_final = pd.read_csv (r"nuevo_conversor_final.csv") #con panda creamos una variable que nos permita trabajar con este nuevo dataset
nuevo_conversor = df_nuevo_conversor_final.dropna()
#print (df_conversiones)
#print(df_navegacion)

#4)Por otro lado nos encargamos de limpar el dataset de navegación, para eso nos desharemos de aquellas filas que cuenten con elementos vacíos 
df_navegacion1 = df_navegacion.dropna()
#5) Ahora queremos extraer todos los datos que nos aportan  las URL de nuestro dataset
def separar_URL (URL): #Para esto creamos una función paqra separar las URL, a la que le pasaremos por parámetro la lista de URLs
#Empezamos creando las listas que rellenaremos con los datos de interés que extraeremos de nuestras URL
    gclid =[]
    camp = []
    uuid =[]
    idUser =[]
    adg = []
    device =[]
    adv = []
    sl = []
#A continuación extraemos los datos y para esto: 
    #1. Recorremos la lista de URLs 
    #2. Indicamos los separadores entre los que se encuentra nuestro datos de interés
    #3. Si esto no es posible porque nuestra URL no aporta información sobre este dato entonces se añade un 0 a la lista de datos 
#Con esto, obtendremos las listas que recojan los datos de gclid, campañaa, uuid, id User, adgroup, device, advertisement y site link
    #Valor del gclid
    for url in URL:
        try:
            esp = str(url).split("gclid=") 
            bueno = esp[1].split("&")
            gclid.append(bueno[0])
        except:
            gclid.append(0)
    #Valor del id campaña
    for url in URL:
        try:
            esp = str(url).split("camp=")
            bueno = esp[1].split("&")
            camp.append(bueno[0])
        except:
            camp.append(0)
    #Valor del uuid
    for url in URL:
        try:
            esp = str(url).split("uuid=")
            bueno = esp[1].split("&")
            uuid.append(bueno[0])
        except:
            uuid.append(0)
    #Valor del id del adgroup
    for url in URL:
        try:
            esp = str(url).split("adg=")
            bueno = esp[1].split("&")
            adg.append(bueno[0])
        except:
            adg.append(0)
    #valor del adv
    for url in URL:
        try:
            esp = str(url).split("adv=")
            bueno = esp[1].split("&")
            adv.append(bueno[0])
        except:
            adv.append(0)
    #valor del sl
    for url in URL:
        try:
            esp = str(url).split("sl=")
            bueno = esp[1].split("&")
            sl.append(bueno[0])
        except:
            sl.append(0)
    #Valor del id User 
    for url in URL:
        try:
            esp = str(url).split("idUser=")
            bueno = esp[1].split("&")
            idUser.append(bueno[0])
        except:
            idUser.append(0)
    #Valor     
    for url in URL:
        try:
            esp = str(url).split("device=")
            bueno = esp[1].split("&")
            device.append(bueno[0])
        except:
            device.append(0)
#Creamos un diccionario con los datos de interés
    datos = {"gclid": gclid,
    "camp": camp,
    "uuid": uuid,
    "adgroup": adg,
    "advertisement": adv,
    "sitelink": sl,
    "id_User": idUser,
    "device": device,
    "ts":df_navegacion1["ts"],
    "Url_landing":df_navegacion1["url_landing"]}
    new_df = pd.DataFrame(datos)
#Creamos un nuevo archivo csv que contenga todos estos datos 
    new_df.to_csv("New_Navegation.csv")
#Llevamos a cabo nuestra función sobre la columna de URLs de nuestro Dataset inicial, por lo tanto nuestro nuevo dataset contiene los datos extraídos de de las URLs
#del dataset que se nos aporta 
separar_URL(df_navegacion1["url_landing"])
#Volvemos a empleaer Pandas para leer nuestro nuevo dataset 
resultado = pd.read_csv(r"New_Navegation.csv")
#En este dataset eliminamos aquellos elementos que cuenten con id User repetido 
m =resultado.drop_duplicates(subset=["id_User"])
a = m.drop_duplicates ( subset = ["gclid"])
#print(m)
#Ordenamos los valores del detaset limpio en función del valor de ts 
a.sort_values ("ts", ascending= False)

#Volvemos a crear un archivo csv que recoja nuestro dataset final 
new_df = pd.DataFrame(a)
new_df.to_csv("navegacion_final.csv")
df_navegacion_final = pd.read_csv(r"navegacion_final.csv")

#Creamos una función que nos calcule el número de conversiones 
def conversiones (dat_1, dat_2): #Pasamos 2 listas que queremos comparar
    conversiones =[] #conversiones es una variable tipo list que toma el valor de lista vacía
    for i in dat_1: #´recorremos la primera lista e i toma el valor de los elementos de la primera lista
        if i in dat_2: #si un elemento de l a lista 1 está en la lista 2, entonces 
            conversiones.append(1) #ñla lista conversiones añade un uno
        else: #en caso contrario
            conversiones.append(0)#añadir 0
    return conversiones 
#print(conversiones(df_navegacion_final["id_User"], nuevo_conversor["id_user"] ))
#print(conversiones(df_navegacion_final["gclid"], nuevo_conversor["gclid"] ))
#comparamos las listas del dataset navegación final y el dataset nuevo conversor comparando las columnas que nos aportan los id user y los gclid
conversiones_por_iduser= conversiones(df_navegacion_final["id_User"], nuevo_conversor["id_user"])
conversiones_por_gclid = conversiones(df_navegacion_final["gclid"], nuevo_conversor["gclid"]
) 
#print(len(conversiones_por_iduser))
#print(len(conversiones_por_gclid))

#FUNCIÓN INÚTIL, es equivalente a len()
def contar(dato=[]):
    return len(dato)


#Creamos una función que nos permita obtener el valor del coche más vendido
def Onbtener_valor():
   #empezamos creando un diccionario donde añadimos los tipos de coche y el número de búsquedas
    cars = {
    
}
    for i in range(resultado.shape[0]):
        m = re.search("http(?:s?):\/(?:\/?)www\.metropolis\.com\/es\/(.+?)\/.*", str(resultado._get_value(i, "Url_landing")))
        if m != None:
            if m.groups()[0] in cars:
                cars[m.groups()[0]] += 1
            else:
                cars[m.groups()[0]] = 1
            

 #lista_valores es un elemento tipo list, inicialmente una lista vacía 
  # creamos un bucle que nos devuelve los valores del diccionario y los añade a nuestra lista de valores
    lista_valores =[]
    for i in cars.values ():
        lista_valores.append(i)
    #lista_keys es un elemento tipo list, inicalmente una lista vacía 
    #a partir de un vucle for recorrem os los elementos de las keys del diccionario añadiéndolos a nuestra lista de keys
    lista_keys =[]
    for i in cars.keys():
        lista_keys.append(i)
    #obtenemos el número mayor de nuestra lista de valores
    mayor_num_visitas = max(lista_valores)
    #recorremos nuestra lista de valores y cuando i tome el valor máximo buscamos el valor de la lista de llaves que se encuentre en la misma posicioón
    #finalemente la función devuelve este valor, el coche más buscado
    for i in range (len(lista_valores)): 
        if mayor_num_visitas == lista_valores[i]:
            return lista_keys[i]

#Ahora creamos una función que rcuente el número de conversiones de cada tipo
def obtener_conversiones(): 
    #añadimos 2 variables qde vaor int y 0 
    #Una terminará tomando el valor de número de conversiones tipo call y la otra del tipo form
    convierte_FORM =0 
    convierte_CALL =0
    #Recorremos la lista del archivo conversiones donde se nos muestra el tipo de conversión de cada caso
    #i toma el valor "CALL" o "FORM"
    for i in df_conversiones["lead_type"]: 
        if i == "CALL": #si toma el valor call entonces la variable donde contamos el número de conversiones de este tipo suma una unidad de valor
            convierte_CALL +=1
        elif i == "FORM": # en caso contrario, la variable donde contamos el número de conversiones de tipo form suma una unidad de valor
            convierte_FORM +=1
        #Imprimimos el total de conversiones de cada tipo
    print("El número total de conversiones tipo call es", convierte_CALL)
    print("El número total de conversiones tipo form es", convierte_FORM)

#Cálculo numérico del porcentaje de usuarios recurentes
def usuarios_recurrentes(Usuarios_repetidos, usuarios_sin_repetir):
   return usuarios_sin_repetir*100//Usuarios_repetidos

#Cálculo gráfico del porcentaje de ususarios recurrentes
def grafica_sectores (usuarios_repetidos,usuarios_sin_repetir):
  
  valores = [usuarios_repetidos,usuarios_sin_repetir]
  nombres =["Usuarios Repetidos","Usuarios sin repetir"]
  colores = ["#55CBCD","#FFDAC1"]
  plt.pie(valores, labels=nombres, autopct="%0.1f %%", colors=colores)
  plt.savefig('diagrama-sectores.png')
  plt.show()
#Imprimimos las respuestas a las preguntas
print("RESPUESTAS")
print(" ")
print("Inicialmente se nos ofrece un dataset con", contar(df_navegacion["id_user"]), "datos")
print("Tras limpiar el dataset, eliminando aquellas filas en las que no se aportaba una URL, obtenemos un total de",contar(df_navegacion1["id_user"]), "usuarios")
print("Finalmente, tras modificar nuestros dataset y elminar aquellos usuarios repetidos obtenemos", contar(df_navegacion_final["id_User"]), "datos")
print(" ")
print("Como el número de visitas que recibe una URL es independiente a si esta es visitada por la misma persona o no, concluimos que el número total de visitas será de ",contar(df_navegacion1["url_landing"]))
print("")
print("El coche más buscado es", Onbtener_valor())
print(" ")
print(" Tras obtener la lista de 0 y 1 para comparar los usuarios y gclid coincidentes en los archivos conversiones y navegacion finalobtenemos:")
print(conversiones_por_iduser)
print(conversiones_por_gclid)
print("lo que nos indica que contamos con un 0% de converisones")
print("")
print("Si los usiuarios del dataset navegacion_final contaran con los usuarios del dataset de conversionesentonces obtendríamos lo siguiente:")
obtener_conversiones()
print("El número de usuarios recurrentes es de ", usuarios_recurrentes(contar(df_navegacion1["id_user"]),  contar(df_navegacion_final["id_User"])), "%")
grafica_sectores(contar(df_navegacion1["id_user"])-contar(df_navegacion_final["id_User"]),  contar(df_navegacion_final["id_User"]))


