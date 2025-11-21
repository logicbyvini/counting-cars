import cv2
import numpy as np
import supervision as sv

# --- CONFIGURAÇÕES ---
VIDEO_PATH = "../data/raw/traffic_video.mp4"
LINHA_X = 320  # Meio da tela (ajuste conforme sua necessidade)

def main():
    # 1. Inicializa Rastreador e Anotadores (Supervision)
    # ByteTrack vai manter o ID do quadrado vermelho enquanto ele se move
    tracker = sv.ByteTrack() 
    box_annotator = sv.BoxAnnotator()
    label_annotator = sv.LabelAnnotator()
    trace_annotator = sv.TraceAnnotator()

    # Memória para contagem manual
    memoria_x = {}
    cnt_in = 0
    cnt_out = 0

    # 2. Abre o vídeo
    cap = cv2.VideoCapture(VIDEO_PATH)
    if not cap.isOpened():
        print("Erro ao abrir vídeo.")
        return

    print("[INFO] Iniciando detecção por COR VERMELHA (Simulação)...")

    while True:
        ret, frame = cap.read()
        if not ret: break

        # --- A. DETECÇÃO POR COR (Substitui o YOLO) ---
        # Converte para HSV (melhor para detectar cores)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Define o intervalo da cor VERMELHA (no OpenCV o vermelho fica nas pontas 0-10 e 170-180)
        lower_red1 = np.array([0, 120, 70])
        upper_red1 = np.array([10, 255, 255])
        mask1 = cv2.inRange(hsv, lower_red1, upper_red1)

        lower_red2 = np.array([170, 120, 70])
        upper_red2 = np.array([180, 255, 255])
        mask2 = cv2.inRange(hsv, lower_red2, upper_red2)

        # Junta as máscaras
        mask = mask1 + mask2

        # Limpa ruídos (opcional)
        kernel = np.ones((3, 3), np.uint8)
        mask = cv2.erode(mask, kernel, iterations=1)
        mask = cv2.dilate(mask, kernel, iterations=2)

        # Encontra contornos (os quadrados vermelhos)
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        bboxes = []
        confidences = []
        class_ids = []

        for cnt in contours:
            # Filtra: ignora manchas muito pequenas (ruído)
            area = cv2.contourArea(cnt)
            if area > 500: 
                x, y, w, h = cv2.boundingRect(cnt)
                # Formato xyxy para o Supervision
                bboxes.append([x, y, x + w, y + h])
                confidences.append(0.99) # Confiança falsa alta, pois achamos a cor
                class_ids.append(0)      # ID 0 = "Carro Vermelho"

        # --- B. CRIA DETECÇÕES PARA O SUPERVISION ---
        if len(bboxes) > 0:
            detections = sv.Detections(
                xyxy=np.array(bboxes),
                confidence=np.array(confidences),
                class_id=np.array(class_ids)
            )
        else:
            detections = sv.Detections.empty()

        # --- C. RASTREAMENTO (ByteTrack) ---
        detections = tracker.update_with_detections(detections)

        # --- D. LÓGICA DE CONTAGEM (EIXO X) ---
        for tracker_id, bbox in zip(detections.tracker_id, detections.xyxy):
            x1, y1, x2, y2 = bbox
            cx = int((x1 + x2) / 2)
            cy = int((y1 + y2) / 2)

            # Verifica cruzamento
            if tracker_id in memoria_x:
                prev_cx = memoria_x[tracker_id]

                # Esquerda -> Direita
                if prev_cx < LINHA_X and cx >= LINHA_X:
                    cnt_out += 1
                    print(f"SAÍDA! Carro #{tracker_id}")
                    cv2.line(frame, (LINHA_X, 0), (LINHA_X, 700), (0, 255, 0), 5)
                
                # Direita -> Esquerda
                elif prev_cx > LINHA_X and cx <= LINHA_X:
                    cnt_in += 1
                    print(f"ENTRADA! Carro #{tracker_id}")
                    cv2.line(frame, (LINHA_X, 0), (LINHA_X, 700), (0, 255, 0), 5)

            memoria_x[tracker_id] = cx

        # --- E. DESENHO ---
        labels = [f"#{t_id}" for t_id in detections.tracker_id]
        
        frame = box_annotator.annotate(scene=frame, detections=detections)
        frame = label_annotator.annotate(scene=frame, detections=detections, labels=labels)
        frame = trace_annotator.annotate(scene=frame, detections=detections)

        # Linha de Chegada (Azul)
        cv2.line(frame, (LINHA_X, 0), (LINHA_X, 700), (255, 0, 0), 2)
        
        # Placar
        cv2.rectangle(frame, (0,0), (300, 60), (0,0,0), -1)
        cv2.putText(frame, f"IN: {cnt_in}  OUT: {cnt_out}", (20, 40), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        
        # Mostra também a máscara (visão preto e branco) para debug
        # cv2.imshow("Mascara (Visao do Computador)", mask) 
        cv2.imshow("Contador Final", frame)

        if cv2.waitKey(30) == 27: # 30ms de delay para não ficar rápido demais
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()