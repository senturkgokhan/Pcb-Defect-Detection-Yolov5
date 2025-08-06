import subprocess
import os

# Ayarlar
WEIGHTS_PATH = os.path.join("runs", "train", "pcb_train_YYYYMMDD_HHMM", "weights", "best.pt")  # Eğitim sonrası oluşan model
TEST_IMAGE_PATH = os.path.join("sample_inputs", "example_test.jpg")  # Örnek görsel yolu
DETECT_PY_PATH = os.path.join("yolov5", "detect.py")

command = [
    "python", DETECT_PY_PATH,
    "--weights", WEIGHTS_PATH,
    "--img", "640",
    "--conf", "0.25",
    "--source", TEST_IMAGE_PATH
]

print("\n İnference başlatılıyor...\n")
result = subprocess.run(command)

if result.returncode == 0:
    print("\n İnference tamamlandı. Çıktılar 'runs/detect/' klasöründe.")
else:
    print(f"\n Hata oluştu. Kod: {result.returncode}")
