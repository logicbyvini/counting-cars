from ultralytics import YOLO
import cv2

class YoloDetector:
    def __init__(self, model_path="yolov8n.pt", device="cpu"):
        """
        Inicializa o detector YOLO.
        """
        self.model = YOLO(model_path)
        self.device = device
        print(f"[INFO] YOLO carregado em {device}")

    def detect(self, frame):
        """
        Roda detecção no frame.
        """
        results = self.model(frame, stream=True)
        detections = []

        for r in results:
            for box in r.boxes:
                x1, y1, x2, y2 = box.xyxy[0]
                cls = int(box.cls[0])
                conf = float(box.conf[0])
                label = self.model.names[cls]

                detections.append({
                    "bbox": (int(x1), int(y1), int(x2), int(y2)),
                    "label": label,
                    "confidence": conf
                })

        return detections

    def draw(self, frame, detections):
        """
        Desenha caixas e labels no frame.
        """
        for det in detections:
            x1, y1, x2, y2 = det["bbox"]
            label = det["label"]
            conf = det["confidence"]

            cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)
            cv2.putText(frame, f"{label} {conf:.2f}", (x1, y1 - 5),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)

        return frame

