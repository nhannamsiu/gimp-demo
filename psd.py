from gimpfu import *

#gimp-console-2.8.exe -idf --batch-interpreter python-fu-eval -b "import psd; psd.load(2)" -b "pdb.gimp_quit(1)"

#for class members and method: https://www.gimp.org/docs/python/index.html

def load(a):
	#prepare paths
	input = r'C:\Users\User\Desktop\gimp-demo\test.psd'
	layer = r"C:\Users\User\Desktop\gimp-demo\a.jpg"
	output = r'C:\Users\User\Desktop\gimp-demo\testout.psd'
	
	#load psd, layer
	image = pdb.file_psd_load(input, input)
	#print current layers
	pdb.gimp_message(image.layers)
	#add new layer to project
	layer = pdb.gimp_file_load_layer(image, layer)
	image.add_layer(layer)
	#print current layers
	pdb.gimp_message(image.layers)
	#save as new psd
	pdb.file_psd_save(image, image.active_layer, output, output, 0, 0)