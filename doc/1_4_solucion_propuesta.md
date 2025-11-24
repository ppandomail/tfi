# 1.4 Solución propuesta

Para abordar el problema de la accesibilidad web, se propone el desarrollo de un modelo de aprendizaje automático supervisado capaz de clasificar automáticamente páginas web según su nivel de accesibilidad.  

El modelo se entrenará utilizando un conjunto de métricas cuantificables extraídas directamente del código fuente de cada página, tales como la ausencia de texto alternativo en las imágenes, texto con bajo contraste de colores, formularios sin etiquetas asociadas, enlaces vacíos, botones sin texto y ausencia de declaración de idioma.  

La automatización de este proceso permitirá evaluar grandes volúmenes de páginas web de manera eficiente, identificar patrones comunes de inaccesibilidad y proporcionar retroalimentación útil para desarrolladores y diseñadores, contribuyendo así a la mejora continua de la inclusión digital.  

La manera que la solución resuelve el problema planteado será:

1. **Extracción automática de características**: Se implementará un sistema de scraping y análisis sintáctico que recorra el contenido de las páginas web y detecte elementos clave como:
     * Imágenes sin atributo alt
     * Texto con bajo contraste (medido por la relación de luminancia entre fondo y texto)
     * Formularios sin etiquetas asociadas (label)
     * Enlaces vacíos (\<a> sin contenido o sin href)
     * Botones sin texto o íconos descriptivos
     * Ausencia de declaración de idioma (\<html lang="...">)

2. **Construcción de dataset etiquetado**: Se recopilarán páginas web con distintos niveles de accesibilidad, evaluadas mediante una herramienta automática, para generar un conjunto de entrenamiento confiable.  

3. **Entrenamiento del modelo**: Se entrenará un algoritmo de clasificación (por ejemplo, Random Forest, SVM o redes neuronales) que aprenda a identificar patrones de accesibilidad a partir de las métricas extraídas.  

4. **Evaluación y validación**: Se medirá la precisión, recall y F1-score del modelo para asegurar su efectividad en la detección de problemas de accesibilidad.  

5. **Interfaz de uso**: Se desarrollará una interfaz sencilla donde el usuario pueda ingresar una URL y obtener un diagnóstico automático del nivel de accesibilidad de la página.  

Esta solución permitirá:

* Automatizar la detección de problemas de accesibilidad en sitios web.
* Facilitar la corrección de errores por parte de desarrolladores, permitiendo la integración en pipelines de desarrollo para alertar sobre proeblemas antes del despliegue.
* Promover la inclusión digital de personas con discapacidades.

Si bien el modelo propuesto representa un avance significativo en la automatización de la evaluación de accesibilidad web, es importante reconocer ciertas limitaciones inherentes a su diseño y alcance:

* **Calidad del dataset**: La precisión del modelo depende de la calidad y diversidad del conjunto de datos utilizado para entrenarlo. Si el dataset no incluye suficientes ejemplos de distintos tipos de sitios web y niveles de accesibilidad, el modelo puede generalizar mal.  

* **Limitaciones del scraping**: Algunas páginas web pueden tener contenido dinámico (JavaScript) que dificulta la extracción completa de elementos relevantes, lo que afecta la precisión del análisis.

* **Evolución de estándares**: Las pautas de accesibilidad (como WCAG) se actualizan con el tiempo. El modelo podría quedar obsoleto si no se adapta a nuevas versiones o criterios emergentes.  

* **Falsos positivos/negativos**: El modelo puede identificar erróneamente elementos como problemáticos (por ejemplo, imágenes decorativas sin alt) o pasar por alto problemas reales si no están representados en las métricas.  

* **Limitaciones lingüísticas**: La detección de la ausencia de declaración de idioma puede no ser suficiente para evaluar la accesibilidad multilingüe o el contenido mal etiquetado dentro del documento.  

Estas limitaciones no invalidan la utilidad del modelo, pero sí señalan la necesidad de complementar su uso con herramientas de evaluación más profundas y con revisión humana en contextos críticos.
