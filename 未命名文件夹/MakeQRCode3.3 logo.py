import qrcode
from PIL import Image
import os, sys
data2 = input('二维码内容：')
print("[Enter]")
wjm2 = input('文件名：')
print("[Enter]")
logo = input('logo文件名（请把logo文件放在程序所在目录！):')
print("[Enter]")
y2 = input('准备完毕，按回车键开始生成')
def gen_qrcode(string, path, logo=""):
    qr = qrcode.QRCode(
        version=2,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=8,
        border=1
    )
    qr.add_data(string)
    qr.make(fit=True)
    # 互动二Image实例并把颜色模式转换成RGBA
    img = qr.make_image()
    img = img.convert("RGBA")
    if logo and os.path.exists(logo):
        try:
            icon = Image.open(logo)    #打开logo文件
            img_w, img_h = img.size
        except Exception as e:
            print(e)
            sys.exit(1)
        factor = 4
        #计算logo尺寸
        size_w = int(img_w / factor)
        size_h = int(img_h / factor)
        print("生成中...50%")
        #比较并重新设置logo文件（图片pdsu.png）的尺寸
        icon_w, icon_h = icon.size
        if icon_w > size_w:
            icon_w = size_w
        if icon_h > size_h:
            icon_h = size_h
        icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS)
        #计算logo的位置，并且复制到二维码中
        w = int((img_w - icon_w) / 2)
        h = int((img_h - icon_h) / 2)
        icon = icon.convert("RGBA")
        img.paste(icon, (w, h), icon)
        print("生成中...100% Done!")
    img.save(path)
    print("打开中...")           #保存二维码qr.png
    # 调用系统命令打开图片
    img.show()
 
 
if __name__ == "__main__":
    info = data2
    pic_path = wjm2 + ".png"      #生成带有图标的二维码
    icon_path = logo   #用于填充的图标
    gen_qrcode(info, pic_path, icon_path )
filename = '日志.txt'
with open(filename, 'a') as file_object:
    file_object.write("[" + sj + "]---成功完成带logo二维码生成操作，内容：" + data2 + ",生成的文件名:" + wjm2 + " \n")
p = input('完成，按回车退出')