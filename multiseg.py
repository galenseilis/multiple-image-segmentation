#!/usr/bin/env python3
#-*- coding:utf-8 - *-

"""
This CLI will perform multiple image segmentations on a given image.


GNU General Public License v3.0
Permissions of this strong copyleft license are conditioned on making available complete source code of licensed works and modifications,
which include larger works using a licensed work, under the same license.
Copyright and license notices must be preserved.
Contributors provide an express grant of patent rights.

Reference Materials:

"""

import os
import time

from multiprocessing import Pool
import matplotlib.pyplot as plt
import numpy as np
import skimage.segmentation as seg
from skimage import io


def segment_image(image, n_segments):
    image = image.copy()
    image_slic = seg.slic(image,n_segments=n_segments)
    for label in np.unique(image_slic):
        for i in range(3):
            image[:,:,i][image_slic == label] = np.mean(image[:,:,i][image_slic == label])
    plt.imsave(f'segmented_{n_segments}.png', image)
    print(time.ctime(), n_segments)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.description = '''This CLI will perform multiple image segmentations on a given image.'''
    parser.add_argument("-i", "--in_file", type=str, help="Intput image file.")
    parser.add_argument("-p", "--cpu", type=int, default=len(os.sched_getaffinity(0)), help="Number of processors/CPUs to use.")
    parser.add_argument("-s", "--start", type=int, default=1, help="Starting number of segments.")
    parser.add_argument("-e", "--end", type=int, default=16, help="Ending number of segments.")
    parser.add_argument("-f", "--flip", type=int, default=0, help="Ending number of segments.")
    args = parser.parse_args()

    file = args.in_file
    if args.flip:
        img = np.rot90(np.rot90(io.imread(file)))
    else:
        img = io.imread(file)

    def para_seg(n):
        try:
            return segment_image(img, n)
        except ZeroDivisionError:
            pass

    with Pool(args.cpu) as p:
        p.map(para_seg, range(args.start, args.end+1))
