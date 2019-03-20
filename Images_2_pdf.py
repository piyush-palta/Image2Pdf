import img2pdf 
from PIL import Image 
import os 
  
# storing images path 
images = ["images/x.jpg", "images/y.jpg", "images/z.jpg", "images/apple-touch-icon.png"]   

#put pdf path here
pdf_path = "file.pdf"

#Writing images to file after converting them to binary
with open(pdf_path,"wb") as f:
	f.write(img2pdf.convert(images))

# Success 
print("Success!!") 