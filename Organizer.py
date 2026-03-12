import os
import shutil

categorias = {
    "Imagens": ["png", "jpg", "jpeg", "gif"],
    "Documentos": ["pdf", "doc", "docx", "txt"],
    "Planilhas": ["xls", "xlsx", "csv"],
    "Videos": ["mp4", "mkv", "avi"],
    "Musicas": ["mp3", "wav"]
}

def organizar_pasta(caminho):

    arquivos = os.listdir(caminho)

    for arquivo in arquivos:

        caminho_completo = os.path.join(caminho, arquivo)

        if os.path.isfile(caminho_completo):

            extensao = arquivo.split(".")[-1].lower()

            pasta_destino = "Outros"

            for categoria, extensoes in categorias.items():

                if extensao in extensoes:
                    pasta_destino = categoria
                    break

            pasta_destino_path = os.path.join(caminho, pasta_destino)

            if not os.path.exists(pasta_destino_path):
                os.makedirs(pasta_destino_path)

            shutil.move(caminho_completo, os.path.join(pasta_destino_path, arquivo))


pasta = input("Digite o caminho da pasta: ")
organizar_pasta(pasta)