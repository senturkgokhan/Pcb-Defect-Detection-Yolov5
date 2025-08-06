import subprocess
from datetime import datetime
import os

IMG_SIZE = 640
BATCH_SIZE = 16
EPOCHS = 200
WEIGHTS = "yolov5n.pt" 
DATA_YAML_PATH = os.path.join("dataset", "data.yaml")  
TRAIN_PY_PATH = os.path.join("yolov5", "train.py")

# Model ismi zaman damgalı
MODEL_NAME = "pcb_train_" + datetime.now().strftime("%Y%m%d_%H%M")

# Komutun hazırlanması
command = [
    "python", TRAIN_PY_PATH,
    "--img", str(IMG_SIZE),
    "--batch", str(BATCH_SIZE),
    "--epochs", str(EPOCHS),
    "--patience", "20",
    "--data", DATA_YAML_PATH,
    "--weights", WEIGHTS,
    "--name", MODEL_NAME
]

print("\n Eğitim başlatılıyor...\n")
result = subprocess.run(command)

if result.returncode == 0:
    print(f"\n Eğitim başarıyla tamamlandı. Model ismi: {MODEL_NAME}")
else:
    print(f"\n Hata oluştu. Kod: {result.returncode}")
