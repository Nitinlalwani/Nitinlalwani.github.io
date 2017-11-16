from PIL import Image
import os, time

size_1024 = (1024, 1024)
size_512 = (512, 512)

for f in os.listdir('.'):
	if f.endswith('.jpg') or f.endswith('.jpeg') or f.endswith('.png'):
		i = Image.open(f)
		fn, fext = os.path.splitext(f)
		i.thumbnail(size_1024)
		i.save('fulls/{}.jpg'.format(fn))
		i.thumbnail(size_512)
		i.save('thumbs/{}.jpg'.format(fn))
		del i
		os.remove(f)
	


