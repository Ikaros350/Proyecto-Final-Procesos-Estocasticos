# Proyecto-Final-Procesos-Estocasticos
Aquí se va a reposar toda la información del proyecto final, cada línea de código y los datos que sean necesarios

# Como conectar a la base de datos
Para conectar con la base de datos deben incluir estas lineas:

```python
sys.path.append("..") #Necesario para poder importar basedatos
import bd #Importa el script bd.py
```
luego pueden usar:
bd.insertarDatos(100,100)
valor = bd.traerValor()
