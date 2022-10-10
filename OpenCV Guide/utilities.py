import numpy as np
import matplotlib.pyplot as plt

import cv2

def show_img(img, figsize: tuple = (12, 10), cmap: str="gray"):
    fig = plt.figure(figsize = figsize)
    ax = fig.add_subplot(111)
    ax.imshow(img, cmap=cmap)
    plt.show()
    
def load_img(img_path: str):
    img = cv2.imread(img_path).astype(np.float32) / 255
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img