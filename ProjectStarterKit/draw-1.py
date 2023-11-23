#draw_program
#Author1: Yanjun Qian
#Section1 : OL01
#Author2: Tianyu Cai
#Section2 :D300
#Group: FinalProject - 180
#Date : Nov 19 / 22

import cmpt120image
import random
#1
def recolorImage(img,color):
    res = cmpt120image.getBlackImage(len(img[0]), len(img))

    for i in range(len(img)):
        for j in range(len(img[i])):
            r = img[i][j][0]
            g = img[i][j][1]
            b = img[i][j][2]
            total = int(r)+int(g)+int(b)
            if r >= 225 and g >= 225 and b >= 225:
                res[i][j] = [255,255,255]
            else:
                res[i][j] = color
    return res

#2
def addcolCom(img, row, col, com):
    colCom = img[row - 1][col][com] + img[row][col-1][com] + img[row][col][com]\
        + img[row-1][col-1][com]
    return colCom

def minify(img):
    final = cmpt120image.getBlackImage(len(img[0])//2, len(img)//2)
    for row in range(len(img)-1, 0, -2):
        for col in range(len(img[row])-1, 0, -2):
            avered = addcolCom(img,row,col,0)//4
            avegreen = addcolCom(img,row,col,1)//4
            aveblue = addcolCom(img,row,col,2)//4

            final[row//2][col//2] = (avered, avegreen, aveblue)

    return final

#3
def mirror(img):
    res = cmpt120image.getBlackImage(len(img[0]), len(img))

    for i in range(len(img)):
        for j in range (len(img[i])//2):
            pixel = img[i][j]
            res[i][j] = img[i][len(img[i])-1-j]
            res[i][len(img[i])-1-j] = pixel
    return res

#4
def checkWhite(r, g, b):
    trueW = (r >= 255 and g >= 255 and b >= 255)
    return trueW

def drawItem(canvas, item, row, col):
    for i in range(len(item)):
        for j in range(len(item[i])):
            pix = item[i][j]
            if not checkWhite(pix[0], pix[1], pix[2]):
                canvas[row + i][col + j] = pix

#5
def distributeItems(canvas, item, n):
    for i in range(n):
        height = len(canvas)
        width = len(canvas[0])
        heightItem = len(item)
        widthItem = len(item[0])
        ranheight = random.randint(0,height-heightItem)
        ranwidth = random.randint(0,width-widthItem )
        drawItem(canvas, item, ranheight, ranwidth)


##test

#1
#img1 = cmpt120image.getImage("images/child.png")
#cmpt120image.showImage(img1)
#img2 = recolorImage(img1, [0,255,0])
#cmpt120image.showImage(img2)
#input("...")

#2
#img1 = cmpt120image.getImage("images/child.png")
#cmpt120image.showImage(img1)
#img2 = minify(img1)
#cmpt120image.showImage(img2)
#input("...")

#3
#img1 = cmpt120image.getImage("images/child.png")
#cmpt120image.showImage(img1)
#img2 = mirror(img1)
#cmpt120image.showImage(img2)
#input("...")

#4
#img1 = cmpt120image.getImage("images/child.png")
#cmpt120image.showImage(img1)
#canva = cmpt120image.getWhiteImage(400, 300)
#drawItem(canva, img1, 20, 40)
#cmpt120image.showImage(canva)
#input("...")

#5
#img1 = cmpt120image.getImage("images/child.png")
#cmpt120image.showImage(img1)
#canva = cmpt120image.getWhiteImage(400, 300)
#distributeItems(canva, img1, 4)
#cmpt120image.showImage(canva)
#input("...")


