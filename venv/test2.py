


#%matplotlib inline
from pycocotools.coco import COCO
import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt
import pylab
from shutil import copyfile

pylab.rcParams['figure.figsize'] = (8.0, 10.0)



#第一个数据集的处理(注释参照test1)
dataDir='/data/coco/image/train2017'
newdataDir='/data/coco/target_image/1dog/'#
dataType='train2017'
#annFile='{}/annotations/instances_{}.json'.format(dataDir,dataType)
annFile='/data/coco/annotations/annotations_trainval2017/annotations_trainval2017.json'.format(dataDir,dataType)

# initialize COCO api for instance annotations
coco=COCO(annFile)

# display COCO categories and supercategories
dogs = coco.loadDogs(coco.getDogIds())
nms=[dog['name'] for dog in dogs]
print('COCO categories: \n{}\n'.format(' '.join(nms)))
nms = set([dog['supercategory'] for dog in dogs])
print('COCO supercategories: \n{}'.format(' '.join(nms)))

# get all images containing given categories
dogIds = coco.getDogIds(dogNms=['dog'])
imgIds = coco.getImgIds(dogIds=dogIds )#list in int

imgs=coco.loadImgs(imgIds)


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





#第二个数据集的处理(注释参照test1)
dataDir='/data/coco/image/train2014'   #读取数据集的地址
newdataDir='/data/coco/target_image/2dog/'#储存数据集的地址
dataType='train2014'
#annFile='{}/annotations/instances_{}.json'.format(dataDir,dataType)
annFile='/data/coco/annotations/annotations_trainval2014/annotations_trainval2014.json'.format(dataDir,dataType) #

# initialize COCO api for instance annotations
coco=COCO(annFile)

# display COCO categories and supercategories
dogs = coco.loadDogs(coco.getDogIds())
nms=[dog['name'] for dog in dogs]
print('COCO categories: \n{}\n'.format(' '.join(nms)))
nms = set([dog['supercategory'] for dog in dogs])
print('COCO supercategories: \n{}'.format(' '.join(nms)))

# get all images containing given categories
dogIds = coco.getDogIds(dogNms=['dog'])
imgIds = coco.getImgIds(dogIds=dogIds )#list in int

imgs=coco.loadImgs(imgIds)


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



#第三个数据集的处理(注释参照test1)
dataDir='/data/coco/image/test2014'   #读取数据集的地址
newdataDir='/data/coco/target_image/3dog/'#储存数据集的地址
dataType='test2014'
#annFile='{}/annotations/instances_{}.json'.format(dataDir,dataType)
annFile='/data/coco/annotations/image_info_test2014/image_info_test2014.json'.format(dataDir,dataType) #

# initialize COCO api for instance annotations
coco=COCO(annFile)

# display COCO categories and supercategories
dogs = coco.loadDogs(coco.getDogIds())
nms=[dog['name'] for dog in dogs]
print('COCO categories: \n{}\n'.format(' '.join(nms)))
nms = set([dog['supercategory'] for dog in dogs])
print('COCO supercategories: \n{}'.format(' '.join(nms)))

# get all images containing given categories
dogIds = coco.getDogIds(dogNms=['dog'])
imgIds = coco.getImgIds(dogIds=dogIds )#list in int

imgs=coco.loadImgs(imgIds)


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





#第四个数据集的处理(注释参照test1)
dataDir='/data/coco/image/test2015'   #读取数据集的地址
newdataDir='/data/coco/target_image/3dog/'#储存数据集的地址
dataType='test2015'
#annFile='{}/annotations/instances_{}.json'.format(dataDir,dataType)
annFile='/data/coco/annotations/image_info_test2015/image_info_test2015.json'.format(dataDir,dataType) #

# initialize COCO api for instance annotations
coco=COCO(annFile)

# display COCO categories and supercategories
dogs = coco.loadDogs(coco.getDogIds())
nms=[dog['name'] for dog in dogs]
print('COCO categories: \n{}\n'.format(' '.join(nms)))
nms = set([dog['supercategory'] for dog in dogs])
print('COCO supercategories: \n{}'.format(' '.join(nms)))

# get all images containing given categories
dogIds = coco.getDogIds(dogNms=['dog'])
imgIds = coco.getImgIds(dogIds=dogIds )#list in int

imgs=coco.loadImgs(imgIds)


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

#第四个数据集的处理(注释参照test1)
dataDir='/data/coco/image/test2015'   #读取数据集的地址
newdataDir='/data/coco/target_image/4dog/'#储存数据集的地址
dataType='test2015'
#annFile='{}/annotations/instances_{}.json'.format(dataDir,dataType)
annFile='/data/coco/annotations/image_info_test2015/image_info_test2015.json'.format(dataDir,dataType) #

# initialize COCO api for instance annotations
coco=COCO(annFile)

# display COCO categories and supercategories
dogs = coco.loadDogs(coco.getDogIds())
nms=[dog['name'] for dog in dogs]
print('COCO categories: \n{}\n'.format(' '.join(nms)))
nms = set([dog['supercategory'] for dog in dogs])
print('COCO supercategories: \n{}'.format(' '.join(nms)))

# get all images containing given categories
dogIds = coco.getDogIds(dogNms=['dog'])
imgIds = coco.getImgIds(dogIds=dogIds )#list in int

imgs=coco.loadImgs(imgIds)


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


#第五个数据集的处理(注释参照test1)
dataDir='/data/coco/image/test2017'   #读取数据集的地址
newdataDir='/data/coco/target_image/5dog/'#储存数据集的地址
dataType='test2017'
#annFile='{}/annotations/instances_{}.json'.format(dataDir,dataType)
annFile='/data/coco/annotations/image_info_test2017/image_info_test2017.json'.format(dataDir,dataType) #

# initialize COCO api for instance annotations
coco=COCO(annFile)

# display COCO categories and supercategories
dogs = coco.loadDogs(coco.getDogIds())
nms=[dog['name'] for dog in dogs]
print('COCO categories: \n{}\n'.format(' '.join(nms)))
nms = set([dog['supercategory'] for dog in dogs])
print('COCO supercategories: \n{}'.format(' '.join(nms)))

# get all images containing given categories
dogIds = coco.getDogIds(dogNms=['dog'])
imgIds = coco.getImgIds(dogIds=dogIds )#list in int

imgs=coco.loadImgs(imgIds)


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




#第六个数据集的处理(注释参照test1)
dataDir='/data/coco/image/unlabeled2017'   #读取数据集的地址
newdataDir='/data/coco/target_image/6dog/'#储存数据集的地址
dataType='unlabeled2017'
#annFile='{}/annotations/instances_{}.json'.format(dataDir,dataType)
annFile='/data/coco/annotations/image_info_unlabeled2017/image_info_unlabeled2017.json'.format(dataDir,dataType) #

# initialize COCO api for instance annotations
coco=COCO(annFile)

# display COCO categories and supercategories
dogs = coco.loadDogs(coco.getDogIds())
nms=[dog['name'] for dog in dogs]
print('COCO categories: \n{}\n'.format(' '.join(nms)))
nms = set([dog['supercategory'] for dog in dogs])
print('COCO supercategories: \n{}'.format(' '.join(nms)))

# get all images containing given categories
dogIds = coco.getDogIds(dogNms=['dog'])
imgIds = coco.getImgIds(dogIds=dogIds )#list in int

imgs=coco.loadImgs(imgIds)


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