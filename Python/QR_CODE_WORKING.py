# first run below commands on local machine to install the modules
#pip install pyqrcode
#pip install pypng

import pyqrcode 
from pyqrcode import QRCode 
import png
  
# String which represent the QR code 
# s = "https://www.youtube.com/channel/UCBz4yaxNxfiz1XYh-07UfWQ"
s="www.geeksforgeeks.org"
  
# Generate QR code 
url = pyqrcode.create(s) 
  
# Create and save the png file naming "myqr.png" 
url.png('myqr.png', scale = 6) 
