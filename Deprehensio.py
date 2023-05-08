import urllib

import urllib.request

import c

import os

import sys

import time

while True:

 os.system('clear')

 print(f"""{c.bcyan}                   _.-, 

              _ .-'  / .._

           .-:'/ - - \:::::-.

         .::: '  e e  ' '-::::.

        ::::'(    ^    )_.::::::

       ::::.' '.  o   '.::::'.'/_

   .  :::.'       -  .::::'_   _.:

 .-''---' .'|      .::::'   '''::::

'. ..-:::'  |    .::::'        ::::

 '.' ::::    \ .::::'          ::::

      ::::   .::::'           ::::

       ::::.::::'._          ::::

        ::::::' /  '-      .::::

         '::::-/__    __.-::::'

           '-::::::::::::::-'

               '''::::'''

               Deprehensio

               {c.white}""")

 print('═'*46)

 print('           By: Phant0m The Great')

 print('═'*46)

 print(f'''

[{c.blue}1{c.white}] Capturar código HTML de site

[{c.blue}2{c.white}] Informações

[{c.blue}3{c.white}] Sair''')

 ech=input('\n[?] Digite sua escolha: ')

 if ech=='1':

   os.system('clear')

   print(f"""{c.bcyan}                   _.-, 

              _ .-'  / .._

           .-:'/ - - \:::::-.

         .::: '  e e  ' '-::::.

        ::::'(    ^    )_.::::::

       ::::.' '.  o   '.::::'.'/_

   .  :::.'       -  .::::'_   _.:

 .-''---' .'|      .::::'   '''::::

'. ..-:::'  |    .::::'        ::::

 '.' ::::    \ .::::'          ::::

      ::::   .::::'           ::::

       ::::.::::'._          ::::

        ::::::' /  '-      .::::

         '::::-/__    __.-::::'

           '-::::::::::::::-'

               '''::::'''

               Deprehensio

               {c.white}""")

   print('═'*46)

   print('           By: Phant0m The Great')

   print('═'*46)

   site2=input(f'[ {c.green}!{c.white} ] Digite a URL/LINK do site, Exemplo: https://www.google.com\n\n[i] Site: ')

   print('')

   print(f'{c.bcyan}Conectando...{c.white}')

   

   try:

    site = urllib.request.urlopen(site2)

   except urllib.error.URLError:

    print(f'{c.red}[!] O site está inacessível de forma segura ou ele não existe :/{c.white}')

    input(f'[{c.green}ENTER{c.white}] para voltar ao menu.')

   except ValueError:

     print(f'{c.red}\n[!] O site está inacessível de forma segura ou ele não existe :/{c.white}')

     input(f'[{c.green}ENTER{c.white}] para voltar ao menu.')

   else:

    print(f'{c.green}\n[!] CONECTADO COM SUCESSO !{c.white}')

    print(f'\n{c.cyan}[!] CAPTURANDO CÓDIGO...{c.white}')

    print(site.read())

    print('\n')

    input(f'[{c.green}ENTER{c.white}] para voltar ao menu.')

 elif ech=='2':

  os.system('clear')

  print(f"""{c.bcyan}                   _.-, 

              _ .-'  / .._

           .-:'/ - - \:::::-.

         .::: '  e e  ' '-::::.

        ::::'(    ^    )_.::::::

       ::::.' '.  o   '.::::'.'/_

   .  :::.'       -  .::::'_   _.:

 .-''---' .'|      .::::'   '''::::

'. ..-:::'  |    .::::'        ::::

 '.' ::::    \ .::::'          ::::

      ::::   .::::'           ::::

       ::::.::::'._          ::::

        ::::::' /  '-      .::::

         '::::-/__    __.-::::'

           '-::::::::::::::-'

               '''::::'''

               Deprehensio

               {c.white}""")

  print('═'*46)

  print('           By: Phant0m The Great')

  print('═'*46)

  print(f'[{c.blue}i{c.white}] Versão: V1\n[{c.blue}i{c.white}] Criador: Phant0m The Great\n[{c.blue}i{c.white}] Sobre: Deprehensio, ferramenta criada para facilitar a observação de códigos HTML de páginas web, podendo capturar o código do site com rapidez e segurança.\n\n[{c.red}#{c.white}] Encontrou falhas ?: Falhas no sistema do Deprehensio podem ocorrer, assim, caso encontre uma tela de erro, não pense 2 vezes em reportar a falha, entre em contato comigo pelo Discord e mande print da tela de erro, se possível um contexto de como chegou lá, agradeço.\n[{c.cyan}i{c.white}] Discord: 𝐏𝐡𝐚𝐧𝐭𝟎𝐦 𝐓𝐡𝐞 𝐆𝐫𝐞𝐚𝐭#1150\n')

  input(f'[{c.green}ENTER{c.white}] para voltar ao menu.')

 elif ech=='3':

   os.system('clear')

   print(f"""{c.bcyan}                   _.-, 

              _ .-'  / .._

           .-:'/ - - \:::::-.

         .::: '  e e  ' '-::::.

        ::::'(    ^    )_.::::::

       ::::.' '.  o   '.::::'.'/_

   .  :::.'       -  .::::'_   _.:

 .-''---' .'|      .::::'   '''::::

'. ..-:::'  |    .::::'        ::::

 '.' ::::    \ .::::'          ::::

      ::::   .::::'           ::::

       ::::.::::'._          ::::

        ::::::' /  '-      .::::

         '::::-/__    __.-::::'

           '-::::::::::::::-'

               '''::::'''

               Deprehensio

               {c.white}""")

   print('═'*46)

   print('           By: Phant0m The Great')

   print('═'*46)

   print('\n')

   print(f'[{c.yellow}#{c.white}] Até a próxima !')

   exit()



