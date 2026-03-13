import os
import shutil
import sys

modo_simulacao = "--simular" in sys.argv

categorias = {
    "Imagens": ["png", "jpg", "jpeg", "gif"],
    "Documentos": ["pdf", "doc", "docx", "txt"],
    "Planilhas": ["xls", "xlsx", "csv"],
    "Videos": ["mp4", "mkv", "avi"],
    "Musicas": ["mp3", "wav"]
}

def organizar_pasta(caminho):

    if modo_simulacao:
        print("=== MODO SIMULAÇÃO ===")
        print("Nenhum arquivo será movido\n")

    arquivos = os.listdir(caminho)

    total_arquivos = len(arquivos)

    contador = 0

    for i, arquivo in enumerate(arquivos, start=1):

        caminho_completo = os.path.join(caminho, arquivo)

        if os.path.isfile(caminho_completo) and "." in arquivo: 

            extensao = arquivo.split(".")[-1].lower()

            pasta_destino = "Outros"

            for categoria, extensoes in categorias.items():

                if extensao in extensoes:
                    pasta_destino = categoria
                    break

            pasta_destino_path = os.path.join(caminho, pasta_destino)

            if not os.path.exists(pasta_destino_path):
                os.makedirs(pasta_destino_path)

            print(f"[{i}/{total_arquivos}] {arquivo} → {pasta_destino}")

            if not modo_simulacao:
                shutil.move(
                    caminho_completo,
                    os.path.join(pasta_destino_path, arquivo)
                )

                contador += 1

    print(f"\nArquivos organizados: {contador}")


pasta = input("Digite o caminho da pasta: ")
organizar_pasta(pasta)