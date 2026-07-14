# Expresiones regulares avanzadas

## Reseña: Capturando grupos
- Los siguientes bloques de código se usarán en el próximo video:
```Python
import re
result = re.search(r"^(\w*), (\w*)$", "Lovelace, Ada")
print(result)
print(result.groups())
print(result[0])
print(result[1])
print(result[2])
"{} {}".format(result[2], result[1])
"""
<_sre.SRE_Match object; span=(0, 13), match='Lovelace, Ada'>
('Lovelace', 'Ada')
Lovelace, Ada
Lovelace
Ada
Ada Lovelace
"""

import re
def rearrange_name(name):
    result = re.search(r"^(\w*), (\w*)$", name)
    if result is None:
        return name
    return "{} {}".format(result[2], result[1])
rearrange_name("Lovelace, Ada")
# Ada Lovelace

import re
def rearrange_name(name):
    result = re.search(r"^(\w*), (\w*)$", name)
    if result is None:
        return name
    return "{} {}".format(result[2], result[1])
rearrange_name("Ritchie, Dennis")
# Dennis Ritchie

import re
def rearrange_name(name):
    result = re.search(r"^([\w \.-]*), ([\w \.-]*)$", name)
    if result == None:
        return name
    return "{} {}".format(result[2], result[1])
rearrange_name("Hopper, Grace M.")
# Grace M. Hopper
```

---

## Capturando grupos
- Por ejemplo, es posible que deseemos extraer el nombre de host o ​un ID de proceso de una línea de registro y usar ese valor para otra operación. ​Para eso necesitamos usar un concepto de expresiones regulares llamadas ​grupos de captura.
- `Capturing groups` nos permiten extraer partes de una cadena que coinciden con un patrón de expresión regular. Se definen usando paréntesis `()` alrededor del patrón que queremos capturar.
- Podemos usar `result.groups()` para obtener una tupla de todos los grupos capturados, o podemos acceder a cada grupo individualmente usando índices, como `result[1]`, `result[2]`, etc.

---

## Reseña: Más información sobre los calificadores de repetición
- Los siguientes bloques de código se usarán en el próximo video:
```Python
import re
print(re.search(r"[a-zA-Z]{5}", "a ghost"))
# <_sre.SRE_Match object; span=(2, 7), match='ghost'>

import re
print(re.search(r"[a-zA-Z]{5}", "a scary ghost appeared"))
# <_sre.SRE_Match object; span=(2, 7), match='scary'

import re
print(re.findall(r"[a-zA-Z]{5}", "a scary ghost appeared"))
# ['scary', 'ghost', 'appea']

import re
re.findall(r"\b[a-zA-Z]{5}\b", "A scary ghost appeared")
# ['scary', 'ghost']

import re
print(re.findall(r"\w{5,10}", "I really like strawberries"))
# ['really', 'strawberri']

import re
print(re.findall(r"\w{5,}", "I really like strawberries"))
# ['really', 'strawberries']

import re
print(re.search(r"s\w{,20}", "I really like strawberries"))
# <_sre.SRE_Match object; span=(14, 26), match='strawberries'>
```

---

## Más información sobre los calificadores de repetición
- Los calificadores de repetición nos permiten especificar cuántas veces queremos que un patrón coincida. Algunos ejemplos incluyen:
  - `{n}`: Coincide exactamente n veces.
  - `{n,}`: Coincide n o más veces.
  - `{,m}`: Coincide hasta m veces.
  - `{n,m}`: Coincide entre n y m veces.
- Para buscar palabras de exactamente 5 letras, podemos usar el patrón `[a-zA-Z]{5}` junto a `\b` para indicar los límites de palabra, como en `\b[a-zA-Z]{5}\b`. Esto nos permitirá encontrar palabras que tengan exactamente 5 letras.

---

## Reseña: Extracción de un PID mediante expresiones regulares en Python
- Los siguientes bloques de código se usarán en el próximo video:
```Python
import re
log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
print(result[1])
# 12345

import re
log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
result = re.search(regex, "A completely different string that also has numbers [34567]")
print(result[1])
# 34567

import re
log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
result = re.search(regex, "A completely different string that also has numbers [34567]")
result = re.search(regex, "99 elephants in a [cage]")
print(result[1])
#Note that this print command results in an error as shown in the video. 

import re
log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
result = re.search(regex, "A completely different string that also has numbers [34567]")
result = re.search(regex, "99 elephants in a [cage]")
def extract_pid(log_line):
    regex = r"\[(\d+)\]"
    result = re.search(regex, log_line)
    if result is None:
        return ""
    return result[1]
print(extract_pid(log))
# 12345

import re
log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
result = re.search(regex, "A completely different string that also has numbers [34567]")
result = re.search(regex, "99 elephants in a [cage]")
def extract_pid(log_line):
    regex = r"\[(\d+)\]"
    result = re.search(regex, log_line)
    if result is None:
        return ""
    return result[1]
print(extract_pid(log))
print(extract_pid("99 elephants in a [cage]"))
# 12345
# ""
```

