# 2 Accesibilidad Web

## 2.1 Introducción

* La **accesibilidad web** se define como el conjunto de principios, pautas y técnicas que permiten que las personas con diversas discapacidades puedan percibir, comprender, navegar e interactuar con el contenido digital.
* Su relevancia trasciende lo técnico: se vincula con derechos humanos fundamentales, como el acceso a la información y la participación plena en la vida social y educativa (W3C, 2025). En este sentido, la accesibilidad constituye un requisito indispensable para la inclusión digital y la equidad educativa.

## 2.2 Principios de la Accesibilidad

* Las Pautas de Accesibilidad para el Contenido Web (WCAG), desarrolladas por el World Wide Web Consortium (W3C), establecen cuatro principios esenciales que constituyen la base de toda práctica accesible (Luján Mora, 2025):
  * **Perceptible**: la información debe presentarse de manera que pueda ser percibida por todos los usuarios, incluyendo alternativas textuales para imágenes y subtítulos para contenido multimedia.
  * **Operable**: los componentes de la interfaz deben ser utilizables mediante diferentes dispositivos y métodos de interacción, como la navegación por teclado.
  * **Comprensible**: el contenido debe ser claro y predecible, evitando ambigüedades y asegurando consistencia en la interfaz.
  * **Robusto**: el contenido debe ser interpretable por una amplia variedad de agentes de usuario, incluidas tecnologías asistivas como lectores de pantalla.

* Estos principios, conocidos por el acrónimo **POUR** (Perceivable, Operable, Understandable, Robust), constituyen el marco conceptual que guía el diseño inclusivo.

    | Principio    | Aplicación práctica                  | Beneficio                                                    |
    | --           | --                                   | --                                                           |
    | Perceptible  | Subtítulos en videos                 | Inclusión de personas sordas o con hipoacusia                |
    | Operable     | Navegación por teclado               | Acceso para usuarios con movilidad reducida                  |
    | Comprensible | Formularios con instrucciones claras | Reducción de errores en usuarios con dificultades cognitivas |
    | Robusto      | Uso de HTML semántico                | Compatibilidad con lectores de pantalla                      |

## 2.3 Evolución de las normativas

* Las versiones más recientes de las WCAG, 2.1 y 2.2, han ampliado el alcance de los criterios de conformidad para abordar nuevas necesidades de accesibilidad. La versión 2.1 incorporó pautas relacionadas con la interacción táctil y el uso en dispositivos móviles, mientras que la 2.2 introdujo mejoras en la usabilidad para personas con discapacidades cognitivas y usuarios con baja visión (Diseño Web Logroño, 2025). Estas actualizaciones reflejan la evolución constante de la web y la necesidad de responder a contextos tecnológicos cambiantes:

    | Versión  | Año  | Principales novedades                                                                                      |
    | --       | --   | --                                                                                                         |
    | WCAG 2.0 | 2008 | Introducción del marco POUR y criterios de conformidad A, AA, AAA.                                         |
    | WCAG 2.1 | 2018 | Inclusión de pautas para dispositivos móviles, interacción táctil y usuarios con baja visión.              |
    | WCAG 2.2 | 2023 | Mejora de la usabilidad para personas con discapacidades cognitivas y criterios adicionales de navegación. |

## 2.4 Niveles de Conformidad WCAG

Las WCAG establecen tres niveles de conformidad que permiten evaluar el grado de accesibilidad alcanzado por un sitio web:

| Nivel               | Descripción                                          | Ejemplo práctico |
| --                  | --                                                   | --               |
| **A (mínimo)**      | Requiere cumplir criterios básicos de accesibilidad. | Proveer texto alternativo en imágenes simples. |
| **AA (intermedio)** | Incluye criterios que impactan significativamente en la experiencia de usuarios con discapacidad. | Asegurar contraste mínimo de 4.5:1 en texto normal y 3:1 en texto grande. |
| **AAA (máximo)**    | Representa el nivel más alto de accesibilidad, recomendado para contextos educativos y gubernamentales. | Proveer interpretación en lengua de señas para contenido audiovisual. |

## 2.5 Conceptos Clave

Entre los elementos técnicos más relevantes se destacan:

* **Texto alternativo (alt text)**: descripciones que permiten a los lectores de pantalla transmitir el contenido visual.
* **Contraste de color**: niveles mínimos de contraste para garantizar la legibilidad (ej. ratio 4.5:1 para texto normal).
* **Estructura semántica del HTML**: uso correcto de etiquetas y roles que facilitan la interpretación por tecnologías asistivas.
* **Compatibilidad con dispositivos de apoyo**: asegurando que el contenido sea robusto frente a diferentes entornos tecnológicos.

## 2.6 Ejemplo de Texto Alternativo

* **Imagen sin alt text**: un lector de pantalla no transmite información, generando una barrera.
* **Imagen con alt text adecuado**: ```<img src="grafico.png" alt="Gráfico de barras que muestra el aumento del tráfico web en 2025">```.

* El texto alternativo debe ser descriptivo y contextual, no redundante.

## 2.7 Ejemplo de Contraste de Color

* El contraste es uno de los aspectos más evaluados en accesibilidad.
  * **Texto con contraste insuficiente (2.5:1)**: gris claro sobre fondo blanco.
  * **Texto accesible (≥ 4.5:1)**: negro sobre fondo blanco o azul oscuro sobre fondo claro.

* Este criterio asegura que personas con baja visión puedan leer el contenido sin dificultad.

## 2.8 Impacto Social y Académico

* La implementación de accesibilidad web no solo beneficia a personas con discapacidad, sino que mejora la experiencia de usuario en general. Además, contribuye a la reputación institucional y al cumplimiento de marcos legales nacionales e internacionales. En el ámbito académico, la accesibilidad se vincula con la equidad en el acceso al conocimiento y con la democratización de la educación digital.

## 2.9 Conclusiones

* La accesibilidad web es un campo interdisciplinario que combina aspectos técnicos, sociales y legales. Su comprensión resulta indispensable para fundamentar propuestas innovadoras, como la **automatización de la evaluación mediante técnicas de machine learning**, que constituye el núcleo de este trabajo final integrador. La integración de estos conceptos asegura que la investigación se apoye en un marco normativo sólido y en una visión ética de la tecnología.

## 2.10 Bibliografía

* W3C (2025). Sumario de WCAG 2. Web Accessibility Initiative (WAI). Disponible en: [https://www.w3.org/WAI/standards-guidelines/wcag/es](https://www.w3.org/WAI/standards-guidelines/wcag/es)
* Diseño Web Logroño (2025). Guías WCAG. Comparativa WCAG 2.1 vs 2.2 en español: claves para transformar la accesibilidad. Disponible en: [https://disenoweblogrono.net/guias-wcag/comparativa-wcag-2-1-vs-2-2-espanol-claves-transformar-accesibilidad/](https://disenoweblogrono.net/guias-wcag/comparativa-wcag-2-1-vs-2-2-espanol-claves-transformar-accesibilidad/)
* Luján Mora, S. (2025). Accesibilidad Web. Accesibilidad Web: Principios y pautas de WCAG 2.1. Disponible en: [https://accesibilidadweb.dlsi.ua.es/?menu=principios-2.1](https://accesibilidadweb.dlsi.ua.es/?menu=principios-2.1)
