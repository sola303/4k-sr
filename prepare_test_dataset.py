import os
import argparse
from tqdm import tqdm
import cv2
import numpy as np

def get_arguments():
    parser = argparse.ArgumentParser(description='Script for converting video to dataset')
    parser.add_argument('--video_folder', default='/gpu02/dataset_public/AI+4K_HDR/test/',
                        help='folder with video')
    parser.add_argument('--dataset_folder', default='./test',
                        help='folder where to save dataset examples')
    parser.add_argument('--scale_factor', default=4, type=int,
                        help='scale factor for low resolution image')


    return parser.parse_args()

def process_video(lr_filepath,args):

    filename, _ = os.path.splitext(os.path.basename(lr_filepath))
    video_savepath=os.path.join(args.dataset_folder,filename)
    if not os.path.exists(video_savepath):
        os.mkdir(video_savepath)
    lr_seq_save_path=os.path.join(video_savepath,'lr')
    if not os.path.exists(lr_seq_save_path):
        os.mkdir(lr_seq_save_path)
    f = open('test_lr.txt', 'a+')
    cap_lr = cv2.VideoCapture(lr_filepath)
    frame_count=0
    success=True
    while(success):
        success_lr,frame_lr=cap_lr.read()

        success=success_lr
        if success:
            cv2.imwrite(os.path.join(lr_seq_save_path ,"%03d.png" % frame_count), frame_lr,[cv2.IMWRITE_PNG_COMPRESSION,0])

            f.write(os.path.join(lr_seq_save_path ,"%03d.png\n" % frame_count))
            frame_count=frame_count+1
    cap_lr.release()

    f.close()
    return
def main():
    args = get_arguments()

    if not os.path.exists(args.dataset_folder):
        os.mkdir(args.dataset_folder)
    lr_video_folder=os.path.join(args.video_folder,'SDR_540p')
    lr_video_list = [os.path.join(lr_video_folder, fn) for fn in os.listdir(lr_video_folder)]
    # hr_video_folder = sorted(os.path.join(args.video_folder, 'SDR_4K'))
    # hr_video_list = [os.path.join(hr_video_folder, fn) for fn in os.listdir(hr_video_folder)]
    f=open('test_lr.txt','w')
    f.close()
    for i in range(len(lr_video_list)):
        print('Processing ', lr_video_list[i], ', ', str(i + 1), '/', str(len(lr_video_list)))
        process_video(lr_video_list[i],args)
if __name__ == '__main__':
    main()
