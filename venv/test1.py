

#%matplotlib inline
from pycocotools.coco import COCO
import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt
import pylab
from shutil import copyfile

pylab.rcParams['figure.figsize'] = (8.0, 10.0)


#第一个数据集的处理
Z = zipfile.ZipFile(f'{root}/annotations/annotations_trainval2017.zip')#解压标注集
Z = zipfile.ZipFile(f'{root}/images/train2017.zip')#解压数据集
dataDir='/data/coco/image/train2017'   #读取数据集的地址
newdataDir='/data/coco/target_image/1cat/'#储存数据集的地址
dataType='train2017'
#annFile='{}/annotations/instances_{}.json'.format(dataDir,dataType)
annFile='/data/coco/annotations/stuff_annotations_trainval2017/stuff_annotations_trainval2017.json'.format(dataDir,dataType) #

# initialize COCO api for instance annotations
coco=COCO(annFile)

# display COCO categories and supercategories
cats = coco.loadCats(coco.getCatIds())
nms=[cat['name'] for cat in cats]
print('COCO categories: \n{}\n'.format(' '.join(nms)))
nms = set([cat['supercategory'] for cat in cats])
print('COCO supercategories: \n{}'.format(' '.join(nms)))

# get all images containing given categories
catIds = coco.getCatIds(catNms=['cat'])
imgIds = coco.getImgIds(catIds=catIds )#list in int

imgs=coco.loadImgs(imgIds)
#print len(imgs)
#if len(imgs)>2000:



for img in imgs:
    annIds = coco.getAnnIds(imgIds=img['id'], catIds=catIds, iscrowd=None)
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




#第二个数据集的处理
Z = zipfile.ZipFile(f'{root}/annotations/annotations_trainval2014.zip')#解压标注集
Z = zipfile.ZipFile(f'{root}/images/train2014.zip')#解压数据集
dataDir='/data/coco/image/train2014'   #读取数据集的地址
newdataDir='/data/coco/target_image/2cat/'#储存数据集的地址
dataType='train2014'
#annFile='{}/annotations/instances_{}.json'.format(dataDir,dataType)
annFile='/data/coco/annotations/annotations_trainval2014/annotations_trainval2014.json'.format(dataDir,dataType) #

# initialize COCO api for instance annotations
coco=COCO(annFile)

# display COCO categories and supercategories
cats = coco.loadCats(coco.getCatIds())
nms=[cat['name'] for cat in cats]
print('COCO categories: \n{}\n'.format(' '.join(nms)))
nms = set([cat['supercategory'] for cat in cats])
print('COCO supercategories: \n{}'.format(' '.join(nms)))

# get all images containing given categories
catIds = coco.getCatIds(catNms=['cat'])
imgIds = coco.getImgIds(catIds=catIds )#list in int

imgs=coco.loadImgs(imgIds)
#print len(imgs)
#if len(imgs)>2000:



for img in imgs:
    annIds = coco.getAnnIds(imgIds=img['id'], catIds=catIds, iscrowd=None)
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


#第三个数据集的处理
Z = zipfile.ZipFile(f'{root}/annotations/image_info_test2014.zip')#解压标注集
Z = zipfile.ZipFile(f'{root}/images/test2014.zip')#解压数据集
dataDir='/data/coco/image/test2014'   #读取数据集的地址
newdataDir='/data/coco/target_image/3cat/'#储存数据集的地址
dataType='test2014'
#annFile='{}/annotations/instances_{}.json'.format(dataDir,dataType)
annFile='/data/coco/annotations/image_info_test2014/image_info_test2014.json'.format(dataDir,dataType) #

# initialize COCO api for instance annotations
coco=COCO(annFile)

# display COCO categories and supercategories
cats = coco.loadCats(coco.getCatIds())
nms=[cat['name'] for cat in cats]
print('COCO categories: \n{}\n'.format(' '.join(nms)))
nms = set([cat['supercategory'] for cat in cats])
print('COCO supercategories: \n{}'.format(' '.join(nms)))

# get all images containing given categories
catIds = coco.getCatIds(catNms=['cat'])
imgIds = coco.getImgIds(catIds=catIds )#list in int

imgs=coco.loadImgs(imgIds)
#print len(imgs)
#if len(imgs)>2000:



