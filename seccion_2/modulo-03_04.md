# Repaso del módulo

## Resumen del Módulo 3: Expresiones regulares
- NO dejes que las expresiones regulares te intimiden. Son una herramienta poderosa para buscar y manipular texto.
- Practica con ejemplos simples y ve aumentando la complejidad a medida que te sientas más cómodo.

---

## Glosario de términos
- `Alteration` (Alteración): Expresión regular que coincide con cualquiera de las alternativas separadas por el símbolo de barra vertical (|).
- `Backreference` (Referencia inversa): Se aplica al usar `re.sub()` para sustituir el valor de un grupo de captura en la salida.
- `Character classes` (Clases de caracteres): Se escriben entre corchetes y permiten listar los caracteres que se buscan dentro de ellos.
- `Character ranges` (Rangos de caracteres): Rangos que se utilizan para comparar un solo carácter con un conjunto de posibilidades.
- `Grep` (Grep): Una herramienta especialmente fácil de usar y a la vez muy potente para aplicar expresiones regulares.
- `Lookahead` (Adelanto): Expresión regular que coincide con un patrón solo si le sigue otro patrón.
- `Regular expression` (Expresión regular): Una consulta de búsqueda de texto expresada mediante un patrón de cadena, también conocida como RegEx o RegExp.
- `Wildcard` (Comodín): Un carácter que puede coincidir con más de un carácter.

---

## Qwiklabs assessment: Work with regular expressions
```Python
#!/usr/bin/env python3

import re
import csv


def contains_domain(address, domain):
  """Returns True if the email address contains the given,domain,in the domain position, false if not."""
  domain_pattern = r'[\w\.-]+@'+domain+'$'
  if re.match(domain_pattern,address):
    return True
  return False


def replace_domain(address, old_domain, new_domain):
  """Replaces the old domain with the new domain in the received address."""
  old_domain_pattern = r'' + old_domain + '$'
  address = re.sub(old_domain_pattern, new_domain, address)
  return address

def main():
  """Processes the list of emails, replacing any instances of the old domain with the new domain."""
  old_domain, new_domain = 'abc.edu', 'xyz.edu'
  csv_file_location = '<csv_file_location>'
  report_file = '<data-directory>' + '/updated_user_emails.csv'
  user_email_list = []
  old_domain_email_list = []
  new_domain_email_list = []

  with open(csv_file_location, 'r') as f:
    user_data_list = list(csv.reader(f))
    user_email_list = [data[1].strip() for data in user_data_list[1:]]

    for email_address in user_email_list:
      if contains_domain(email_address, old_domain):
        old_domain_email_list.append(email_address)
        replaced_email = replace_domain(email_address,old_domain,new_domain)
        new_domain_email_list.append(replaced_email)

    email_key = ' ' + 'Email Address'
    email_index = user_data_list[0].index(email_key)

    for user in user_data_list[1:]:
      for old_domain, new_domain in zip(old_domain_email_list, new_domain_email_list):
        if user[email_index] == ' ' + old_domain:
          user[email_index] = ' ' + new_domain
  f.close()

  with open(report_file, 'w+') as output_file:
    writer = csv.writer(output_file)
    writer.writerows(user_data_list)
    output_file.close()

main()
"""
Full Name, Email Address
Blossom Gill, blossom@xyz.edu
Hayes Delgado, nonummy@utnisia.com
Petra Jones, ac@xyz.edu
Oleg Noel, noel@liberomauris.ca
Ahmed Miller, ahmed.miller@nequenonquam.co.uk
Macaulay Douglas, mdouglas@xyz.edu
Aurora Grant, enim.non@xyz.edu
Madison Mcintosh, mcintosh@nisiaenean.net
Montana Powell, montanap@semmagna.org
Rogan Robinson, rr.robinson@xyz.edu
Simon Rivera, sri@xyz.edu
Benedict Pacheco, bpacheco@xyz.edu
Maisie Hendrix, mai.hendrix@xyz.edu
Xaviera Gould, xlg@utnisia.net
Oren Rollins, oren@semmagna.com
Flavia Santiago, flavia@utnisia.net
Jackson Owens, jackowens@xyz.edu
Britanni Humphrey, britanni@ut.net
Kirk Nixon, kirknixon@xyz.edu
Bree Campbell, breee@utnisia.net
"""
```

