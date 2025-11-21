import os
import cv2
import sys

print("\n--- INICIO DO DIAGNOSTICO ---")

# 1. Verifica onde estamos
cwd = os.getcwd()
print(f"1. Pasta atual: {cwd}")

# 2. Verifica arquivos na pasta atual
print(f"2. Arquivos aqui dentro: {os.listdir('.')}")

# 3. Tenta achar o video
# Tenta subir um nivel (..) e entrar em data/raw
caminho_video = os.path.abspath(os.path.join(cwd, "..", "data", "raw", "traffic_video.mp4"))
print(f"3. Procurando video em: {caminho_video}")

if os.path.exists(caminho_video):
    print("   [OK] Video encontrado!")
else:
    print("   [ERRO] Video NAO encontrado.")
    # Tenta listar o que tem na pasta raw para ajudar
    try:
        pasta_raw = os.path.dirname(caminho_video)
        print(f"   Conteudo da pasta raw: {os.listdir(pasta_raw)}")
    except:
        print("   Nem a pasta 'raw' foi encontrada.")
    sys.exit()

# 4. Tenta abrir com OpenCV
cap = cv2.VideoCapture(caminho_video)
if not cap.isOpened():
    print("   [ERRO] OpenCV nao conseguiu abrir o arquivo (Codec/Corrompido).")
else:
    ret, frame = cap.read()
    if ret:
        print(f"   [SUCESSO] Video aberto! Resolucao: {frame.shape[1]}x{frame.shape[0]}")
        print("   Tentando abrir janela... (Se nao aparecer, verifique permissoes)")
        cv2.imshow("Teste Video", frame)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("   [ERRO] Video aberto mas frame vazio.")

print("--- FIM ---")
