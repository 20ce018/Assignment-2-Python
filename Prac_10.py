# pip install PIL
from PIL import Image
#Path where image store
image_1=Image.open(r'D:\Studies\python\RESULT.png')
#converting into PDF
im_1=image_1.convert('RGB')
#Path where your pdf file will be save
im_1.save(r'D:\Studies\python\20CE018_Practical_10.pdf')
