# Semana 1
Este repositorio contiene las actividades realizadas en la Semana 1, enfocadas en hacer una prueba para saber nuestro nivel en cuanto a programación, manejo de estructuras, logica de programación y validación.  
## Proyectos realizados  

### 1. Programa 1: Análisis númerico (Fibonacci, Primos y Validar el número)  
Este programa evalúa un número entero n ingresado por el usuario.  
- **Clasificación de signo:** Determina si el número es positivo (n>0), negativo (n<0) o cero.
- **Validación si es primo:** Implementa un bucle while eficiente que busca divisores hasta la raíz cuadrada del número (divisor * divisor <= n).
- **Pertenencia a Fibonacci:** Genera la secuencia partiendo de los casos base [0,1] hasta alcanzar o superar el valor ingresado para verificar su existencia en la serie.

## 2. Programa 2: Gestión de notas académicas  
Un algoritmo diseñado para procesar una cadena de texto con nombres y calificaciones de estudiantes:  
- **Procesamiento del texto:** Utiliza .split para fragmentar los datos de entrada en una lista general de datos.
- **Estructura de datos:** Organiza la información en listas independientes (nombres y notas) mediante saltos de indice de 2 en 2.
- **Filtrado de resultados:** Valida y muestra únicamente a los estudiantes cuya nota es mayor o igual a 3.0.

## Estructura del repositorio Semana 1  
- **"Prueba 1_Semana 1.py":** Código python para el Programa 1.
- **"Prueba 2_Semana 1.py":** Código python para el Programa 2.
- **"Analisis y diagrama prueba 1.pdf":** Documentación del procedimiento y diagrama de flujo del Programa 1.
- **"Analisis y diagrama prueba 2.pdf":** Documentación del procedimiento y diagrama de flujo del Programa 2.
- **"D1-P1.png" y "D2-P2.png":** Diagramas de flujo de cada una de las pruebas.

## Tecnologias y conceptos aplicados  
- **Lenguaje:** Python (Uso de input, int, float, listas, bucles)
- **Lógica:** Implementación de condicionales anidados y estructuras de control.
- **Documentación:** Creación de diagramas de flujo para representar visualmente la solución.

--- 
# Semana 2
Este repositorio contiene las actividades realizadas durante la Semana 2, enfocadas en la profundización de algoritmos de gestión de datos, análisis de requerimientos y la organización estructurada de archivos en Python.  

## Proyectos realizados

### 1. Programa: Gestión Avanzada de Estudiantes (`Estudiantes_sem2.py`)
Un algoritmo desarrollado para automatizar el procesamiento de información académica, mejorando la lógica de captura y filtrado de datos.
- **Entrada dinámica:** Permite la carga y procesamiento de registros de estudiantes.
- **Manejo de colecciones:** Uso de estructuras de datos para organizar nombres y calificaciones.
- **Validación y lógica:** Implementación de filtros para determinar estados académicos basados en las notas obtenidas.

### 2. Documentación y Análisis Técnica
Se realizó un proceso de preventa y diseño lógico antes de la codificación, asegurando que la solución cumpla con los requisitos del taller.
- **Análisis de Diseño:** Documentación detallada sobre la arquitectura del código y la lógica aplicada para resolver los problemas planteados.
- **Taller Práctico:** Resolución de ejercicios de lógica de programación y estructuras de control.

## Estructura del repositorio Semana 2
- **`Semana-2/`**: Carpeta principal que contiene los entregables de este módulo.
- **`Estudiantes_sem2.py`**: Código fuente en Python para la gestión de datos académicos.
- **`Analisis_diseño.docx`**: Documento con el análisis lógico y estructural del proyecto.
- **`Taller_Semana 2.docx`**: Documento con la resolución de los ejercicios teóricos y prácticos propuestos.

## Tecnologías y conceptos aplicados
- **Lenguaje:** Python (Optimización de listas, manejo de cadenas y estructuras de control).
- **Documentación Técnica:** Redacción de análisis de requerimientos en formato profesional.
- **Gestión de Versiones:** Uso avanzado de Git (manejo de ramas o *branches*) para organizar el flujo de trabajo.
--- 
# Semana 3  
Enfocada en el paradigma **Dividir y Conquistar (D&C)** y análisis de complejidad mediante recurrencias.  
## Proyectos realizados  
### 1. Gestión de Estudiantes con D&C (`Estudiantes_D&G_Semana 3.py`)  
Reforma total del sistema de filtrado utilizando recursividad para mejorar la escalabilidad.  
- **Estrategia:** La función `filtrar_estudiantes_DyC` descompone la lista hasta el caso base (un estudiante).
- **Lógica:** Divide el rango mediante un punto medio (`mid`), resuelve las mitades y combina los resultados.
- **Análisis:** Aunque se mantiene una complejidad de $\Theta(n)$, la estructura prepara el código para procesamiento en paralelo.

### 2. Ejercicios de Aplicación (`Ejercicios- Semana 3.pdf`)
Resolución de problemas clásicos aplicando optimización:
- **Búsqueda Binaria:** Localización del menor número en arreglos con comportamiento unimodal (decremento/incremento).
- **Exponenciación Rápida:** Algoritmo recursivo para calcular $a^n$ en tiempo logarítmico $O(\log n)$.
- **Ordenamiento Mergesort:** Seguimiento paso a paso para ordenar alfabéticamente la cadena "ALGORITMO".
- **Conteo de Bits:** Uso de búsqueda binaria para identificar números faltantes basados en sumas de bits.

## Estructura del Repositorio - Semana 3
- **`Estudiantes_D&G_Semana 3.py`**: Código fuente con la implementación de la herramienta D&C.
- **`Diseño del problema de los estudiantes con D&C.pdf`**: Documentación técnica (Historias de usuario, diagramas de flujo recursivo, secuencia y casos de uso).
- **`Ejercicios- Semana 3.pdf`**: Análisis detallado y pseudocódigos de los problemas resueltos en clase.

## Tecnologías y Conceptos Aplicados
- **Paradigma de Diseño:** Dividir, Conquistar y Combinar.
- **Análisis Matemático:** Notación Big O, Teorema Maestro y Ecuaciones de Recurrencia $T(n) = 2T(n/2) + c$.
- **Modelado UML:** Diagramas de secuencia para representar la auto-llamada (recursión) y flujo de mensajes.

