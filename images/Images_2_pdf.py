import img2pdf 
from PIL import Image 
import os 
  
# storing image path 
images = ["x.jpg", "y.jpg", "z.jpg", "apple-touch-icon.png"]
pdf_path = "file.pdf"
with open("name.pdf","wb") as f:
	f.write(img2pdf.convert(images))
  
# storing pdf path 


# for img_path in images :    
# # opening image 
# 	file = open(pdf_path, "ab") 
# 	image = Image.open(img_path) 
 

# # converting into chunks using img2pdf 
# 	pdf_bytes = img2pdf.convert(image.filename) 
  
# # opening or creating pdf file 
	
  
# # writing pdf files with chunks 
# 	file.write(pdf_bytes) 
  
# # closing image file 
# 	image.close() 
  
# # closing pdf file 
# file.close() 
  
# output 
print("Successfully made pdf file") 