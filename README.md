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

## 📂 Estrutura do Projeto

```plaintext
counting-cars/
│
├── 📂 src/                      # Código principal do projeto
│   ├── detector.py             # Lógica de detecção (YOLO)
│   ├── tracker.py              # Lógica de rastreamento
│   └── counter.py              # Lógica de contagem
│
├── 📂 models/                   # Modelos YOLO, pesos treinados (.pt)
│
├── 📂 data/                     # Dados do projeto
│   ├── 📂 raw/                  # Vídeos originais
│   └── 📂 processed/            # Frames processados, datasets
│
├── 📂 notebooks/                # Jupyter Notebooks para exploração/testes
│
├── 📂 utils/                    # Funções auxiliares e ferramentas
│   └── plotting.py             # Funções de plotagem gráfica
│
├── 📂 docs/                     # Documentação, diagramas e explicações
│
├── 📂 deployments/              # Exportação (CoreML, ONNX, TensorRT)
│
├── 📂 experiments/              # Logs de testes e treinamentos
│
├── 📂 tests/                    # Testes unitários (QA)
│
├── 📂 results/                  # Gráficos e vídeos de saída gerados
│
├── 📂 scripts/                  # Scripts CLI (ex: processar vídeo em lote)
│
├── 📄 requirements.txt          # Lista de dependências do Python
├── 📄 .gitignore                # Arquivos ignorados pelo Git
└── 📄 README.md                 # Documentação principal
