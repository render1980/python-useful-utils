import argparse
import os
import cv2

import pdb

ext3 = ['jpg', 'png', 'bmp', 'tif']
ext4 = ['jpeg', 'tiff']

def get_all_images_names(path):
    files = os.listdir(path)
    filtered_files = [file for file in files if file[-3:] in ext3 or file[-4:] in ext4]
    return filtered_files

def parse_args():
    parser = argparse.ArgumentParser(description='Resize images in --source folder. Result images will be store in {source_folder_name}_dest folder.')
    parser.add_argument('--source', dest='source', help='source folder with images')
    # parser.add_argument('--dest', dest='dest', help='dest folder with transformated images')
    parser.add_argument('--width', dest='width', help='image target width')
    parser.add_argument('--height', dest='height', help='image target height')
    args = parser.parse_args()
    return args

def change_image_ext(image_name, ext):
    parts = image_name.split('.')
    parts[-1] = '.' + ext
    return ''.join(parts)

def resize(image_name, source_folder, dest_folder, k=None, width=None, height=None, ext=None):
    image_path = os.path.join(source_folder, image_name)
    image = cv2.imread(image_path)
    # pdb.set_trace()
    print("image_name={0} source_folder={1} dest_folder={2} width={3} height={4}".format(image_name, source_folder, dest_folder, width, height))
    
    if k is None:
        result_image = cv2.resize(image, (int(width), int(height)), interpolation=cv2.INTER_CUBIC)
    else:
        result_image = cv2.resize(image, None, fx=k, fy=k, interpolation=cv2.INTER_CUBIC)
    if ext is None:
        result_image_path = os.path.join(dest_folder, image_name)
    else:
        result_image_path = os.path.join(dest_folder, change_image_ext(image_name, ext))
    cv2.imwrite(result_image_path, result_image)

def resize_images(source_folder, dest_folder, width, height):
    images = get_all_images_names(source_folder)
    # create dest folder
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
    else:
        raise ValueError('Dest Folder already exists!')
    for image_name in images:
        resize(image_name=image_name,
               source_folder=source_folder,
               dest_folder=dest_folder,
               width=width,
               height=height)

def main():
    args = parse_args()
    
    source_folder = args.source
    dest_folder = source_folder+'_dest'
    width = args.width
    height = args.height
    
    # images = get_all_images(source_folder)
    # for image in images:
    #     print("image={0}".format(image))

    resize_images(source_folder, dest_folder, width, height)

if __name__ == '__main__':
    main()
