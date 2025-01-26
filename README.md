# Actividad Práctica: Implementación de un Búfer de Entrada

Funcionamiento:
Se implementó un búfer de entrada en Python para procesar una entrada con un tamaño fijo de búfer. El carácter eof se utilizó como centinela para indicar el final de los datos. El objetivo es extraer lexemas mientras se simula la lectura de datos desde un búfer.

Funciones: 
- cargar_buffer():Carga un segmento de entrada a partir de inicio. Si el segmento < al tamaño del buffer, se agrega eof
- procesar_buffer(): procesa la entrada y utiliza los punteros para manejar la recarga del búfer, lectura de datos y la extracción de lexemas. 


