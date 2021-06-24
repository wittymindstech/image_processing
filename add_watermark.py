#Import required Image library
from PIL import Image, ImageDraw, ImageFont

#Create an Image Object from an Image
im = Image.open('images/boy.jpg')
width, height = im.size

draw = ImageDraw.Draw(im)
text = "sample watermark"
#Download ttf from https://github.com/JotJunior/PHP-Boleto-ZF2/blob/master/public/assets/fonts/arial.ttf
font = ImageFont.truetype('arial.ttf', 36)
textwidth, textheight = draw.textsize(text, font)

# calculate the x,y coordinates of the text
margin = 10
x = width - textwidth - margin
y = height - textheight - margin

# draw watermark in the bottom right corner
draw.text((x, y), text, font=font)
im.show()

#Save watermarked image

rgb_im = im.convert('RGB')
rgb_im.save('audacious.jpg')
#im.save('images/watermark.jpg')
