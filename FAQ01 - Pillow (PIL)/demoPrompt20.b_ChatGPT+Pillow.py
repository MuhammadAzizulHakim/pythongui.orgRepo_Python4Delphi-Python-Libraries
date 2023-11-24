from pandasgui import show
import pandas as pd
from PIL import Image
from io import BytesIO

# Create a sample DataFrame with image paths
data = {
    'Name': ['Image 1', 'Image 2'],
    'ImagePath': ['C:/Users/ASUS/Pillow+ChatGPT/cat3_small.jpg', 'C:/Users/ASUS/Pillow+ChatGPT/cat4_small.jpg']
}
df = pd.DataFrame(data)

# Function to open and display an image using Pillow
def show_image(row):
    image_path = row['ImagePath']
    pil_image = Image.open(image_path)
    pil_image.show()

# Add a column with a button to open the associated image
df['View Image'] = df.apply(lambda row: show_image(row), axis=1)

# Display the DataFrame using pandasgui
show()
gui = show(df)
