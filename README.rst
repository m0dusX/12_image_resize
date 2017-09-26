Image Resizer
-------------

[TODO. There will be project description]

How to use
-------------

Place image_resize.py somewhere. Then run command line, go to folder in which you moved script and execute it with desired parameters (see arguments section).

Example of script launch on Linux, Python 3.5::

    # $ python image_resize.py [optional_arguments] <path_to_original>

Arguments
-------------

*Positional arguments:*

``<path_to_original>``
    Path to original image

    
*Optional arguments:*
    
--height              new height of image
--width               new width of image
--scale               new scale of image
--output              output folder for converted file (without filename)

**IMPORTANT**: 1) --scale argument cannot be used with --height or --width arguments

**IMPORTANT**: 2) If --scale argument is not specified, either --height or --width argument is required
                      

Project Goals
-------------

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