---

## Extracción de un PID mediante expresiones regulares en Python
- En la expresión `r"\[(\d+)\]"`:
    - `\[` y `\]` coinciden con los corchetes literales.
    - `(\d+)` es un grupo de captura que coincide con uno o más dígitos. El `+` indica que debe haber al menos un dígito.
```Python
# Add to the regular expression used in the extract_pid function, to return the uppercase message in parenthesis, after the process id.
import re
def extract_pid(log_line):
    regex = r"\[(\d+)\]: ([A-Z]+)"
    result = re.search(regex, log_line)
    if result is None:
        return None
    return "{} ({})".format(result[1], result[2])

print(extract_pid("July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade")) # 12345 (ERROR)
print(extract_pid("99 elephants in a [cage]")) # None
print(extract_pid("A string that also has numbers [34567] but no uppercase message")) # None
print(extract_pid("July 31 08:08:08 mycomputer new_process[67890]: RUNNING Performing backup")) # 67890 (RUNNING)
```

---

## Reseña: División y reemplazo
- Los siguientes bloques de código se usarán en el próximo video:
```Python
import re
re.split(r"[.?!]", "One sentence. Another one? And the last one!")
# ['One sentence', ' Another one', ' And the last one', '']

import re
re.split(r"([.?!])", "One sentence. Another one? And the last one!")
# ['One sentence', '.', ' Another one', '?', ' And the last one', '!', '']

import re
re.sub(r"[\w.%+-]+@[\w.-]+", "[REDACTED]", "Received an email for go_nuts95@my.example.com")
# 'Received an email for [REDACTED]'

import re
re.sub(r"^([\w .-]*), ([\w .-]*)$", r"\2 \1", "Lovelace, Ada")
# 'Ada Lovelace'
```

---

## División y reemplazo
- La función `re.split()` divide una cadena en una lista, usando un patrón de expresión regular como delimitador.
- Ejemplo: `re.split(r"[.?!]", "One sentence. Another one? And the last one!")` dividirá la cadena en cada punto, signo de interrogación o signo de exclamación.
- La función `re.sub()` reemplaza todas las ocurrencias de un patrón de expresión regular en una cadena con una cadena de reemplazo.
- Ejemplo: `re.sub(r"[\w.%+-]+@[\w.-]+", "[REDACTED]", "Received an email for go_nuts95@my.example.com")` reemplazará la dirección de correo electrónico con `[REDACTED]`.
- `Backreferences` en `re.sub()` permiten referirse a grupos capturados en la cadena de reemplazo. Por ejemplo, `r"\2 \1"` intercambia el orden de los grupos capturados en la expresión regular.

---

## Guía de estudio: Expresiones regulares avanzadas
- Las expresiones regulares avanzadas —conocidas comúnmente como regex avanzadas— son utilizadas por los desarrolladores para realizar búsquedas de patrones complejos en cadenas de texto.
- Alteraciones: Una alteración coincide con cualquiera de las alternativas separadas por el símbolo de barra vertical |.
- Ejemplo: `r"location.*(London|Berlin|Madrid)"`: Esta línea de código coincidirá con la cadena de texto "location is London", "location is Berlin" o "location is Madrid".
- Coincidencia solo al principio o al final: Si usas el símbolo de circunflejo (^) como primer carácter de tu expresión regular, solo coincidirá si el patrón aparece al inicio de la cadena.
- De igual manera, si usas el símbolo de dólar ($) al final de una expresión regular, solo coincidirá si el patrón aparece al final.
- Ejemplo: `r"^Mi nombre es (\w+)"`: Esta línea de código coincidirá con "Mi nombre es Asha", pero no con "Hola. Mi nombre es Asha".
- Rangos de caracteres: Los rangos de caracteres se pueden usar para comparar un solo carácter con un conjunto de posibilidades.
- Ejemplos: 
    - `r"[A-Z]"` Coincidirá con una sola letra mayúscula.
    - `r"[0-9$-,.]"` Coincidirá con cualquiera de los dígitos del cero al nueve, o con el signo de dólar, el guion, la coma o el punto.
    - `r"([0-9]{3}-[0-9]{3}-[0-9]{4})"` Coincidirá con un número de teléfono estadounidense como el 888-123-7612.
