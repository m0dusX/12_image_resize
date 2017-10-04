import argparse
import sys
from PIL import Image
import os


def print_caution():
    print('Aspect ratio of new image does not match the original!\n')


def get_new_dimensions(new_image, original_width, original_height):
    if new_image['scale'] is not None:
        scale = new_image['scale']
        new_width = width * scale
        new_height = height * scale
    else:
        if new_image['height'] is not None and new_image['width'] is not None:
            new_height = new_image['height']
            new_width = new_image['width']
            ratio = original_width / new_width
            if new_height != original_height / ratio:
                print_caution()
        elif new_image['height'] is not None:
            new_height = new_image['height']
            new_width = int(new_height * original_width / original_height)
        elif new_image['width'] is not None:
            new_width = new_image['width']
            new_height = int(new_width * original_height / original_width)
    return new_width, new_height


def read_image(filepath):
    img = Image.open(filepath)
    return img


def save_image(new_location, new_width, new_height, img):
    filename_splitted = new_location['filename'].split('.')
    new_filename = '{}__{}x{}.{}'.format(filename_splitted[0],
                                         new_width, new_height,
                                         filename_splitted[1])
    if new_location['output'] is not None:
        ouput_folder = new_location['output']
        output_path = os.path.join(ouput_folder, new_filename)
        img.save(output_path)
    else:
        output_path = os.path.join(new_location['dirname'], new_filename)
        img.save(output_path)
    return output_path


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Image Resizer')
    parser.add_argument('path_to_original', help='path to file', type=str)
    parser.add_argument('--width', help='new width of image', type=int)
    parser.add_argument('--height', help='new height of image', type=int)
    parser.add_argument('--scale', help='new scale of image', type=int)
    parser.add_argument('--output', help='output folder for converted ' +
                        'file (without filename)', type=str)
    args = parser.parse_args()
    if not (args.height or args.width) and not args.scale:
            parser.error('Either --height or --width argument is required')
    if args.scale and (args.height or args.width):
        parser.error('--scale argument cannot be used with ' +
                     '--height or --width arguments')
    input_image = args.path_to_original
    new_image_dimensions = {
        'scale': args.scale,
        'width': args.width,
        'height': args.height,
        }
    new_image_location = {
        'filename': os.path.basename(input_image),
        'dirname': os.path.dirname(input_image),
        'output': args.output,
    }
    original_image = read_image(input_image)
    width, height = original_image.size
    new_width, new_height = get_new_dimensions(new_image_dimensions,
                                               width, height)
    converted_image = original_image.resize((new_width, new_height),
                                            Image.ANTIALIAS)
    converted_path = save_image(new_image_location, new_width,
                                new_height, converted_image)
    print('Image was successfully converted! Check {}'.format(converted_path))
    sys.exit()
