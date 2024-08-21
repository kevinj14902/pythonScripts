from rembg import remove
from PIL import Image

#for input enter the name of your image
#for output name your new image
inputPath = 'input.jpg'
outputPath = 'output.png'

input = Image.open(inputPath)
output = remove(input)
output.save(outputPath)