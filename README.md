
# face-detection 
With help of open-cv and dlib detect the face in images  
# First need to install dlib for os (Windows 10)  
-> I have install it in conda enviroment, to make this installtaion please follow below steps:  
-->pip install cmake  
--> add cmake path to system environmental variable  
--> run conda install -c conda-forge dlib command (No need to install visual studio for cross platform things)  
--> once dlib install check it by running  
-->import dlib  
--> download pretrained facial landmark detector for dlib (http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2)  
--> extract pretrained detector and provide path of it in line 23 in detect_face.py  

-> install requirement.txt for other dependencies (Go to requirement.txt drive and run pip install - r requirement.txt)  
-> create input folder and put your input images (in  detect_face.py file line 25 provide input file path)  
-> create output folder (in  detect_face.py file line 25 provide output dir path)  
# Run main.py file and start detecting faces. (To run multiple images load all images in a loop)
# images
![alt text](https://github.com/nitintyagi-ai/face-detection/blob/master/input_images/Nitin.jpg?raw=true)![alt text](https://github.com/nitintyagi-ai/face-detection/blob/master/output/output.jpg?raw=true) 
![alt text](https://github.com/nitintyagi-ai/face-detection/blob/master/input_images/Nitin2.jpg?raw=true) ![alt text](https://github.com/nitintyagi-ai/face-detection/blob/master/output/output2.jpg?raw=true)
![alt text](https://github.com/nitintyagi-ai/face-detection/blob/master/input_images/Nitin3.jpg?raw=true) ![alt text](https://github.com/nitintyagi-ai/face-detection/blob/master/output/output3.jpg?raw=true)

