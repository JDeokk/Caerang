import cv2
import numpy as np

mask = cv2.imread('C:/Users/MMC/Places2/test_fin/mask/mask_0.png', cv2.IMREAD_GRAYSCALE)  # 흑백 이미지로 읽어옴
mask[mask == 0] = 255
mask[np.logical_and(mask != 0, mask != 255)] = 0
cv2.imwrite('C:/Users/MMC/Places2/test_fin/mask/mask!.png', mask)