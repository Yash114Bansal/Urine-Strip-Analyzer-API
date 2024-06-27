import cv2
import numpy as np


def analyze_urine_strip(image):
    nparr = np.frombuffer(image.read(), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    height = img.shape[0]
    box_height = height // 10
    colors = []

    for i in range(10):
        box = img[i * box_height : (i + 1) * box_height, :]
        avg_color = cv2.mean(box)[:3]
        colors.append([int(c) for c in avg_color])

    return {
        "URO": colors[0],
        "BIL": colors[1],
        "KET": colors[2],
        "BLD": colors[3],
        "PRO": colors[4],
        "NIT": colors[5],
        "LEU": colors[6],
        "GLU": colors[7],
        "SG": colors[8],
        "PH": colors[9],
    }