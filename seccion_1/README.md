# Introducción al curso

- Módulo 1:
1. [Hola Python](modulo-01_01.md)
2. [Introducción a la programación](modulo-01_02.md)
3. [Introducción a Python](modulo-01_03.md)
4. [Hello World](modulo-01_04.md)
5. [Revisión del módulo](modulo-01_05.md)
- Módulo 2: Sintaxis Básica de Python
1. [Expresiones y variables](modulo-02_01.md)
2. [Funciones](modulo-02_02.md)
3. [Condicionales](modulo-02_03.md)
4. [Reseña de módulo](modulo-02_04.md)
- Módulo 3: Bucles
1. [While loops](modulo-03_01.md)
2. [For loops](modulo-03_02.md)
3. [Recursión (opcional)](modulo-03_03.md)
4. [Repaso de módulo](modulo-03_04.md)
- Módulo 4: Strings, Lists y Diccionarios
1. [Strings](modulo-04_01.md)
2. [List (listas)](modulo-04_02.md)
3. [Diccionarios](modulo-04_03.md)
4. [Programación orientada a objetos](modulo-04_04.md)
5. [Repaso del módulo](modulo-04_05.md)
- Módulo 5: Proyecto Final
1. [Proyecto final](modulo-05_01.md)
2. [Resumen del curso](modulo-05_02.md)
3. [Buscando un nuevo trabajo o un ascenso](modulo-05_03.md)

## Skills
- Python Programming
- Programming Principles
- Scripting Languages
- Data Structures
- Computer Programming
- Computer Programming Tools
- Development Environment
- Integrated Development Environments
- Debugging
- Scripting
- Program Development
- Computational Thinking

## Resumen de sección

### Fundamentos de programación
- **Programación**: crear instrucciones paso a paso (receta) para la computadora.
- **Sintaxis**: reglas de construcción del código.
- **Semántica**: significado/efecto de las instrucciones.
- **Script**: programa corto para automatizar tareas específicas.
- **Automatización**: reemplazar pasos manuales por automáticos. Ahorra tiempo, reduce errores y aumenta la consistencia.

### Python como lenguaje
- Lenguaje de propósito general, multiplataforma, interpretado y de tipado dinámico.
- Sintaxis similar al inglés, legible, ideal para automatización de TI y análisis de datos.
- Case-sensitive; usa indentación para definir bloques de código.
- Se puede usar en IDLE, VS Code, Jupyter Notebook, Colab, PyCharm.

### Tipos de datos y sintaxis básica
- **Tipos**: `int`, `float`, `string`, `bool`, `list`, `tuple`, `dict`, `set`, `None`.
- **Variables**: usar `snake_case`, nombres descriptivos, evitar palabras reservadas.
- **Type hints** opcionales (`nombre: str = "Ana"`) para documentar el tipo esperado.
- **Conversión**: implícita (automática) y explícita (`int()`, `float()`, `str()`).
- **Operadores**: aritméticos (`+`, `-`, `*`, `/`, `//`, `%`, `**`), comparación (`==`, `!=`, `<`, `>`, `<=`, `>=`), lógicos (`and`, `or`, `not`).

### Funciones
- Definir con `def nombre(parametros):` y devolver valor con `return`.
- **Reutilización**: si un bloque se repite, convertirlo en función.
- **Refactorización**: reescribir código para hacerlo más legible y autodocumentado.
- Buenas prácticas: nombres descriptivos, comentarios con `#`, código claro.
- Funciones integradas clave: `print()`, `type()`, `len()`, `str()`, `sorted()`, `max()`, `min()`, `range()`, `enumerate()`.

### Estructuras de control
- **Condicionales**: `if`, `elif`, `else` para ramificar según condiciones booleanas.
- **Bucles `while`**: ejecutan mientras la condición sea `True`. Requieren inicializar variables y actualizar la condición para evitar loops infinitos.
- **Bucles `for`**: iteran sobre secuencias (`range()`, listas, strings, etc.). Más concisos que `while` para secuencias conocidas.
- **Control de flujo**: `break` (salir del bucle), `continue` (saltar iteración), `pass` (marcador de posición).
- **Bucles anidados**: un bucle dentro de otro. Aumentan la complejidad, usarlos con cuidado.
- **Recursión**: función que se llama a sí misma. Requiere un caso base y un caso recursivo. Límite por defecto: 1000 llamadas.

### Strings
- **Inmutables**: no se pueden modificar, solo crear nuevos strings.
- **Indexación** con `[0]`, índices negativos (`[-1]` = último carácter).
- **Slicing**: `string[start:end:step]`.
- **Métodos principales**: `.upper()`, `.lower()`, `.strip()`, `.count()`, `.endswith()`, `.isnumeric()`, `.isalpha()`, `.replace()`, `.split()`, `.join()`.
- **Formateo**: `.format()`, f-strings (`f"Hola {nombre}"`), operador `%` (legado).

### Listas y tuplas
- **Listas**: mutables, `[]`, métodos: `.append()`, `.insert()`, `.remove()`, `.pop()`, `.sort()`, `.reverse()`.
- **Tuplas**: inmutables, `()`, ideales para retornar múltiples valores y unpacking.
- **Comprensión de listas**: `[expr for item in iterable if condition]` — forma concisa de crear listas.
- `enumerate()`: obtiene índice y valor al iterar.

### Diccionarios
- Pares **clave:valor** `{}`, mutables. Claves pueden ser strings, números o tuplas.
- Acceso: `dict[clave]`, `.get(clave, default)`. Métodos: `.keys()`, `.values()`, `.items()`, `.update()`.
- Iterar con `for k, v in dict.items()`.
- Operador merge `|` (Python 3.9+).

### Programación orientada a objetos (POO)
- **Clases**: plantillas para crear objetos. **Instancias**: objetos concretos de una clase.
- **Constructor** `__init__()`, método `__str__()`, métodos especiales (dunder).
- Tipos de métodos: instancia (`self`), clase (`@classmethod`, `cls`), estáticos (`@staticmethod`).

### Proyecto final y metodología
- Enfoque estructurado: 1) Identificar problema, 2) Investigar soluciones, 3) Planificar, 4) Escribir código, 5) Ejecutar y verificar.
- Separar responsabilidades: funciones de procesamiento vs. funciones de presentación.
- `sort(key=función)` para ordenar listas por un criterio personalizado.
- Bibliotecas útiles: `csv`, `secrets`, `subprocess`, `pathlib`.