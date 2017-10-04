Image Resizer
-------------

This script resizes image according to input arguments, which can contain width, height or scale of new image and then saves converted image to specified (or not) output folder. New filename is composed following this pattern: 

**[original_name]__[new_width]x[new_height].[original_format]**

Works with all known image formats.

How to use
-------------

Place image_resize.py somewhere. Then run command line, go to folder in which you moved script and execute it with desired parameters (see arguments section).

Example of script launch on Linux, Python 3.5::

```#!bash

$ python image_resize.py [optional_arguments] <path_to_original>

```

Output data example:

```#!bash

Image was successfully converted! Check D:\books\pic__3900x1300.jpeg

```

Arguments
-------------

*Positional arguments:*

| Argument           | Type | Description            |
|--------------------|------|------------------------|
| <path_to_original> | str  | path to original image |
    
*Optional arguments:*
    
| Argument | Type | Description                                         |
|----------|------|-----------------------------------------------------|
| --height | int  | new height of image                                 |
| --width  | int  | new width of image                                  |
| --scale  | int  | new scale of image                                  |
| --output | str  | output folder for converted file (without filename) ||

**IMPORTANT**: 1) --scale argument cannot be specified together with --height or/and --width arguments

**IMPORTANT**: 2) if --scale argument is not specified, either --height or --width argument is required

**IMPORTANT**: 3) if --output argument is not specified, converted image will be created in folder containing input image 

Project Goals
-------------

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
