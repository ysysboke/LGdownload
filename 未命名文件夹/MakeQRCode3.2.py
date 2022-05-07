import qrcode
import time
sj = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

print("欢迎使用MakeQRCode二维码制作软件终端版")
print("该程序由LightGroup制作，感谢使用！")
print("现在时间：", sj)
print("程序版本：MakeQRCode3.2 Beta 终端版")
data = input('二维码内容：')
print("[Enter]")
wjm = input('文件名：')
print("[Enter]")
y = input('准备完毕，按回车键开始生成')
print("开始生成...")

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4
)
qr.add_data(data)
print("生成中...50%")
qr.make(fit=True)
img = qr.make_image()
img.save(wjm + ".png")
print("生成中...100% Done!")
print("打开中...")
img.show()
print("储存至日志...")

filename = '日志.txt'
with open(filename, 'a') as file_object:
    file_object.write("[" + sj + "]---成功完成生成操作，内容：" + data + ",生成的文件名:" + wjm + " \n")
p = input('完成，按回车退出')
