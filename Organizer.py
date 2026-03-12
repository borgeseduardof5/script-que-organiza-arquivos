import os
import shutil

def organizar_pasta(caminho):
    arquivos = os.listdir(caminho)

    for arquivo in arquivos:
        caminho_completo = os.path.join(caminho, arquivo)

        if os.path.isfile(caminho_completo):
            extensao = arquivo.split(".")[-1]

            pasta_destino = os.path.join(caminho, extensao.upper())

            if not os.path.exists(pasta_destino):
                os.makedirs(pasta_destino)

            shutil.move(caminho_completo, os.path.join(pasta_destino, arquivo))

pasta  = input("Digite o caminho da pasta: ")
organizar_pasta(pasta)