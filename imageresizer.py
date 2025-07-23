import cv2
import sys

source = "F:/ai/python/projects/photo.jpeg"
destination = "newimage.jpeg"
scale_percent = 50

src = cv2.imread(source, cv2.IMREAD_UNCHANGED)

if src is None:
    print(f"Error: Cannot read '{source}'. Check the file name and location.")
    sys.exit()

new_width = int(src.shape[1] * scale_percent / 100)
new_height = int(src.shape[0] * scale_percent / 100)

output = cv2.resize(src, (new_width, new_height))
cv2.imwrite(destination, output)
