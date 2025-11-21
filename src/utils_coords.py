import cv2

# Variável global para armazenar os pontos
points = []

def get_coordinates(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"📍 Ponto clicado: ({x}, {y})")
        points.append((x, y))

def main():
    # Ajuste o caminho do vídeo se necessário
    VIDEO_PATH = "../data/raw/traffic_video.mp4"
    
    cap = cv2.VideoCapture(VIDEO_PATH)
    
    if not cap.isOpened():
        print(f"Erro ao abrir o vídeo em: {VIDEO_PATH}")
        print("Verifique se o arquivo existe na pasta 'data/raw'.")
        return

    # Lê o primeiro frame para usarmos de referência
    ret, frame = cap.read()
    
    if ret:
        print("\n--- INSTRUÇÕES ---")
        print("1. Clique no INÍCIO da linha imaginária.")
        print("2. Clique no FIM da linha imaginária.")
        print("3. Olhe o terminal para ver as coordenadas.")
        print("4. Pressione qualquer tecla na janela da imagem para sair.\n")

        cv2.namedWindow("Pegar Coordenadas")
        cv2.setMouseCallback("Pegar Coordenadas", get_coordinates)
        
        while True:
            # Mostra os pontos clicados no frame
            for pt in points:
                cv2.circle(frame, pt, 5, (0, 0, 255), -1)
                
            cv2.imshow("Pegar Coordenadas", frame)
            
            # Sai se apertar qualquer tecla
            if cv2.waitKey(1) != -1:
                break
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
