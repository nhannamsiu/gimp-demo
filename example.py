from gimpfu import *

#gimp-console-2.8.exe -id --batch-interpreter python-fu-eval -b "import example; example.run(2)" -b "pdb.gimp_quit(1)"

#call gimp.exe to execute the python script
#python script must be written inside functions with at least 1 arg
#the true format of image cant be changed by just rename the extension, like a.jpg -> a.png

#for class members and method: https://www.gimp.org/docs/python/index.html

def run(a):
	inputName = r"C:\Users\User\Desktop\gimp-demo\a.jpg"
	layerPath = r"C:\Users\User\Desktop\gimp-demo\temp"
	outputPath = r"C:\Users\User\Desktop\gimp-demo\output"
	
	for i in range(1,a+1):
		layerName = layerPath + "\\" + str(i) + ".jpg"
		outputName = outputPath + "\\" + str(i) + ".jpg"
		#load image to create project
		image = pdb.file_jpeg_load(inputName, inputName)
		#load layer to project and add to image
		layer = pdb.gimp_file_load_layer(image, layerName)
		image.add_layer(layer)
	
		#set layer opacity
		pdb.gimp_layer_set_opacity(layer, 80)
		
		#transform perspective
		#top-left, top-right, btm-left, btm-right
		layer = pdb.gimp_item_transform_perspective(layer,82,55, 510,21,80,325, 510, 350)
		
		#create text layer
		textlayer = pdb.gimp_text_layer_new(image,"CN","Sans", 30, 0)
		#add to image
		image.add_layer(textlayer)
		#transform perspective
		#top-left, top-right, btm-left, btm-right
		textlayer = pdb.gimp_item_transform_perspective(textlayer,90,60,140,55,90,95, 140,95)
		
		
		#merge layer
		tosave = pdb.gimp_image_merge_visible_layers(image, 0)
		
		#save
		pdb.file_jpeg_save(image, tosave, outputName,outputName , "0.5",0,1,0,"",0,1,0,0)
	
	

	
	
