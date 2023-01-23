from pyzbar.pyzbar import decode;
from PIL import Image;

#decode qrcode

img = Image.open("2.png");

result = decode(img);
print(result)
#5mins 09/05/2022