import sys
import cv2
import numpy as np
from rembg import remove
from PIL import Image

def prep(input_path):
    print(f"Removendo fundo de {input_path}...")
    img = Image.open(input_path)
    img_no_bg = remove(img)
    img_cv = np.array(img_no_bg)
    if img_cv.shape[2] == 4:
        bgr = img_cv[:, :, :3]
        alpha = img_cv[:, :, 3]
    else:
        bgr = img_cv
        alpha = np.ones(bgr.shape[:2], dtype=np.uint8) * 255
    gray = cv2.cvtColor(bgr, cv2.COLOR_RGB2GRAY)
    print("Aplicando contraste adaptativo (CLAHE)...")
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    contrasted = clahe.apply(gray)
    final = np.where(alpha == 0, 255, contrasted)
    cv2.imwrite("source-prepped.png", final)
    print("Sucesso! source-prepped.png gerado na raiz.")

if __name__ == "__main__":
    prep(sys.argv[1])