"""
Nessa aula será ensinado como mover, copiar e apagar arquivos.
"""
import os 
import shutil


#r'C:\Users\user\Desktop\Books2'
#input('Quais pastas devem ser verificadas? ')
caminho_origem = input('Quais pastas devem ser verificadas? ')
# caminho para onde será movido os arquivos. Caso não exista, será necessário criar.
caminho_destino = r'C:\Users\user\Desktop\Books'

# Tratar erros para criação de pasta.

try:
    # mkdir para criar um novo diretório
    os.mkdir(caminho_destino)
    print('Pasta criada com sucesso.')
except Exception as e:
    print('Erro ', e)
    pass 


for root, dir, files in os.walk(caminho_origem):
    for file in files: # vai percorrer todos os arquivos no caminho_origem
        #print(file)        
        old_file_path = os.path.join(root, file) # a ideia é juntar a raiz e os arquivos em um unico endereço
        #print(old_file_path)
        new_file_path = os.path.join(caminho_destino, file) # a ideia aqui é em um novo caminho, descompactar os arquivos do caminho_origem.
        #print(new_file_path)
        if '.pdf' in file:
            shutil.copy(old_file_path, new_file_path) # Vai mover old_file_path para o new_file_path
            #shutil.move(copia)
            print('Arquivos copiados com sucesso.')