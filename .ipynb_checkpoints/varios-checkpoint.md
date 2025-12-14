# Varios

* TFI como integración de aprendizajes 
* Cohorte 2025
* Plazo 1 año
* TFI evaluado por un jurado
* No hay defensa
* OBJ acotado
* BD disponible
* Metodología: clasificación

# Validación cruzada. Funcionamiento

* **División de datos**: el dataset se divide en un número predeterminado de k particiones de tamaño similar
* **Iteraciones de entrenamiento y prueba**: El proceso se repite k veces. En cada iteración:
    * una partición se designa como conjunto de prueba
    * Las k-1 restantes se utilizan como conjunto de entrenamiento
* **Evaluación**: Cada iteración produce una métrica de rendimiento (por ejemplo, precisión). Al final de las k iteraciones, se promedian los resultados para obtener una estimación más fiable del rendimiento del modelo

# una de las manera de medir la probabilidad es el número de casos favorables / número de casos , se lo llama probabilidad frecuencial

# Exploración

* Fijarse:
    * valores faltantes
    * valores repetidos
    * variables que no aportan ninguna información
    * comparar para cada variabLE P-VALUE
    * si las clases no están balanceadas, usar stratify=y, que garantiza que en train y test las clases queden balanceadas
    * correlación de variables

# Tips:

* mirar los datos
* generar algoritmo de trabajo (en que orden pruebo y porque)
* resultados y comparo

# SIGNIFICANCIA

