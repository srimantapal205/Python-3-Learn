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

print(dir(img))
