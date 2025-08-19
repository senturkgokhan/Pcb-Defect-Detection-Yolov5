import subprocess
from datetime import datetime   

# Parametreler
IMG_SIZE = 640
BATCH_SIZE = 16
EPOCHS = 200
WEIGHTS = "yolov5n.pt"
MODEL_NAME = "Pcb_Train_" + datetime.now().strftime("_%Y%m%d_%H%M")
DATA_YAML_PATH = "C:/Users/sentu/OneDrive/Desktop/Pcb_Dataset/data.yaml"
TRAIN_PY_PATH = "C:/Users/sentu/OneDrive/Desktop/Yolov5/yolov5/train.py"

# Eğitim komutu
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

print("\n Eğitim başlatılıyor.\n")
result = subprocess.run(command)

if result.returncode == 0:
    print("\n Eğitim tamamlandı.")
else:
    print(f"\n Hata oluştu. Kod: {result.returncode}")