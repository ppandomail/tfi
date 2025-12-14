# 3. Ciencia de Datos

## Introducción

* La **ciencia de datos** se ha consolidado como un campo interdisciplinario que combina estadística, informática y conocimiento del dominio para extraer valor de grandes volúmenes de información.
* Su relevancia radica en la capacidad de transformar datos en conocimiento accionable, apoyando la toma de decisiones en ámbitos tan diversos como la salud, la educación, la economía y la accesibilidad digital (Provost & Fawcett, 2013).

## Proceso de Ciencia de Datos

El ciclo de vida de un proyecto de ciencia de datos se organiza en etapas iterativas que garantizan rigor metodológico, reproducibilidad y valor práctico. Una de las metodologías más reconocidas es CRISP-DM (Cross Industry Standard Process for Data Mining), que establece un marco sistemático para abordar problemas complejos (Chapman et al., 2000).

1. **Comprensión del negocio**:
    * Definir claramente el problema y los objetivos del proyecto.
    * Identificar las preguntas de investigación o necesidades de la organización.
    * Ejemplo: determinar si un sitio web cumple criterios de accesibilidad.
2. **Comprensión de los datos**:
    * Recolectar datos de diversas fuentes (bases de datos, APIs, archivos, web scraping).
    * Explorar su estructura, calidad y relevancia.
    * Detectar inconsistencias, valores faltantes y sesgos.
3. **Preparación de los datos**:
    * Limpieza: tratamiento de valores nulos, duplicados y errores.
    * Transformación: normalización, codificación de variables categóricas, reducción de dimensionalidad.
    * Integración: combinar múltiples fuentes en un dataset coherente.
    * Ejemplo: convertir etiquetas de accesibilidad en variables binarias (1 = accesible, 0 = no accesible).
4. **Modelado**:
    * Selección de algoritmos de machine learning adecuados (regresión logística, árboles de decisión, SVM, redes neuronales).
    * Entrenamiento del modelo con datos de entrenamiento.
    * Ajuste de hiperparámetros para optimizar el rendimiento.
5. **Evaluación**:
    * Validar el modelo con datos de prueba.
    * Medir desempeño con métricas específicas:
        * Accuracy: proporción de predicciones correctas.
        * Precision y Recall: equilibrio entre falsos positivos y falsos negativos.
        * F1-score: media armónica de precisión y recall.
        * ROC-AUC: capacidad de discriminación global.
    * Comparar modelos y seleccionar el más adecuado.
6. **Implementación**:
    * Desplegar el modelo en un entorno real (aplicación, API, dashboard).
    * Integrar con procesos de negocio o sistemas existentes.
    * Ejemplo: un sistema que evalúe automáticamente la accesibilidad de páginas web.
7. **Monitoreo y mantenimiento**:
    * Supervisar el rendimiento del modelo en producción.
    * Detectar degradación por cambios en los datos (concept drift).
    * Actualizar y reentrenar periódicamente para mantener la eficacia. 

![Proceso de Ciencia de Datos](../img/CRISP-DM.png)

| Etapa                    | Objetivo                     | Ejemplo aplicado                      |
| --                       | --                           | --                                    |
| Comprensión del negocio  | Definir problema y objetivos | Evaluar accesibilidad web             |
| Comprensión de los datos | Explorar fuentes y calidad	  | Dataset de páginas con etiquetas      |
| Preparación              | Limpiar y transformar        | Codificación binaria de accesibilidad |
| Modelado                 | Entrenar algoritmos          | Regresión logística, SVM              |
| Evaluación               | Medir desempeño              | Accuracy, F1-score                    |
| Implementación           | Desplegar modelo             | API de evaluación automática          |
| Monitoreo                | Mantener rendimiento         | Reentrenar con nuevos datos           |

## 1. Comprensión del negocio





## Conclusión

* La ciencia de datos ofrece un marco metodológico robusto para abordar problemas complejos mediante el análisis de datos. La clasificación binaria, como técnica de machine learning, constituye una herramienta fundamental para tareas de predicción y evaluación, incluyendo la automatización de procesos de accesibilidad web. Este capítulo establece las bases conceptuales que sustentan la propuesta de este trabajo final, integrando rigor estadístico, metodológico y tecnológico aprendido en la carrera de Especialización en Ciencia de Datos de la Universidad Nacional del Oeste.

## Bibliografía

* Chapman, P., et al. (2000). CRISP-DM 1.0: Step-by-step data mining guide. SPSS Inc.
* Provost, F., & Fawcett, T. (2013). Data Science for Business. O’Reilly Media.
* Hastie, T., Tibshirani, R., & Friedman, J. (2009). The Elements of Statistical Learning. Springer.
* Witten, I. H., Frank, E., & Hall, M. A. (2016). Data Mining: Practical Machine Learning Tools and Techniques. Morgan Kaufmann.



[Data Science: ¿Cómo trabajar la data para que aporte valor al negocio?](https://www.linkedin.com/pulse/data-science-c%C3%B3mo-trabajar-la-para-que-aporte-valor-al-gac-pabst/)
