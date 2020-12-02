# Multiple Image Segmentation

## Original Image
![fire](https://github.com/galenseilis/multiple-image-segmentation/blob/main/fire.jpg)


## Segmented Examples
![grid](https://github.com/galenseilis/multiple-image-segmentation/blob/main/grid.png)

## Usage


```
usage: multiseg.py [-h] [-i IN_FILE] [-p CPU] [-s START] [-e END] [-f FLIP]

This CLI will perform multiple image segmentations on a given image.

optional arguments:
  -h, --help            show this help message and exit
  -i IN_FILE, --in_file IN_FILE
                        Intput image file.
  -p CPU, --cpu CPU     Number of processors/CPUs to use.
  -s START, --start START
                        Starting number of segments.
  -e END, --end END     Ending number of segments.
  -f FLIP, --flip FLIP  Rotate image by 180 degrees.
```
