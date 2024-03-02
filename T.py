from PIL import Image , ImageEnhance

#ex1
image = Image.open('C:\\Users\\ELITEBOOK\\Pictures\\ps\\pic1.jpg')
image.show()
image.save('img_trt.jpg')

#ex2
image_gray = image.convert('L')
image_gray.show()
image_gray.save('imgg_trt.jpg')

#ex3
image_resized = image.resize((1200, 1200))
image_resized.show()
image_resized.save('imgg_rz.jpg')

#ex4
image_rotated = image.rotate((-90))
image_rotated.show()
image_rotated.save('imgg_rt.jpg')

#ex5
image_brightened = ImageEnhance.Brightness(image).enhance(1.3)
image_brightened.show()
image_brightened.save('imgg_brgt.jpg')
