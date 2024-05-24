import os
import shutil

# **Exercício 1: Criar um Arquivo**

with open('novo', 'w') as novo_arquivo:
    os.mkdir('novo_arquivo')

# **Exemplo 2: Entrar em um Diretório**

with os.scandir('C:/Users/aluno/Downloads/aula8/') as arquivos:
    for arquivo in arquivos:
      print('arquivo')

# **Exercício 3: Renomear um Diretório**

os.rename('novo', 'renomeado' )

# **Exercício 4: Remover um Diretório**

shutil.rmtree('C:/Users/aluno/Downloads/aula8/pasta_teste2')

# **Exercício 5: Listar Arquivos em um Diretório** 

with os.scandir('C:/Users/aluno/Downloads/aula8/') as arquivos:
    for aula1 in arquivos:
      print('arquivo', aula1)
            
# **Exercício 6: Copiar Arquivos em um Diretório**

shutil.copytree('C:/Users/aluno/Downloads/aula8/pasta_teste', 'teste2')