Image Resizer
-------------

[TODO. There will be project description]

How to use
-------------

Place image_resize.py somewhere. Then run command line, go to folder in which you moved script and execute it with desired parameters.

``$ python image_resize.py [optional_arguments] <path_to_original_image>``
    Create a new resized image named accordingly to filename from *<path_to_original_image>*. 

    ``image_resize.py`` optional arguments:
    
      --height              new height of image
      --width               new width of image
      --scale               new scale of image
                            --scale argument cannot be used with --height or --width arguments
      --output              output folder for converted file (without filename)
                            if 

    any other options are passed on to the ``virtualenv`` command.	

Project Goals
-------------

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
