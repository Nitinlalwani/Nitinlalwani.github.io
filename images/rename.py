import os

i = 1
for f in os.listdir('.'):
	if f.endswith('.jpg') or f.endswith('.jpeg') or f.endswith('.png'):
		fn, fext = os.path.splitext(f)
		newname = str(i) + '.jpg'
		os.rename(f, newname)		
		i += 1