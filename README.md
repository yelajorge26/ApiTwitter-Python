# ApiTwitter-Python
Extracción y limpieza de datos API Twitter - Python, Django, SQlite
## Ejecución
Con el fin de comprender la percepción de la ciudadanía ecuatoriana acerca de la atención médica en los hospitales del país y preparan un conjunto de datos que pueda ser utilizado para que, mediante algoritmos de aprendizaje automático, seamos capaces de primero comprender la verdadera situación y a partir de esto reforzar o tener en consideración determinadas acciones necesarias para hacerle frente de mejor manera a una situación sanitaria similar en el futuro, se construye una aplicación con Python, Django y SQlite, un aplicativo que permita extraer, limpiar y almacenar datos de la red social de Twitter mediante su API.
### 1. Criterios de busqueda
Los datos pueden ser extraídos mediante, la selección de un hospital disponible dentro de una lista desplegable, nombre de usuario (cuenta del hospital) y una búsqueda personalizada para extraer comentarios según frases clave.
![Busqueda por hospital](https://github.com/yelajorge26/ApiTwitter-Python/blob/main/img_ejecucion/hospital.png)
![Busqueda por nombre de usuario](https://github.com/yelajorge26/ApiTwitter-Python/blob/main/img_ejecucion/username.png)
![Busqueda personalizada](https://github.com/yelajorge26/ApiTwitter-Python/blob/main/img_ejecucion/personalizada.png)
### 2. Tweets obtenidos
Los tweets obtenidos son almacenados en una base de datos de sqlite, son mostradas en un listado y se permite al usuario eliminar aquellos que considere poco necesarios y descargar en formato csv la data obtenida.
![Listado datos obtenidos](https://github.com/yelajorge26/ApiTwitter-Python/blob/main/img_ejecucion/base_datos.png)
