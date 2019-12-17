


#%matplotlib inline
from pycocotools.coco import COCO
import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt
import pylab
from shutil import copyfile

pylab.rcParams['figure.figsize'] = (8.0, 10.0)

dataDir='/home/kylefan/data/coco/train2017'#需要改动地址
newdataDir='/home/kylefan/data/coco/mydataset/2dog/'
dataType='train2017'
#annFile='{}/annotations/instances_{}.json'.format(dataDir,dataType)
annFile='/home/kylefan/data/coco/annotations_trainval2017/annotations/instances_train2017.json'.format(dataDir,dataType)

# initialize COCO api for instance annotations
coco=COCO(annFile)

# display COCO categories and supercategories
dogs = coco.loadDogs(coco.getDogIds())
nms=[Dog['name'] for dog in dogs]
print('COCO categories: \n{}\n'.format(' '.join(nms)))
nms = set([dog['supercategory'] for dog in dogs])
print('COCO supercategories: \n{}'.format(' '.join(nms)))

# get all images containing given categories
dogIds = coco.getDogIds(dogNms=['dog']);
imgIds = coco.getImgIds(dogIds=dogIds );#list in int

imgs=coco.loadImgs(imgIds)
#print len(imgs)
#if len(imgs)>2000:
#    imgs=imgs[:2000]


for img in imgs:
    annIds = coco.getAnnIds(imgIds=img['id'], dogIds=dogIds, iscrowd=None)
    anns = coco.loadAnns(annIds)
    #1 in 1
    #print img['file_name'],'has chair in',anns[0]['bbox']

    #1,move jpg to new folder

    copyfile(dataDir+'/'+img['file_name'],newdataDir+img['file_name'])

    #2,create label file txt
    box = str(int(round(anns[0]['bbox'][0])))+' '+str(int(round(anns[0]['bbox'][1])))+' '+str(int(round(anns[0]['bbox'][2])))+' '+str(int(round(anns[0]['bbox'][3])))+' 2'
    #bbox to string
    file = open(newdataDir+img['file_name']+'.txt','w')
    file.write(box)
    file.close()
    #more in 1
    # for ann in anns:
    #     print img['file_name'],'has dog in',ann['bbox']

