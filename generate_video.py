import os
import argparse
import cv2
import numpy as np

def get_arguments():
    parser = argparse.ArgumentParser(description='Script for converting video to dataset')
    parser.add_argument('--video_folder', default='./code_video_result',
                        help='folder with video')
    parser.add_argument('--dataset_folder', default='./Results',
                        help='folder where to save dataset examples')
    parser.add_argument('--scale_factor', default=4, type=int,
                        help='scale factor for low resolution image')


    return parser.parse_args()

def process_video(hr_imagepath,args):

    videoname= os.path.basename(hr_imagepath)
    video_savepath=os.path.join(args.video_folder,videoname)+'.mp4'

    if not os.path.exists(args.video_folder):
        os.mkdir(args.video_folder)
    fps=25
    num=100
    img_size=(3840,2160)
    fourcc=cv2.VideoWriter_fourcc('m','p','4','v')
    video_writer = cv2.VideoWriter(video_savepath,fourcc,fps,img_size)
    for i in range(num):
        img_name=os.path.join(args.dataset_folder,hr_imagepath,'%03d.png'%i)
        try:
            frame=cv2.imread(img_name)
        except Exception:
            print('img does not exit\n')
            print('Force Finish!')
            return
        video_writer.write(frame)
    video_writer.release()
    print('finish')
    return
def main():
    args = get_arguments()

    if not os.path.exists(args.video_folder):
        os.mkdir(args.video_folder)
   # lr_video_folder=os.path.join(args.video_folder,'SDR_540p')
    dir_list=os.listdir(args.dataset_folder)
    hr_video_list = sorted(dir_list,  key=lambda x: os.path.getmtime(os.path.join(args.dataset_folder, x)))
    for i in range(41,len(hr_video_list)):
        print('Processing ', hr_video_list[i], ', ', str(i + 1), '/', str(len(hr_video_list)))
        process_video(hr_video_list[i],args)
if __name__ == '__main__':
    main()
