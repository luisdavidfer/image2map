import subprocess
import sys
import math

# Process template with input parameters
def process_template(template, arguments):
    processed_template = template
    for arg in arguments:
        processed_template = processed_template.replace("{{arg}}", arg ,1)
    return processed_template

# Return template content
def read(filename):
    file = open(filename, "r")
    content = file.read()
    file.close()
    return content

# Write a file content
def write(filename, content):
    file = open(filename, "w")
    file.write(content)
    file.close()

# Checks input parameters

if len(sys.argv) > 1 and sys.argv[1] == "-h":
    print("Image2map is a Python 3 utility to generate Leaflet based  maps from plain images.")
    print("Required arguments:")
    print("$python3 image2map.py map_name image_path image_width image_height")
    print("Options and arguments (locate between Python file and arguments list):")
    print("-h   : List help, options and arguments.")
    print("-mp  : Execute multicore process mode (monocore by default)")
elif len(sys.argv) == 1 or len(sys.argv) < 5 or (len(sys.argv) > 5 and sys.argv[1] != "-mp") or (len(sys.argv) > 6 and sys.argv[1] == "-mp"):
    print("Invalid parameters. Read about use in official documentation or use -h for help.")
else:
    
    # Check process mode for parameters position

    # Monocore
    i = 1

    # Multicore
    if sys.argv[1] == "-mp":
        i = 2


    print("Generating HTML document:")
    
    # HTML data list
    htmlArgs = []
    htmlArgs.append(sys.argv[i])    # Map name
    
    # HTML making
    htmlTemplate = read("template.html")
    htmlProcessed = process_template(htmlTemplate, htmlArgs)
    write("index.html", htmlProcessed)

    print("done.")


    print("Generating JavaScript document:")

    # Max zoom equation: log2(max(width, height)/tilesize)
    defaultMaxZoom = math.ceil(math.log(max(int(sys.argv[i+2]), int(sys.argv[i+3]))/256) / math.log(2))

    # JS data list
    jsArgs = []
    jsArgs.append(str(defaultMaxZoom))  # Max zoom level
    jsArgs.append(sys.argv[i+2])        # Image width
    jsArgs.append(sys.argv[i+3])        # Image height
    
    # JavaScript 
    jsTemplate = read("template.js")
    jsProcessed = process_template(jsTemplate, jsArgs)
    write("index.js", jsProcessed)

    print("done.")


    # Map tiles

    image = sys.argv[i+1]   # Map image

    # Tiles making
    if i != 1:
        subprocess.run(["python3", "gdal2tiles-multiprocess.py", "-l", "-p", "raster", "-w", "none", image, "tiles"])
    else:
        subprocess.run(["python3", "gdal2tiles.py", "-l", "-p", "raster", "-w", "none", image, "tiles"])
