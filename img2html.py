from PIL import Image,ImageDraw,ImageFont
import sys

file = sys.argv[1]
outfile = sys.argv[2]

image = Image.open(file)
sizeW,sizeH = image.size
pixels = image.load()

preHTML = """<!DOCTYPE html>
<html>
	<head>
		<style>
			.row { width: %dpx; height: 1px}
			.pixel {width: 1px; height: 1px; float:left;}
		</style>
	</head>
	<body>
"""%sizeW

closeHTML = """
	</body>
</html>
"""

file = open(outfile + ".html", "a")
file.write(preHTML)

for i in range(sizeH):
	file.write("\t<div class=\"row\">\n\t")
	for j in range(sizeW):
		red, green, blue = image.getpixel((j,i))
		pixelHTML = "<div class=\"pixel\" style=\"background-color: rgb(%d, %d, %d)\"></div>\n\t"%(red, green, blue)
		file.write(pixelHTML)
	file.write("</div>")

file.write(closeHTML)