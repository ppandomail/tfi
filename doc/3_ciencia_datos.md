# 3 Ciencia de Datos

## 3.1 Introducción

* La **ciencia de datos** se ha consolidado como un campo interdisciplinario que combina estadística, informática y conocimiento del dominio para extraer valor de grandes volúmenes de información.
* Su relevancia radica en la capacidad de transformar datos en conocimiento accionable, apoyando la toma de decisiones en ámbitos tan diversos como la salud, la educación, la economía y la accesibilidad digital (Provost & Fawcett, 2013).

## 3.2 Proceso de Ciencia de Datos

El ciclo de vida de un proyecto de ciencia de datos se organiza en etapas iterativas que garantizan rigor metodológico, reproducibilidad y valor práctico. Una de las metodologías más reconocidas es CRISP-DM (Cross Industry Standard Process for Data Mining), que establece un marco sistemático para abordar problemas complejos (Chapman et al., 2000).

1. **Comprensión del negocio**:
    * Definir claramente el problema y los objetivos del proyecto.
    * Identificar las preguntas de investigación o necesidades de la organización.
2. **Comprensión de los datos**:
    * Recolectar datos de diversas fuentes (bases de datos, APIs, archivos, web scraping).
    * Explorar su estructura, calidad y relevancia.
    * Detectar inconsistencias, valores faltantes y sesgos.
3. **Preparación de los datos**:
    * Limpieza: tratamiento de valores nulos, duplicados y errores.
    * Transformación: normalización, codificación de variables categóricas, reducción de dimensionalidad.
    * Integración: combinar múltiples fuentes en un dataset coherente.
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

## 3.2.1 Comprensión del negocio

* Este trabajo final de integrador tiene como objetivo general "Desarrollar un modelo de aprendizaje automático que clasifique páginas web según problemas de accesibilidad, para promover la inclusión digital y detectar  barreras que afectan a personas con discapacidad".
* La accesibilidad web garantiza que todos puedan acceder y utilizar el contenido digital por igual. Crea una experiencia en línea más justa e inclusiva, donde nadie queda excluido y todos pueden interactuar con la web con facilidad y confianza.
* Se seleccionaron los seis problemas de accesibilidad web más comunes en 2025, según los resultados del estudio WebAIM Million, que analiza un millón de páginas de inicio cada año (WebAIM, 2025):
    * Páginas a las que les falta el atributo de idioma  
    * Imágenes sin texto alternativo
    * Formularios sin etiquetas
    * Botones con etiquetas faltantes o poco claras
    * Enlaces con texto faltante o poco claro
    * Contraste de color insuficiente entre el texto y el fondo

### 3.2.1.1 Páginas a las que les falta el atributo de idioma

* El atributo de **lang** indica a los navegadores y lectores de pantalla en qué idioma está escrita la página.
* Cuando el atributo **lang** falta en el HTML, las tecnologías de asistencia deben "adivinar" el idioma. Esto suele provocar una pronunciación incorrecta y una lectura confusa.
* Ejemplo de una página HTML con un atributo **lang** correctamente definido (lang="en-US") en la etiqueta.

![Atributo lang](../img/lang.jpg)

* **A quién afecta**:
    * Usuarios de lectores de pantalla.
    * Personas que no hablan el idioma del sitio web.
    * Cualquiera que confíe en una pronunciación correcta o en herramientas de traducción.

* **Cómo corregir el atributo lang faltante**: establecer el idioma correcto en cada página para que los navegadores y lectores de pantalla sepan leer el contenido. Los desarrolladores deben agregar el atributo **lang** a la etqieta **<html>** en la página principal. Por ejemplo:

```html
<html lang="en">
```

* Si una página o sección usa un idioma diferente, se debe cambiar el valor del atributo **lang** para toda la página o se debe agregar un atributo **lang** a esa sección específica. Esto ayuda a las herramientas de asistencia a pronunciar las palabras correctamente y mejora la comprensión.

### 3.2.1.2 Imágenes sin texto alternativo

