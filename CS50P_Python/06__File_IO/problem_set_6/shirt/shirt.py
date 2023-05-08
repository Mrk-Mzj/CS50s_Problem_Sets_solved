"""
https://cs50.harvard.edu/python/2022/psets/6/shirt/


Implement a program that expects exactly two command-line arguments:

- in sys.argv[1], the name (or path) of a JPEG or PNG to read (i.e., open) as input
- in sys.argv[2], the name (or path) of a JPEG or PNG to write (i.e., save) as output


The program should then overlay shirt.png (which has a transparent background) on the input 
after resizing and cropping the input to be the same size, saving the result as its output.

- Open the input with Image.open, per https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.open, 
- resize and crop the input with ImageOps.fit, per https://pillow.readthedocs.io/en/stable/reference/ImageOps.html#PIL.ImageOps.fit, 
  using default values for method, bleed, and centering, 
- overlay the shirt with Image.paste, per https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.paste, 
- save the result with Image.save, per https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.save.


The program should instead exit via sys.exit:

- if the user does not specify exactly two command-line arguments,
- if the input’s and output’s names do not end in .jpg, .jpeg, or .png, case-insensitively,
- if the input’s name does not have the same extension as the output’s name, or
- if the specified input does not exist.
"""
# pip install --upgrade pip
# pip install Pillow --upgrade

# python CS50P_Python/06__File_IO/problem_set_6/shirt/shirt.py before1.jpg after1.jpg


import sys, os.path, PIL.ImageOps, PIL.Image


PATH = "CS50P_Python/06__File_IO/problem_set_6/shirt/"
EXTENSIONS = ("jpg", "jpeg", "png")


# checking if user specified 2 arguments,
# ending with identical extensions
# valid extensions,
# and if input file exists
if (
    len(sys.argv) != 3
    or not sys.argv[1].split(".")[1].lower() == sys.argv[2].split(".")[1].lower()
    or not sys.argv[1].lower().endswith(EXTENSIONS)
    or not os.path.isfile(PATH + sys.argv[1])
):
    sys.exit(
        "\nYou must add valid input jpg / jpeg / png file as the 1st parameter, and output file as the 2nd parameter"
    )

# open input and overlay images
img_input = PIL.Image.open(PATH + sys.argv[1], mode="r", formats=None)
img_overlay = PIL.Image.open(PATH + "shirt.png", mode="r", formats=None)

# resize and crop input to shirt.py size
img_processed = PIL.ImageOps.fit(
    img_input, (600, 600), method=PIL.Image.Resampling.BICUBIC, bleed=0.0, centering=(0.5, 0.5)
)
# overlay
img_processed.paste(img_overlay, box=None, mask=img_overlay)

# save output and show the result
img_processed.save(PATH + sys.argv[2])
img_processed.show()