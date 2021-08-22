# ImageToHTML
Another Terrible Idea

This is just another script in a long line of terrible ideas.

#Caution

This script generates HTML files that are absolutly huge.  Generating a large image has crashed Windows Explorer on me.  Reccomend disabling preview pane.
The test image I used when building this monstrosoty was 1300x1000 and it generated a file over 1.5 Million lines long and over 102 MB (near 30x the original image size).

Please use at your own risk.

#ToDo

Fix the RGB Alpha variable
  Currently images with/without the RGB aplha variable can break the script
  Removing / adding alpha to the variable declaration on line 33 can fix this if you would like to run it prior to the update (Why.... Why are you running this.)

#Requirements
Python 3
PIL
  python3 -m pip install --upgrade pip
  python3 -m pip install --upgrade Pillow
  
  
