# Script de buscas no github
# By: lucas-Dk

try:
	import requests
	import json
	import os
	import sys
	from time import sleep as sl
except:
	print("\033[1;31m[!] OOPS: parece que você não tem os requisitos... :(")
	print("Digite esse comando para instalar as dependências:\033[m")
	print("\npip install -r requirements.txt")
else:
	
	while True:
		os.system("clear")
		print("""\033[1;31m
                                 _                       _   
                                ( )                   _ ( )_ 
  ___    __     _ _  _ __   ___ | |__   ______   __  (_)| ,_)
/',__) /'__`\ /'_` )( '__)/'___)|  _ `\(______)/'_ `\| || |  
\__, \(  ___/( (_| || |  ( (___ | | | |       ( (_) || || |_ 
(____/`\____)`\__,_)(_)  `\____)(_) (_)       `\__  |(_)`\__)
                                              ( )_) |        
                                               \___/'        
\033[m
========================================================================

\033[1;32m[*]\033[m Feito por lucas-Dk
\033[1;32m[*]\033[m Meu facebook: https://www.facebook.com/Walker.Lxrd/
\033[1;32m[*]\033[m Meu github: https://github.com/lucas-Dk

[ 1 ] - Fazer uma busca
[ 2 ] - Saber como usar
[ x ] - Sair

	""")
		try:
			escolhe = input("\033[1;32m[+]\033[m O que você deseja: ")
		except KeyboardInterrupt:
			print("\033[1;31mSaindo...\033[m")
			sys.exit()
		else:
			print()
			if escolhe.isnumeric():
				escolhe = int(escolhe)
				if escolhe == 1:
					try:
						user = str(input("\033[1;32m[+]\033[m Nome de usuário do github: "))
						ver_repost = str(input("\033[1;32m[+]\033[m Deseja ver os repositórios desse usuário [Y/N]: ")).upper()
					except KeyboardInterrupt:
						print("\033[1;31mSaindo...\033[m")
						sys.exit()
					else:
						if ver_repost == "Y":
							url = "https://api.github.com/users/{}/repos".format(user)
							requisitar = requests.get(url)
							if requisitar.status_code == 200:
								print("\n\033[1;32m[-] PEGANDO OS REPOSITÓRIOS DO USER:\033[m {}\n".format(user))
								dados_api = json.loads(requisitar.text)
								for x in dados_api:
									resultado_api_repos = x
									for chave,valor in resultado_api_repos.items():
										if chave == "owner":
											pass
										else:
											if chave and valor:	
												if chave == "name":
													print("\033[1;32m[*] {}:\033[m {}".format(chave.replace(chave,"Repositório"),valor))
												elif chave == "description":
													print("\033[1;31m[+] {}:\033[m {}".format(chave.replace(chave,"Descrição"),valor))
												elif chave == "forks":
													print("\033[1;31m[+] {}:\033[m {}".format(chave.replace(chave,"Forks"),valor))
												elif chave == "watchers":
													print("\033[1;31m[+] {}:\033[m {}".format(chave.replace(chave,"Pessoas visualizando o repositório"),valor))
													print()
												elif chave == "clone_url":
													print("\033[1;31m[+] {}:\033[m {}".format(chave.replace(chave,"Link para clonar"),valor))
												elif chave == "language":
													print("\033[1;31m[+] {}:\033[m {}".format(chave.replace(chave,"Feito com a linguagem"),valor))
												elif chave == "license":
													for ch,vl in valor.items():
														if ch == "name":
															print("\033[1;31m[+] {}:\033[m {}".format(ch.replace(ch,"Licença-codigo"),vl))
															break
													print()
								try:
									sair = str(input("\033[1;32m[+]\033[m S = sair / C = continuar [S/C]: ")).upper()
								except KeyboardInterrupt:
									print("\033[1;31mSaindo...\033[m")
									sys.exit()
								else:
									while sair not in "S"  and sair not in "C":
										try:
											sair = str(input("\033[1;32m[+]\033[m S = sair / C = continuar [S/C]: ")).upper()
										except KeyboardInterrupt:
											print("\033[1;31mSaindo...\033[m")
											sys.exit()
										else:
											if sair == "S":
												sys.exit()
											elif sair == "C":
												pass
						elif ver_repost == "N":
							url = "https://api.github.com/users/{}".format(user)
							requisitar_url = requests.get(url)
							if requisitar_url.status_code == 200:
								dados = json.loads(requisitar_url.text)
								for chave,valor in dados.items():
									if chave == "login":
										pass
									else:
										print("\033[1;32m[*] {}:\033[m {}".format(chave,valor))
								input("Aperte ENTER para voltar ao menu... ")
								os.system("clear")

				elif escolhe == 2:
					print("""
Esse script utiliza a API do github, faz as buscas pelo nome de usuário
e retorna os dados mais relevantes para quem estiver utilizando!

[Y/N] = Caso escolha Y, ele irá retornar para você:

- Nome dos repositórios
- Descrição
- Números de Forks
- Número de visualizações
- link para dar git colone no repositório e etc

[Y/N] = Caso escolha N, ele irá retornar para você:

- Todos os dados do usuário que você pesquisar menos os repositórios!
				\n""")
					input("Aperte ENTER para voltar ao menu... ")
					os.system("clear")

				elif escolhe == "x" or escolhe == "X":
					sys.exit()
