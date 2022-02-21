import os

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import seaborn as sns; sns.set()

#Part 1 this is the part that I used to get the classification of each of the access of an image so i have been able to load the image and convert each image to nd array
def generateimageurl(c):
    arrayofimgurls = []
    images = os.listdir(os.path.join(os.getcwd(), 'MNIST_DS/'+c))
    for img in images :
        arrayofimgurls.append(os.path.join(os.getcwd(), 'MNIST_DS/'+c, img))
    return arrayofimgurls


folderidentificationarray = ['0','1','2','3','4','5','6','7','8','9']
new_arr = []
for iden in folderidentificationarray:
    new_arr.append(generateimageurl(iden))
images_in_folder0 = new_arr[0]
images_in_folder1 = new_arr[1]
images_in_folder2 = new_arr[2]
images_in_folder3 = new_arr[3]
images_in_folder4 = new_arr[4]
images_in_folder5 = new_arr[5]
images_in_folder6 = new_arr[6]
images_in_folder7 = new_arr[7]
images_in_folder8 = new_arr[8]
images_in_folder9 = new_arr[9]


def open_image_and_covert_to_array(num):
    empty_array = []
    for imgurl in num:
        image = Image.open(imgurl)
        empty_array.append(np.asarray(image))
    return empty_array

converted0 = open_image_and_covert_to_array(images_in_folder0)
converted1 = open_image_and_covert_to_array(images_in_folder1)
converted2 = open_image_and_covert_to_array(images_in_folder2)
converted3 = open_image_and_covert_to_array(images_in_folder3)
converted4 = open_image_and_covert_to_array(images_in_folder4)
converted5 = open_image_and_covert_to_array(images_in_folder5)
converted6 = open_image_and_covert_to_array(images_in_folder6)
converted7 = open_image_and_covert_to_array(images_in_folder7)
converted8 = open_image_and_covert_to_array(images_in_folder8)
converted9 = open_image_and_covert_to_array(images_in_folder9)

#index 0-9 represents each individual image in each folder
print(converted9[7]) #This will be the first image in folder 0

# plt.imshow(arr, cmap='gray', vmin=0, vmax=255)
ax = sns.heatmap(converted4[3], annot=True, fmt="d")
plt.show()























#projections algorithm
#def getprojections(v,converted):
  #  convertion_array = []
  #  u = np.array(v)
   # for conv in converted:
    #    q= np.array(conv)

     #   try:

      #      projectionofconvonu = (np.dot(u,q)/ np.sqrt(sum(q**2))**2)*q
       #     convertion_array.append(projectionofconvonu)
      #  except(RuntimeWarning):
      #      continue


#x1 = getprojections(converted0[0],converted0)
