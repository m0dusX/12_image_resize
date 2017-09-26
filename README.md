Image Resizer
-------------

This script resizes image according to input arguments, which can contain width, height or scale of new image. 

How to use
-------------

Place image_resize.py somewhere. Then run command line, go to folder in which you moved script and execute it with desired parameters (see arguments section).

Example of script launch on Linux, Python 3.5::

```#!bash

$ python image_resize.py [optional_arguments] <path_to_original>

```

Arguments
-------------

*Positional arguments:*

| Argument           | Description            |
|--------------------|------------------------|
| <path_to_original> | path to original image |
    
*Optional arguments:*
    
| Argument | Description                                         |
|----------|-----------------------------------------------------|
| --height | new height of image                                 |
| --width  | new width of image                                  |
| --scale  | new scale of image                                  |
| --output | output folder for converted file (without filename) |

**IMPORTANT**: 1) --scale argument cannot be specified together with --height or --width arguments

**IMPORTANT**: 2) if --scale argument is not specified, either --height or --width argument is required

**IMPORTANT**: 3) if --output argument is not specified, converted image will be created in folder containing input image                     

Project Goals
-------------

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
