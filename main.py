import cv2
import numpy as np
import mediapipe as mp
import matplotlib.pyplot as plt

# TODO List:
# Make backgrounds auto-crop to fit the sample image (sample image and background image needs to be the same size)
# Create front-end of web application
#   1. Upload image of person, Upload background image, Replace Background button
#   2. 
# Deploy website
change_background_mp = mp.solutions.selfie_segmentation

change_bg_segment = change_background_mp.SelfieSegmentation()

sample_img = cv2.imread('media/sample.jpg')

plt.figure(figsize = [10, 10])

plt.title("Sample Image");plt.axis('off');plt.imshow(sample_img[:,:,::-1]);plt.show()

RGB_sample_img = cv2.cvtColor(sample_img, cv2.COLOR_BGR2RGB)

result = change_bg_segment.process(RGB_sample_img)

plt.figure(figsize=[22,22])
 
plt.subplot(121);plt.imshow(sample_img[:,:,::-1]);plt.title("Original Image");plt.axis('off')
plt.subplot(122);plt.imshow(result.segmentation_mask, cmap='gray');plt.title("Probability Map");plt.axis('off')

binary_mask = result.segmentation_mask > 0.9

plt.figure(figsize=[22,22])
plt.subplot(121);plt.imshow(sample_img[:,:,::-1]);plt.title("Original Image");plt.axis('off')
plt.subplot(122);plt.imshow(binary_mask, cmap='gray');plt.title("Binary Mask");plt.axis('off')

binary_mask_3 = np.dstack((binary_mask,binary_mask,binary_mask))

output_image = np.where(binary_mask_3, sample_img, 255)    

plt.figure(figsize=[22,22])
 
plt.subplot(121);plt.imshow(sample_img[:,:,::-1]);plt.title("Original Image");plt.axis('off')
plt.subplot(122);plt.imshow(output_image[:,:,::-1]);plt.title("Output Image");plt.axis('off')

bg_img = cv2.imread('media/background.jpg')

output_image = np.where(binary_mask_3, sample_img, bg_img)     

plt.figure(figsize=[22,22])
plt.subplot(131);plt.imshow(sample_img[:,:,::-1]);plt.title("Original Image");plt.axis('off')
plt.subplot(132);plt.imshow(binary_mask, cmap='gray');plt.title("Binary Mask");plt.axis('off')
plt.subplot(133);plt.imshow(output_image[:,:,::-1]);plt.title("Output Image");plt.axis('off')

plt.show()