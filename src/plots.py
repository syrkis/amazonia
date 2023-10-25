# plots.py
#     neuroscope plots
# by: Noah Syrkis

# imports
import numpy as np
from IPython.display import display, clear_output
from IPython.display import display, HTML
import numpy as np
from jinja2 import Environment, FileSystemLoader
import darkdetect
from src.utils import matrix_to_image


# globals
env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('images.html')



def make_halves(pred_batch, target_batch):
    pred_batch, target_batch = np.array(pred_batch), np.array(target_batch)
    batch = np.zeros_like(pred_batch)
    batch[:, :, : pred_batch.shape[1] // 2, :] = pred_batch[:, :, : pred_batch.shape[1] // 2, :]
    batch[:, :, pred_batch.shape[1] // 2 :, :] = target_batch[:, :, pred_batch.shape[1] // 2 :, :]
    return batch



def plot_multiples(imgs, n=3, info_bar=None):
    imgs = np.array(imgs[:n])
    imgs = imgs if darkdetect.isDark() else 1 - imgs
    template = env.get_template('images.html')
    imgs = [matrix_to_image(pred) for pred in imgs]
    background = "dark" if darkdetect.isDark() else "white"
    
    html = template.render(images=imgs, n=n, info_bar=info_bar if info_bar else [""], background=background)
    clear_output(wait=True)
    display(HTML(html))