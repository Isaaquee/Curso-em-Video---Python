print ('===Desafio04===')
print ('Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ele')
r = input('Digite algo: ')
#Verifica o tipo de string 
print('O tipo primitivo desse valor é',type(r))
#Verifica se contém espaço
print('Contém espaço?', r.isspace())
#Verifica se tem algum número
print('É um numero?', r.isnumeric())
#Verifica se a String tem o conteúdo apenas alfabético
print ('É alfabético?', r.isalpha())
#Verifica se a String tem conteúdo alfa-numérico
print ('É alfanumerico?',r.isalnum())
#Verifica se a String tem conteúdo em maiusculo
print ('Esta em maiuscula?', r.isupper())
#Verifica se a String tem conteúdo em maiusculo
print ('Esta em minuscula?', r.islower())
#Verifica se esta capitalizada, quer dizer com a inicial maiuscula e as demais letras minusculas
print ('Está capitalizada?', r.istitle())