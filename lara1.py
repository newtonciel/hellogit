import matplotlib.image as mpimg
from os import chdir

chemin=r'/home/ilyas/Téléchargements/eleve'
chdir(chemin)
image=mpimg.imread('canyon.png')

formatimage=image.shape
print(formatimage)
print(type(image))
print(image[0,0])
print(type(image[0,0]))
print('Proportion de rouge du premier pixel', image[0,0,0])
print('Proportion de vert du premier pixel', image[0,0,1])
print('Proportion de bleu du premier pixel', image[0,0,2])
