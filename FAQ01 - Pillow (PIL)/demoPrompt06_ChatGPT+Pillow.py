from PIL import Image

# Open the source image
source_image = Image.open("C:/Users/ASUS/Pillow+ChatGPT/cat3.jpg")

# Create a thumbnail with a specified size
thumbnail_size = (100, 100)  # Change to your desired thumbnail size
thumbnail = source_image.copy()  # Create a copy of the source image
thumbnail.thumbnail(thumbnail_size)

# Save the thumbnail
thumbnail.save("C:/Users/ASUS/Pillow+ChatGPT/cat3_thumbnail.jpg")
