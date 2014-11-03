from icns_info import *
from image_utils import Image, nearest_icon_size, resize
import sys

"""This module takes any image that is readable by PIL and exports it to an icns file.
The image will be scaled keeping the aspect ratio if it is a non square image.
"""

def encode_image_to_icns(image_path):
    """Takes an image and converts it to icns. Image aspect ratio will remain intact."""
    i = Image(image_path)
    icns_header = ICNSHeader()
    f_data = icns_header.parse_image(i)
    return f_data

def save_icns(image_path, icns_path):
    im_data = encode_image_to_icns(image_path)
    icns_path = icns_path if icns_path.endswith('.icns') else icns_path+'.icns'
    open(icns_path, 'wb+').write(im_data)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print 'Usage: pycns input_image_path output_icns_path'
        sys.exit()

    image_path, icns_path = sys.argv[1:3]

    save_icns(image_path, icns_path)