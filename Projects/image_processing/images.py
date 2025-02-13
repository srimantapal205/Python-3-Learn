from PIL import Image, ImageFilter

img = Image.open('./data/original_image/pikachu.jpg')
print(img)
print(img.format, img.size, img.mode)

blur_filterd_Image = img.filter(ImageFilter.BLUR)
blur_filterd_Image.save("./data/processed_image/pikachu_blur.png", "png")

smooth_filterd_Image = img.filter(ImageFilter.SMOOTH)
smooth_filterd_Image.save("./data/processed_image/pikachu_smooth.png", "png")

sharpen_filterd_Image = img.filter(ImageFilter.SHARPEN)
sharpen_filterd_Image.save("./data/processed_image/pikachu_sharpen.png", "png")


gray_filterd_image = img.convert('L')
gray_filterd_image.save("./data/processed_image/pikachu_grayscale.png", "png")

rotateImage = gray_filterd_image.rotate(90)
rotateImage.save("./data/processed_image/pikachu_grayscale_90Rotate.png", "png")

resizeImage = gray_filterd_image.resize((300, 300))
resizeImage.save("./data/processed_image/pikachu_grayscale_resize.png", "png")

boxSize = (100,100,400,400)
cropImages = gray_filterd_image.crop(boxSize)
cropImages.save("./data/processed_image/pikachu_grayscale_crop.png", "png")
print(dir(img))

astroImg = Image.open('./data/original_image/astro.jpg')
print(astroImg)

profileImage = astroImg.resize((400, 400))
profileImage.save("./data/processed_image/profile_astroImage.png", "png")
print(profileImage)

thumbnailImage = Image.open('./data/original_image/astro.jpg')
thumbnailImage.thumbnail((400,200))
thumbnailImage.save("./data/processed_image/thumbnailImage_astroImage.png", "png")
print(thumbnailImage)



