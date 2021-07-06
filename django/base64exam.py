import base64
from PIL import Image
from io import BytesIO

with open('./test2.jpg', 'rb') as img:
    base64_str = base64.b64encode(img.read())
    print(base64_str)
    img_str = base64.b64decode(base64_str)
    img = Image.open(BytesIO(img_str))
    
    img.show()