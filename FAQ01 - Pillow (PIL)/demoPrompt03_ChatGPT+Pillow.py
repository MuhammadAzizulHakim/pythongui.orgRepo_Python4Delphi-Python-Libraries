from PIL import Image, ImageDraw, ImageFilter

# Open an image
image = Image.open('C:/Users/ASUS/cat1.jpg')

# Resize the image
image = image.resize((800, 600))

# Crop a portion of the image
image = image.crop((100, 100, 700, 500))

# Rotate the image
image = image.rotate(90)

# Apply a Gaussian blur filter
image = image.filter(ImageFilter.GaussianBlur(radius=5))

# Convert the image to grayscale
image = image.convert('L') # 'L' mode represents grayscale

# Draw text on the image
draw = ImageDraw.Draw(image)
draw.text((50, 50), 'Pillow Example (Ft. ChatGPT)', fill='white')

# Save the manipulated image
image.save('C:/Users/ASUS/cat1_output.jpg')
