import argparse
import sys
from PIL import Image
import os

def get_new_dimensions(new_image, original_width, original_height):
    if "scale" in new_image:
        scale = new_image["scale"]
        new_width = width * scale
        new_height = height * scale
    else:
        if "height" in new_image and "width" in new_image:
            new_height = new_image["height"]
            new_width = new_image["width"]
            ratio = original_width / new_width
            if new_height != original_height / ratio:
                print('Aspect ratio of new image does not match the original!\n')
        elif "height" in new_image and "width" not in new_image:
            new_height = new_image["height"]
            new_width  = int(new_height * original_width / original_height)
        elif "width" in new_image and "height" not in new_image:
            new_width = new_image["width"]
            new_height = int(new_width * original_height / original_width)
    return new_width, new_height

def resize_image(new_image):
    input_image = new_image["path_to_original"]
    filename = os.path.basename(input_image)
    dirname = os.path.dirname(input_image)
    img = Image.open(input_image)
    width, height = img.size
    new_width, new_height = get_new_dimensions(new_image, width, height)
    img = img.resize((new_width, new_height), Image.ANTIALIAS)
    if "output" in new_image:
        ouput_folder = new_image["output"]
        output_path = os.path.join(ouput_folder, filename)
        img.save(output_path)
    else:
        filename_splitted = filename.split(".")
        output_path = os.path.join(dirname, 
            "{}__{}x{}.{}".format(filename_splitted[0], 
                new_width, new_height, filename_splitted[1]))
        img.save(output_path)
    return output_path

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Image Resizer", 
        formatter_class=argparse.MetavarTypeHelpFormatter)
    parser.add_argument("path_to_original",
        help="path to original file", type=str)
    parser.add_argument("--width", 
        help="new width of image", type=int)
    parser.add_argument("--height", 
        help="new height of image", type=int)
    parser.add_argument("--scale", 
        help="new scale of image", type=int)
    parser.add_argument("--output", 
        help="output folder for converted file (without filename)", type=str)
    args = parser.parse_args()
    if not (args.height or args.width):
            parser.error('Either --height or --width argument is required')
    if args.scale and (args.height or args.width):
        parser.error('--scale argument cannot be used with --height or --width arguments')
    #Create new dict with parsed parameters representing our new resized image 
    #(excluding those which have None value)
    new_image = {key: value for (key, value) in vars(args).items() if vars(args)[key] is not None}
    converted_image = resize_image(new_image)
    print("Image was successfully converted! Check {}".format(converted_image))
    sys.exit()