- Retroreferencias: Se utiliza al usar `re.sub()` para sustituir el valor de un grupo de captura en la salida.
- Ejemplo: `re.sub(r"([A-Z])\.\s+(\w+)", r"Ms. \2", "A. Weber y B. Bellmas se han unido al equipo.")` Esta línea de código producirá: «Ms. Weber y Ms. Bellmas se han unido al equipo».
- Búsqueda anticipada: Coincide con un patrón solo si le sigue otro patrón.
- Ejemplo: `r"(Test\d)-(?=Passed)"` y la cadena fuera `"Test1-Passed, Test2-Passed, Test3-Failed, Test4-Passed, Test5-Failed"`, el resultado sería: Test1, Test2, Test4

---

## Test your knowledge: Advanced regular expressions
1. You’re working with a CSV file that contains employee information. Each record has a name field, followed by a phone number field, and a role field. The phone number field contains U.S. phone numbers and needs to be modified to the international format, with +1- in front of the phone number. The rest of the phone number should not change. Fill in the regular expression, using groups, to use the transform_record() function to do that.
```Python
import re
def transform_record(record):
  new_record = re.sub(r"^([\w ]*),([\d-]+),(.*)$", r"\1,+1-\2,\3", record)
  return new_record

print(transform_record("Sabrina Green,802-867-5309,System Administrator")) 
# Sabrina Green,+1-802-867-5309,System Administrator

print(transform_record("Eli Jones,684-3481127,IT specialist")) 
# Eli Jones,+1-684-3481127,IT specialist

print(transform_record("Melody Daniels,846-687-7436,Programmer")) 
# Melody Daniels,+1-846-687-7436,Programmer

print(transform_record("Charlie Rivera,698-746-3357,Web Developer")) 
# Charlie Rivera,+1-698-746-3357,Web Developer
```

2. Question 2
The multi_vowel_words() function returns all words with 3 or more consecutive vowels (a, e, i, o, u). Fill in the regular expression to do that
```Python
import re
def multi_vowel_words(text):
  pattern = r"\b\w*[aeiou]{3,}\w*\b"
  result = re.findall(pattern, text)
  return result

print(multi_vowel_words("Life is beautiful")) 
# ['beautiful']

print(multi_vowel_words("Obviously, the queen is courageous and gracious.")) 
# ['Obviously', 'queen', 'courageous', 'gracious']

print(multi_vowel_words("The rambunctious children had to sit quietly and await their delicious dinner.")) 
# ['rambunctious', 'quietly', 'delicious']

print(multi_vowel_words("The order of a data queue is First In First Out (FIFO)")) 
# ['queue']

print(multi_vowel_words("Hello world!")) 
# []
```

3. When capturing regex groups, what datatype does the groups method return?
> A tuple

4. The transform_comments() function converts comments in a Python script into those usable by a C compiler. This means looking for text that begins with a hash mark (#) and replacing it with double slashes (//), which is the C single-line comment indicator. For the purpose of this exercise, we'll ignore the possibility of a hash mark embedded inside of a Python command, and assume that it's only used to indicate a comment. We also want to treat repetitive hash marks (##), (###), etc., as a single comment indicator, to be replaced with just (//) and not (#//) or (//#). Fill in the parameters of the substitution method to complete this function: 
```Python
import re
def transform_comments(line_of_code):
  result = re.sub(r"#+", "//", line_of_code)
  return result

print(transform_comments("### Start of program")) 
# Should be "// Start of program"
print(transform_comments("  number = 0   ## Initialize the variable")) 
# Should be "  number = 0   // Initialize the variable"
print(transform_comments("  number += 1   # Increment the variable")) 
# Should be "  number += 1   // Increment the variable"
print(transform_comments("  return(number)")) 
# Should be "  return(number)"
```

5. The convert_phone_number() function checks for a U.S. phone number format: XXX-XXX-XXXX (3 digits followed by a dash, 3 more digits followed by a dash, and 4 digits), and converts it to a more formal format that looks like this: (XXX) XXX-XXXX. Fill in the regular expression to complete this function.
```Python
import re
def convert_phone_number(phone):
  result = re.sub(r"(\d{3})-(\d{3})-(\d{4})\b", r"(\1) \2-\3", phone)
  return result

print(convert_phone_number("My number is 212-345-9999.")) # My number is (212) 345-9999.
print(convert_phone_number("Please call 888-555-1234")) # Please call (888) 555-1234
print(convert_phone_number("123-123-12345")) # 123-123-12345
print(convert_phone_number("Phone number of Buckingham Palace is +44 303 123 7300")) # Phone number of Buckingham Palace is +44 303 123 7300
```