---

## Ejemplo: Trabajar con expresiones regulares
- En este laboratorio, encontramos usuarios que utilizaban un dominio de correo electrónico antiguo en una lista extensa mediante expresiones regulares.
- Escribimos un script que reemplazaba el dominio antiguo (abc.edu) por uno nuevo (xyz.edu) y guardamos todos los dominios, incluidos los actualizados, en un archivo nuevo.

---

## Diálogo con el entrenador: Automatización con expresiones regulares
" ¡Bienvenidos! En este diálogo, exploraremos cómo usar expresiones regulares (Regex) para la automatización de texto.

Esto es lo que cubriremos:

El papel de las expresiones regulares en el procesamiento de texto.

Funciones clave del módulo `re` para buscar y modificar texto, con casos de uso en automatización informática.

Un enfoque sistemático para usar expresiones regulares en tareas de automatización." 
```txt
Durante la sesión de hoy sobre el uso de expresiones regulares (Regex) para la automatización de texto, nos centramos en su función, las funciones clave del módulo `re` para buscar y modificar texto, y el enfoque sistemático para su uso en tareas de automatización.

Sus puntos fuertes:

Definió correctamente las expresiones regulares como secuencias de caracteres que definen un patrón de búsqueda.

Identificó y diferenció correctamente entre `re.sub()` para la sustitución, `re.findall()` para extraer todas las coincidencias y `re.split()` para dividir cadenas en listas.

Áreas de mejora:

Inicialmente, consideró `re.match()` para una tarea que requería una coincidencia de patrones y sustitución más amplia. Recuerde que `re.match()` solo busca un patrón al principio de una cadena. Repasar los casos de uso específicos de cada función del módulo `re` le ayudará a comprender mejor el concepto.
```

---

## Module 3 challenge: Work with Regular Expressions

1. What is a regular expression? 
> A sequence of characters that forms a search pattern

2. Which of the following statements are correct regarding the re.sub() function? Select all that apply.
> The re.sub() function allows the use of capturing groups to reuse matched patterns in the replacement text.
> The replacement string in re.sub() can contain back references to captured groups.
> The re.sub() function takes four parameters: the pattern, the replacement string, the input text, and an optional flags parameter.

3. You have a list of website urls that includes both securely encrypted websites that begin with https://www. and the unencrypted websites that begin with http://. The list includes websites that end in .com and .co. 
Complete the secure_website_domain() function so it returns the part of the website between www. and the last part of the url (.com or .co) for only the secure websites. 
```Python
def secure_website_domain(website):
 pattern = r"^https://www\.(.+)\.(com|co)$" # enter the regex pattern here
 result = re.match(pattern, website) # enter the re method here
 if result is None:
  return ""
 return result.group(1) # enter the correct capturing group


print(secure_website_domain("http://www.text.com")) #Should return nothing
print(secure_website_domain("https://www.text.com")) #Should return text
print(secure_website_domain("http://www.text.co")) #Should return nothing
print(secure_website_domain("https://www.text.co")) #Should return text
```

3.1 You are reading an article that contains website urls in the format: 

https://www.website-domain.com

You’d like to extract the complete urls from the text automatically, instead of copying and pasting them by hand. Complete the function find_url() to extract all encrypted websites that begin with https:// and end with any top level domain, such as .org, .com, or .co from the text.
```Python
def find_url(website):
 pattern = r"https://www\.[\w\-]+\.\w+" #enter the regex pattern here
 result = re.findall(pattern, website) #enter the re method here
 return result


print(find_url("Go to the website https://www.coursera.com find more information about Google Certificate Programs. Then, visit https://www.python.org/ to learn more about Python. ")) # Should return ['https://www.coursera.com', 'https://www.python.org']
print(find_url("You can find anything on https://www.google.com!")) # Should return ['https://www.google.com']
print(find_url("You can find anything on http://www.google.com!")) # Should return []
print(find_url("Check out python.org!")) # Should return []
```

