from PIL import Image
 
img = Image.open("C:/Users/YOUR_USERNAME/cat1.jpg")
img = img.convert("RGB")
 
datas = img.getdata()
 
new_image_data = []
for item in datas:
    # Change all white (also shades of whites) pixels to yellow
    if item[0] in list(range(190, 256)):
        new_image_data.append((255, 204, 100))
    else:
        new_image_data.append(item)
        
# Update image data
img.putdata(new_image_data)
 
# Save new image
img.save("cat1_alteredBackground.jpg")
 
# Show image in preview
img.show()