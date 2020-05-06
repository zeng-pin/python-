from PIL import Image
im = Image.open(r"C:\Users\HP\Desktop\活动\作文.png",'r')
print(im.format,im.mode,im.size)
im.show()
s=input()
im.thumbnail((128, 128))
im.show()
s=input()

im = Image.open(r"C:\Users\HP\Desktop\公选课\大学计算机\pybit.gif",'r')      # 读入一个GIF文件
print(im.format,im.mode,im.size)
try:
    im.show()
    s=input()
    while True:
        im.seek(im.tell()+1)
        im.show()
        s=input()
except:
    print("处理结束")
im = Image.open(r"C:\Users\HP\Desktop\活动\作文.png",'r')
r, g, b = im.split()
im = Image.merge("RGB", (b, g, r))
im.show()
s=input()

newg = g.point(lambda i: i * 0.9)   # 将G通道颜色值变为原来的0.9
newb = b.point(lambda i: i < 100) # 选择B通道值低于100的像素点
im=Image.merge(im.mode,(r,newg,newb))     # 将3个通道合形成新图像
im.show()
s=input()

im = im.filter(ImageFilter.CONTOUR)
im.show()
s=input()

im = ImageEnhance.Contrast(im)
im.enhance(20).show()


