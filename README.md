# fresas_con_yogur
Para esta tarea he creado un repositorio en GitHubcon el siguiente link:

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

Una que nos permita contar el número de conversiones de cada tipo (call o form)

Una que nos permita saber cuál ha sido el coche más buscado 

Una que nos permita calcular el porcentaje dde ususarios recurrentes y otra que nos lo muestre en una gráfica de sectores

El código de nuestra tarea es el siguiente, aquí aparece más detallado el funcionamiento del mismo:

```



