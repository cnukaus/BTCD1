from PIL import Image
import os
import imageio
import sys

def rotate(picture_name,pos=20):

    filename=os.path.join(os.path.dirname(os.path.abspath(__file__)),picture_name)
    im=Image.open(filename)

    for pos in range (pos):
        im_shift=im.rotate(pos*2)
        im_shift.save('{0}.PNG'.format(pos))
        im_shift=im.rotate(-pos*2)
        im_shift.save('{0}.PNG'.format(-pos))


def create_gif(source, name, duration):
    """
     Generate gif function, the original image only supports png
           Source: is a list of png images (ordered)
           Name : the name of the generated file
           Duration: the time interval between each image
    """
    frames = []     # buffer
    for img in source:
        frames.append(imageio.imread(img))
    imageio.mimsave(name, frames, 'GIF', duration=duration)
    print("Processing completed")

def transform(im):
    return im.transform(im.size, Image.MESH, mesh)
def main(or_path,gif_name,duration_time = 0.8):
    """
     Or_path: the target folder
    """
    path = os.chdir(or_path)
    pic_list = os.listdir()
    pic_list = [x for x in pic_list] # in pic_list  if 'PNG' in x
    create_gif(pic_list, gif_name, duration_time)

if __name__ == '__main__':
    #picture_name = "613.JPG"
    #rotate(picture_name)

    '''filename=os.path.join(os.path.dirname(os.path.abspath(__file__)),picture_name)
    im=Image.open(filename)
    transform(im).save('trans.jpg')'''

    parm_list = sys.argv
    parm_list[1]
    if len(parm_list) != 2:
        print("Please enter the folder you need to process!")
    else:
        main(parm_list[1],"congrat_wen.gif")