* El texto alternativo es una breve descripción que comunica el contenido de una imagen a los usuarios que no pueden verla. Sin texto alternativo, los lectores de pantalla solo anuncian el elemento como "imagen", sin ninguna descripción de lo que representa, lo que impide que los usuarios accedan a información importante.

* **A quién afecta**:
    * Usuarios ciegos.
    * Usuarios con baja visión que dependen de lectores de pantalla.
    * Personas en redes lentas o inestables cuando las imágenes no se cargan.

* **Cómo corregir el texto alternativo faltante**: asegurarse de que cada imagen significativa tenga un texto alternativo preciso. Se debe escribir un texto breve que describa el propósito de la imagen y agregarlo al atributo **alt** en el HTML. Por ejemplo:

```html
<img src="laptop-user.jpg" alt="Person typing on a laptop">
```

* Las imágenes decorativas deben usar un atributo alt vacío ( alt="") para que los lectores de pantalla las omitan. Para elementos visuales complejos, como gráficos o diagramas, se debe incluir un texto alternativo breve y proporcionar una explicación más extensa cerca o un enlace a una descripción larga y accesible.

### 3.2.1.3 Formularios sin etiquetas

* Una etiqueta conecta texto descriptivo (como "Correo electrónico" o "Contraseña") con su campo de entrada correspondiente en un formulario.
* Sin esta conexión, los lectores de pantalla no pueden indicar correctamente lo que el usuario debe escribir en el campo, lo que lo obliga a adivinar o abandonar el formulario.
* Ejemplo: un formulario que utiliza marcadores de posición en lugar de etiquetas visibles, lo que genera problemas de accesibilidad. Como puede ver, el texto del marcador de posición "Nombre" desaparece en cuanto el usuario empieza a escribir su nombre.

![Form sin etiquetas](../img/form.jpg)

* **A quién afecta**:
    * Usuarios de lectores de pantalla.
    * Usuarios navegando con entrada de voz.
    * Usuarios con desafíos cognitivos que necesitan una orientación clara.

* **Cómo corregir las etiquetas de formulario faltantes**: asegurarse de que cada campo de formulario tenga una etiqueta clara y vincule la etiqueta a su entrada mediante coincidencias atributos **for** y **id** para que las herramientas de asistencia puedan leerla correctamente. Por ejemplo:

```html
<label for="email">Email address</label> 
<input type="email" id="email" name="email">
```

* Se debe evitar confiar únicamente en el texto del marcador de posición, ya que los lectores de pantalla suelen ignorarlo y desaparece en cuanto el usuario empieza a escribir. Si el campo requiere información específica, como un formato o un ejemplo, agregue esas instrucciones en la etiqueta o cerca de ella para que todos los usuarios comprendan el requisito.

### 3.2.1.4 Botones con etiquetas faltantes o poco claras

* Los botones vacíos son botones que no tienen texto visible ni nombre accesible. Esto suele ocurrir cuando un botón solo usa un icono sin texto alternativo, lo que lo hace prácticamente vacío para los lectores de pantalla; simplemente lo anunciarán como "botón", lo cual no explica la acción. Aquí hay un ejemplo de un código vacío:

```html
<button></button>
```

* **A quién afecta**:
    * Usuarios de lectores de pantalla.
    * Usuarios del teclado.
    * Usuarios con dificultades motoras o cognitivas.
    * Todos los usuarios del sitio web.

* **Cómo arreglar botones vacíos**: los botones siempre deben indicar a los usuarios qué acción activan. Se debe usar etiquetas cortas y claras como "Buscar", "Enviar" o "Agregar al carrito" para que el propósito sea fácil de entender. Asegurarse de que esta etiqueta se incluya en el HTML para que las herramientas de asistencia puedan leerla. Por ejemplo:

```html
<button>Search</button>
```

### 3.2.1.5 Enlaces con texto faltante o poco claro

* Los enlaces vacíos son enlaces sin texto visible ni nombre accesible. Esto suele ocurrir cuando un enlace solo usa un icono sin texto alternativo significativo, o cuando el texto del enlace se omite accidentalmente. Sin etiqueta, los lectores de pantalla lo anuncian simplemente como "enlace". A continuación se muestra un ejemplo de un enlace vacío:

