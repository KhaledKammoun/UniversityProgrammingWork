# how to import opencv-python
import cv2
import os
import numpy as np

# Question 1
def load_images(path):
    images = []
    for filename in os.listdir(path):
        # imread : permet de charger une image à partir d'un fichier.
        img = cv2.imread(os.path.join(path, filename))
        images.append(img)
    return images

# Question 2
def check_images(images):
    for img in images:
        if img.shape != (64,64):
            img = cv2.resize(img, (64,64))
    return images

def create_dataframe(images):
    data = []
    for img in images:
        data.append(img.reshape(1, -1))
    return data

# Question 3
def check_data(data):
    for img in data:
        if img.min() < 0 or img.max() > 255:
            print("Erreur de niveau de gris")
            return False
        else:
            return True
    return True

# Question 4
def min_max(data):
    for img in data:
        min_value = img.min()
        max_value = img.max()
        print(f"Min : {min_value} |  Max : {max_value}")
def check_gray_levels(data):
    for img in data:
        if img.min() < 0 or img.max() > 255:
            print("Erreur de niveau de gris")
            return False
        else:
            return True
    return True



# Question 1
images = load_images("AFD")
print(images)

# Question 2
new_images = check_images(images)
print("--------------")
print(new_images)

# Question 3
print("Check Data : ")
new_images_bool = check_data(new_images)
print(new_images_bool)

# Question 4
# call min_max and check_gray_levels
min_max(new_images)
check_gray_levels_var = check_gray_levels(new_images)
print(check_gray_levels_var)


# Stat Continue :
# mariam a obtenu un score de 940 a un test de réussite nationale, le score moyen au test etait de 850
# avec un ecart type de 100,
# quelle est la probabilité que plus que mariam
# ait obtenu un score de 940 ou plus ?

def normal_distribution(x, mu, sigma):
    return 1/(sigma * np.sqrt(2 * np.pi)) * np.exp(-(x - mu)**2 / (2 * sigma**2))
