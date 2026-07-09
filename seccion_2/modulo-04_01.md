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