```html
<!-- This link has no visible text and no accessible name --> 
<a href="/pricing"> 
    <img src="pricing-icon.svg" alt=""> <!-- No meaningful alt text --> 
</a>
```

* **A quién afecta**:
    * Usuarios de lectores de pantalla.
    * Usuarios del teclado que navegan a través de enlaces.
    * Usuarios con desafíos cognitivos.

* **Cómo arreglar enlaces vacíos**: asegurarse de que cada enlace tenga texto visible o un nombre accesible para que los usuarios y los lectores de pantalla comprendan su propósito. Por ejemplo:

```html
<a href="/pricing">View pricing</a>
```

* Nota: Si el  enlace tiene texto, pero es impreciso (como "Haga clic aquí" o "Leer más"), se debe considerar reemplazarlo con un texto más claro como "Ver precios" o "Descargar informe".

### 3.2.1.6 Contraste de color insuficiente entre el texto y el fondo

* El contraste de color mide la diferencia de luminancia o brillo percibido entre dos colores.
* Un contraste de color insuficiente se produce cuando el texto no destaca lo suficiente del fondo, lo que dificulta su visibilidad y aún más su lectura. Un ejemplo común es el texto gris claro sobre un fondo blanco. Puede parecer limpio, pero crea un claro problema de contraste.
* Un ejemplo de una página con bajo contraste de color, lo que dificulta la lectura del texto:

![Bajo contraste de color](../img/contraste.jpg)

* **A quién afecta**:
    * Personas con baja visión.
    * Personas con daltonismo.
    * Adultos mayores con sensibilidad al contraste reducida.
    * Personas intentando leer contenido bajo la luz solar directa.

* **Cómo solucionar el contraste de color insuficiente**: su objetivo es cumplir con las relaciones de contraste WCAG: 4,5:1 para texto normal (cualquier tamaño inferior a 18 puntos o inferior a 14 puntos en negrita) y 3:1 para texto grande (es de 18 puntos o más o de 14 puntos o más en negrita). Se debe ajustar la paleta de colores para que todos los elementos clave cumplan con las relaciones de contraste requeridas, no solo el texto de fondo. Esto incluye enlaces, botones, indicadores de enfoque, iconos, bordes de campos de formulario y cualquier otro elemento visual que los usuarios necesiten ver con claridad.
* Se debe probar los colores con herramientas como el Verificador de Contraste de Color de WebAIM (https://webaim.org/resources/contrastchecker/). Si un par de colores falla, ajustar oscureciendo o aclarando el texto o el fondo, o eligiendo un color completamente diferente hasta que el contraste cumpla con los requisitos WCAG y el contenido sea legible.

## 3.2.2 Comprensión de los datos







## Conclusión

* La ciencia de datos ofrece un marco metodológico robusto para abordar problemas complejos mediante el análisis de datos. La clasificación binaria, como técnica de machine learning, constituye una herramienta fundamental para tareas de predicción y evaluación, incluyendo la automatización de procesos de accesibilidad web. Este capítulo establece las bases conceptuales que sustentan la propuesta de este trabajo final, integrando rigor estadístico, metodológico y tecnológico aprendido en la carrera de Especialización en Ciencia de Datos de la Universidad Nacional del Oeste.

## Bibliografía

* Chapman, P., et al. (2000). CRISP-DM 1.0: Step-by-step data mining guide. SPSS Inc.
* Provost, F., & Fawcett, T. (2013). Data Science for Business. O’Reilly Media.
* Hastie, T., Tibshirani, R., & Friedman, J. (2009). The Elements of Statistical Learning. Springer.
* Witten, I. H., Frank, E., & Hall, M. A. (2016). Data Mining: Practical Machine Learning Tools and Techniques. Morgan Kaufmann.



[Data Science: ¿Cómo trabajar la data para que aporte valor al negocio?](https://www.linkedin.com/pulse/data-science-c%C3%B3mo-trabajar-la-para-que-aporte-valor-al-gac-pabst/)
