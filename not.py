import cv2
import numpy as np

# 마스크 이미지를 흑백 이미지로 읽어옴
mask = cv2.imread('C:/Users/MMC/Places2/test_fin/mask/mask!.png', cv2.IMREAD_GRAYSCALE)

# 255 값을 0으로, 0 값을 255로 바꿔줌
modified_mask = np.where(mask == 255, 0, np.where(mask == 0, 255, mask))

# 수정된 마스크 이미지 저장
cv2.imwrite('C:/Users/MMC/Places2/test_fin/mask/modified_mask.png', modified_mask)
