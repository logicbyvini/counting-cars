# 🚗 Car Counting with YOLOv8 + Object Tracking + OpenCV

This project demonstrates real-time **vehicle detection**, **tracking**, and **counting** using **YOLOv8**, **ByteTrack**, and **OpenCV**.

Cars are counted as they cross a virtual line in the video.

---

## 🔥 Features
- YOLOv8 object detection (cars, trucks, buses, motorcycles)
- ByteTrack multi-object tracking
- Line-crossing vehicle counter
- Real-time video processing
- Automatic CSV export with timestamps
- Output video with bounding boxes + IDs
- Fully modular codebase

---

## 📁 Project Structure
counting-cars/
│
├── src/                 # Código principal do projeto
│   ├── detector.py
│   ├── tracker.py
│   └── counter.py
│
├── models/              # Modelos YOLO, pesos treinados etc.
│
├── data/
│   ├── raw/             # Vídeos originais
│   └── processed/       # Frames, labels, datasets
│
├── notebooks/           # Jupyter para exploração
│
├── utils/               # Funções auxiliares
│   └── plotting.py
│
├── docs/                # Documentação, diagramas, explicações
│
├── deployments/         # Exportação para CoreML, ONNX, TensorRT
│
├── experiments/         # Testes, treinamentos, métricas
│
├── tests/               # Testes unitários
│
├── results/             # Gráficos e vídeos de saída
│
├── scripts/             # Scripts CLI (ex: processar vídeo)
│
├── requirements.txt     # Dependências
├── .gitignore
└── README.md

