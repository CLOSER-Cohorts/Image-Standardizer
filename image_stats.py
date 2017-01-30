import fnmatch
import os
from PIL import Image

#It takes a while to run- is there a way to make is more efficient?

images = ['*.jpg', '*.jpeg', '*.png', '*.tif', '*.tiff']
image_files = []
fix = []
excludes = "index_files"

for root, dirnames, filenames in os.walk("M:\\bundles"):
     for extensions in images:
         if excludes in root:
                 break
         else:
             for filename in fnmatch.filter(filenames, extensions):
                 image_files.append(os.path.join(root, filename))
                 if "images" not in root:
                     fix.append(root)
#print image_files

j=0
p=0
n=0
t=0

for image in image_files:
     n+=1
     if 'PNG' in image:
         p+=1
     if "JPG" in image or 'jpg' in image or 'jpeg' in image or 'JPEG' in image: #how can I take into account the case?
         j+=1
     if 'tiff' in image or 'TIFF' in image or 'TIF' in image or 'tif' in image:
         t+=1
print "There are " +str(n) + " images."
print "There are " + str(j) + " JPG images, " + str(p) + " PNG images and " + str(t) + " TIFF images."
print "Directories which need fixing are " +str(list(set(fix)))

def image_size(image):
    im = Image.open(image)
    width, height = im.size
    print im.size
    print width*height

image_size("qc_1.PNG")