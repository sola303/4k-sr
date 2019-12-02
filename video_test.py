import os
import argparse
from tqdm import tqdm
import cv2
import numpy as np

def get_arguments():
    parser = argparse.ArgumentParser(description='Script for converting video to dataset')
    parser.add_argument('--video_folder', default='./Video_result',
                        help='folder with video')
    parser.add_argument('--dataset_folder', default='./Results',
                        help='folder where to save dataset examples')
    parser.add_argument('--scale_factor', default=4, type=int,
                        help='scale factor for low resolution image')


    return parser.parse_args()


def main():
    args = get_arguments()
    dir_list=os.listdir('./Results')
    f=open('generate_video.txt','a+')
    for i in range(len(dir_list)):
        video_name=dir_list[i]
        f.write('ffmpeg -r 24000/1001 -i %s -vcodec libx265 -pix_fmt yuv422p -crf 10 %s -y\n'%(os.path.join('./Results',dir_list[i],'%03d.png'),os.path.join('./ffmpeg_video_result',video_name+'.mp4')))
    f.close()
if __name__ == '__main__':
    main()
