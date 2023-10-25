# utils.py
#   neuroscope project
# by: Noah Syrkis


# imports
import numpy as np
import numpy as np
import base64
from PIL import Image as PILImage
from io import BytesIO


# functions
def matrix_to_image(matrix):
        # ensure all values are [0; 1]
        matrix = np.clip(matrix, 0, 1)
        # if matrix is 128 x 128 x 1, convert to 128 x 128 x 3
        matrix = np.repeat(matrix, 3, axis=2) if matrix.shape[2] == 1 else matrix
        image = PILImage.fromarray((matrix * 255).astype(np.uint8))
        image_bytes = BytesIO()
        image.save(image_bytes, format='png')
        encoded_image = base64.b64encode(image_bytes.getvalue()).decode('utf-8')
        return encoded_image