4. You are exploring the punctuation at the end of sentences and want to split sentences so that each word is separate and any punctuation is included in the word next to it. Complete the parse_sentences() function to accomplish this task. 
```Python
def parse_sentences(sentence):
 pattern = r"\s+" #enter the regex pattern here
 result = re.split(pattern, sentence) #enter the re method  here
 return result

print(parse_sentences("Hello! How are you doing?")) # should return ['Hello!', 'How', 'are', 'you', 'doing?']
print(parse_sentences("what a beautiful day it is")) # should return ['what', 'a', 'beautiful', 'day', 'it', 'is']
print(parse_sentences("2 + 2 is definitely 4!")) # should return ['2', '+', '2', 'is', 'definitely', '4!']
```

4.1 You’re working with a dataset on capital cities around the world. This dataset includes a field that contains information on both city and country. You’d like to separate this field into two fields, a city field and a country field. In the current field, city and country are separated by either a comma or a period. Complete the function parse_city_country() to split city and country into two strings and return only the city.
```Python
def parse_city_country(text):
  pattern = r"^(.*?)[,.]\s*(.*)$" #enter the regex pattern here
  result = re.match(pattern, text) #enter the re method  here
  if not result:
    return ""
  return result.group(1) #return the correct capturing group

print(parse_city_country("Paris, France")) # should return Paris
print(parse_city_country("Mumbai, India")) # should return Mumbai
print(parse_city_country("Rio de Janeiro. Brazil")) # should return Rio de Janeiro
print(parse_city_country("Tokyo! Japan"))  # result should be blank
```

5. A company uses unique, 9-character codes that begin with a capital letter, followed by a hyphen (-), followed by 7 or 8 digits as employee ID numbers, in the format: 

A-1234567 or A-12345678 

Project reports submitted to the company include the employee’s ID number and a summary of the work they completed on the project. A data analyst wants to pull all of the employee ID numbers out of these projects. Complete the find_eid() function to extract these employee ID numbers from the reports. 
```Python
def find_eid(report):
  pattern = r"[A-Z]-[\d]{7,8}\b" #enter the regex pattern here
  result = re.findall(pattern, report) #enter the re method  here
  return result


print(find_eid("Employees B-1234567 and C-12345678 worked with products X-123456 and Z-123456789")) # Should return ['B-1234567', 'C-12345678']
print(find_eid("Employees B-1234567 and C-12345678, not employees b-1234567 and c-12345678")) #Should return ['B-1234567', 'C-12345678']
```

6. In the provided code snippet, what is the purpose of the replace_domain() function?
```Python
def replace_domain(address, old_domain, new_domain):
  old_domain_pattern = r'' + old_domain + '$'
  address = re.sub(old_domain_pattern, new_domain, address)
  return address
```
> To create a new email address by replacing an old domain with a new domain

6.1 In the lab, the variable old_domain_pattern is defined as:  r'' + old_domain + '$'. What information does this variable store?
> A regular expression pattern to identify the old domain

7. What is the purpose of initializing the old_domain_email_list in the code from the lab?
> To perform a substitution operation on email addresses
# mala, posible > To store email addresses with the old domain that match the regex pattern

7.1 In the lab, you were tasked with initializing a list called old_domain_email_list and populating it with email addresses that contain the old domain name and meet the criteria defined in the contains_domain() function. The list of current email addresses was provided in the list user_email_list.  How did you accomplish this in the lab?
> Step 1: Initialized old_domain_email_list with an empty list. 
> Step 2: Used a for loop to iterate over the emails in user_email_list, checking each email address to determine if it contains the old domain using the contains_domain() function, which uses regex to check if it matches the old domain. 
> Step 3: Appended email addresses with the old domain to the old_domain_email_list. 

8. Why is it considered good practice to use the close() method to close a file after processing it in Python?
> To free up system resources and prevent further reading or writing to the file

9. Which Python libraries are commonly employed to perform updates to domain names and to save all the modified domain names to a separate file?
> re (regular expressions) and open() function

9.1 Why is it important to replace old domain names with new ones and generate a new file containing all user names with their respective email addresses?
> To enhance data security measures.

10. In the Python script for processing user_emails.csv, what is the purpose of the contains_domain() function?
> To check if an email address belongs to a specific domain, using regular expressions (regex)

10.1 In the Python script for processing user_emails.csv, what is the purpose of the contains_domain() function?
> To check if an email address belongs to a specific domain, using regular expressions (regex)