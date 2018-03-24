1. add C:\Program Files\GIMP 2\bin to system path
2. copy example.py to C:\Program Files\GIMP 2\lib\gimp\2.0\plug-ins
3. open cmd, test if gimp-console is found:
	gimp-console-2.8.exe -v
4. Paste this folder to where you want, rename to gimp-demo
5. Open example.py in C:\Program Files\GIMP 2\lib\gimp\2.0\plug-ins to edit to your correct path:
	inputName = r"C:\Users\User\Desktop\gimp-demo\a.jpg"
	layerPath = r"C:\Users\User\Desktop\gimp-demo\temp"
	outputPath = r"C:\Users\User\Desktop\gimp-demo\output"
	
6. open cmd:
	gimp-console-2.8.exe -idf --batch-interpreter python-fu-eval -b "import example; example.run(2)" -b "pdb.gimp_quit(1)"

7. Check the result in gimp-demo\output