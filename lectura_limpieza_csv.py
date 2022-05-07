#1) Comenzamos importando pandas para poder leer nuestros archivos csv
#2) Nos damos cuenta de que en nuestros archivos csv los elementos de las filas vienen separados por puntos y cmas;
#por lo tanto es necesario indicar el separador (sep =";") para que sea posible la lectura de nuestro archivo csv.
import pandas as pd
df_conversiones= pd.read_csv(r"C:/Users/andre/OneDrive/Escritorio/Programación/fresas_con_yogur/conversiones (4).csv", sep = ";")
print (df_conversiones)

df_navegacion = pd.read_csv(r"C:/Users/andre/OneDrive/Escritorio/Programación/fresas_con_yogur/navegacion (4).csv", sep = ";")
print(df_navegacion)

#A continuación procederemos a extraer los datos necesarios de nuestras URL