for img in imgs:
    annIds = coco.getAnnIds(imgIds=img['id'], catIds=catIds, iscrowd=None)
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




#第四个数据集的处理
Z = zipfile.ZipFile(f'{root}/annotations/image_info_test2015.zip')#解压标注集
Z = zipfile.ZipFile(f'{root}/images/test2015.zip')#解压数据集
dataDir='/data/coco/image/test2015'   #读取数据集的地址
newdataDir='/data/coco/target_image/4cat/'#储存数据集的地址
dataType='test2015'
#annFile='{}/annotations/instances_{}.json'.format(dataDir,dataType)
annFile='/data/coco/annotations/image_info_test2015/image_info_test2015.json'.format(dataDir,dataType) #

# initialize COCO api for instance annotations
coco=COCO(annFile)

# display COCO categories and supercategories
cats = coco.loadCats(coco.getCatIds())
nms=[cat['name'] for cat in cats]
print('COCO categories: \n{}\n'.format(' '.join(nms)))
nms = set([cat['supercategory'] for cat in cats])
print('COCO supercategories: \n{}'.format(' '.join(nms)))

# get all images containing given categories
catIds = coco.getCatIds(catNms=['cat'])
imgIds = coco.getImgIds(catIds=catIds )#list in int

imgs=coco.loadImgs(imgIds)
#print len(imgs)
#if len(imgs)>2000:



for img in imgs:
    annIds = coco.getAnnIds(imgIds=img['id'], catIds=catIds, iscrowd=None)
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



#第五个数据集的处理
Z = zipfile.ZipFile(f'{root}/annotations/image_info_test2017.zip')#解压标注集
Z = zipfile.ZipFile(f'{root}/images/test2017.zip')#解压数据集
dataDir='/data/coco/image/test2017'   #读取数据集的地址
newdataDir='/data/coco/target_image/5cat/'#储存数据集的地址
dataType='test2017'
#annFile='{}/annotations/instances_{}.json'.format(dataDir,dataType)
annFile='/data/coco/annotations/image_info_test2017/image_info_test2017.json'.format(dataDir,dataType) #

# initialize COCO api for instance annotations
coco=COCO(annFile)

# display COCO categories and supercategories
cats = coco.loadCats(coco.getCatIds())
nms=[cat['name'] for cat in cats]
print('COCO categories: \n{}\n'.format(' '.join(nms)))
nms = set([cat['supercategory'] for cat in cats])
print('COCO supercategories: \n{}'.format(' '.join(nms)))

# get all images containing given categories
catIds = coco.getCatIds(catNms=['cat'])
imgIds = coco.getImgIds(catIds=catIds )#list in int

imgs=coco.loadImgs(imgIds)
#print len(imgs)
#if len(imgs)>2000:



for img in imgs:
    annIds = coco.getAnnIds(imgIds=img['id'], catIds=catIds, iscrowd=None)
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



#第六个数据集的处理
Z = zipfile.ZipFile(f'{root}/annotations/image_info_unlabeled2017.zip')#解压标注集
Z = zipfile.ZipFile(f'{root}/images/unlabeled2017.zip')#解压数据集
dataDir='/data/coco/image/unlabeled2017'   #读取数据集的地址
newdataDir='/data/coco/target_image/6cat/'#储存数据集的地址
dataType='unlabeled2017'
#annFile='{}/annotations/instances_{}.json'.format(dataDir,dataType)
annFile='/data/coco/annotations/image_info_unlabeled2017/image_info_unlabeled2017.json'.format(dataDir,dataType) #

# initialize COCO api for instance annotations
coco=COCO(annFile)

# display COCO categories and supercategories
cats = coco.loadCats(coco.getCatIds())
nms=[cat['name'] for cat in cats]
print('COCO categories: \n{}\n'.format(' '.join(nms)))
nms = set([cat['supercategory'] for cat in cats])
print('COCO supercategories: \n{}'.format(' '.join(nms)))

# get all images containing given categories
catIds = coco.getCatIds(catNms=['cat'])
imgIds = coco.getImgIds(catIds=catIds )#list in int

imgs=coco.loadImgs(imgIds)
#print len(imgs)
#if len(imgs)>2000:



for img in imgs:
    annIds = coco.getAnnIds(imgIds=img['id'], catIds=catIds, iscrowd=None)
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
