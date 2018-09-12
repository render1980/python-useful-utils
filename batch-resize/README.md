### Batch-resize

Resize all images from {path}/{source_folder} and save them into {path}_{dest_folder}.

### Run

```
▶ python main.py -h
usage: main.py [-h] [--source SOURCE] [--width WIDTH] [--height HEIGHT]

Resize images in --source folder. Result images will be store in
{source_folder_name}_dest folder.

optional arguments:
  -h, --help       show this help message and exit
  --source SOURCE  source folder with images
  --width WIDTH    image target width
  --height HEIGHT  image target height
```

### Examples

```
python main.py --source /tmp/test_resize --width 800 --height 600 # result images will be in /tmp/test_resize_dest folder

```
