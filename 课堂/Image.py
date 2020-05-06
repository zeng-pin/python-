from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance

im = Image.open("birdnest.jpg")
print(im.format,im.mode,im.size)
im.show()
s=input()
im.thumbnail((128, 128))
im.save("birdnestTN.jpg","JPEG")
print(im.format,im.mode,im.size)
im.show()
s=input()

im = Image.open('pybit.gif')      # 读入一个GIF文件
print(im.format,im.mode,im.size)
try:
    im.save('picframe{:02d}.png'.format(im.tell()))
    im.show()
    s=input()
    while True:
        im.seek(im.tell()+1)
        im.save('picframe{:02d}.png'.format(im.tell()))
        im.show()
        s=input()
except:
    print("处理结束")

im = Image.open('birdnest.jpg')
r, g, b = im.split()
om = Image.merge("RGB", (b, g, r))
om.save('birdnestBGR.jpg')
om.show()
s=input()

newg = g.point(lambda i: i * 0.9)   # 将G通道颜色值变为原来的0.9
newb = b.point(lambda i: i < 100) # 选择B通道值低于100的像素点
om=Image.merge(im.mode,(r,newg,newb))     # 将3个通道合形成新图像
om.save('birdnestMerge.jpg')       # 输出图片
om.show()
s=input()

om = im.filter(ImageFilter.CONTOUR)
om.save('birdnestContour.jpg')
om.show()
s=input()

om = ImageEnhance.Contrast(im)
om.enhance(20).save('birdnestEnContrast.jpg')
om.enhance(20).show()
