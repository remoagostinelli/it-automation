#!/usr/bin/env python3

from PIL import Image
import os

path = 'images/'
result = '/opt/icons/'

def main():
    for infile in os.listdir(path):
        if infile != '.DS_Store':
            try:
                im = Image.open(os.path.join(path, infile))
                file, ext = os.path.splitext(infile)
                outfile = file + '.jpeg'
                im.rotate(-90).convert('RGB').resize((128, 128), resample=Image.Resampling.NEAREST).save(os.path.join(result, outfile))
                print(infile, 'converted' + '.')
            except OSError:
                print('Did not convert', infile + '.')

if __name__ == '__main__':
    main()