import re

frase = 'Oi! Bom dia, comunidade!!!'

encontre_dia = re.search('dia', frase)

igual_dia = re.match('\.dia$', frase)

print(encontre_dia)

print(igual_dia.group())