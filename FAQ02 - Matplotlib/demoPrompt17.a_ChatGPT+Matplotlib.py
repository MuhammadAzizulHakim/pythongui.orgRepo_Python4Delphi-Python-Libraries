import dearpygui.dearpygui as dpg
import matplotlib
matplotlib.use('Qt5Agg')  # Set the backend to Qt5Agg
from PyQt5 import QtCore, QtWidgets
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

def update_plot(sender, app_data):
    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    plt.figure(figsize=(4, 3))
    plt.plot(x, y, label='Sine Wave')
    plt.legend()
    plt.tight_layout()
    plt.savefig('plot.png')
    plt.close()

    image = Image.open('plot.png')
    dpg.set_value('texture', np.array(image))

dpg.create_context()
with dpg.texture_registry():
    dpg.add_dynamic_texture(width=400, height=300, default_value=np.zeros((400, 300, 4)), tag="texture")

with dpg.window(label="Matplotlib Plot"):
    dpg.add_button(label="Update Plot", callback=update_plot)
    dpg.add_image("texture")

dpg.create_viewport(title='DearPyGUI with Matplotlib', width=600, height=400)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
