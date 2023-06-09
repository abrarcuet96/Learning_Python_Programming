from PIL import Image, ImageEnhance, ImageFilter
import os

# image format change:
img1=Image.open('IMG_20200201_161209.jpg')
# img1.save('IMG_20200201_161209.png')

# to show image:
# img1.show('IMG_20200201_161209.jpg')

# resize image:
# max_size= (250,250)
# img1.thumbnail(max_size)
# img1.save('small_image.jpg')
# img1.show('small_image.jpg')

# to convert all images extension altogether:
# for item in os.listdir():
#     if item.endswith('.jpg'):
#         img1=Image.open(item)
#         filename,extension=os.path.splitext(item)
#         img1.save(f'{filename}.png')

# SHARPNESS:
# enhancer=ImageEnhance.Sharpness(img1)
# 0--> blury
# 1--> original image
# 2,3,4... --> sharp image
# enhancer.enhance(4).save('editedImage.jpg')
# img1.show('editedImage.jpg')

# COLOR:
# img1=Image.open('20200131_155401.jpg')
# enhancer=ImageEnhance.Color(img1)
# enhancer.enhance(10).save('editedImage2.jpg')
# img1.show('editedImage2.jpg')

# BRIGHTNESS:
# img1=Image.open('20200131_155401.jpg')
# enhancer=ImageEnhance.Brightness(img1)
# enhancer.enhance(3).save('editedImage2.jpg')
# img1.show('editedImage2.jpg')

# using Filter:
img1.filter(ImageFilter.GaussianBlur()).save('filtered_img.jpg')