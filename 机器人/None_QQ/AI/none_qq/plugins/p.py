import os

from PIL import Image, ImageFont, ImageDraw
from nonebot.adapters.onebot.v11 import MessageSegment
from nonebot import on_command
from nonebot.adapters.onebot.v11 import Bot, Event, Message


def spacing(check_str, font):
    # 用pil内置textsize函数获取字符串长度
    testkinter = Image.new('RGBA', (300, 300))
    test = ImageDraw.Draw(testkinter)

    return test.textsize(check_str, font=font)[0]


def ph_generator(text1, text2):
    # 配置信息
    rectangle_color = (247, 151, 29)  # 橘色矩形配色
    bg_color = (20, 20, 20)  # 背景色
    font_size = 90  # 字号

    # 字体
    ph_font = ImageFont.truetype(r'D:\WorkSpace\PC\机器人\None_QQ\AI\none_qq\fonts\NotoSansBold.otf', size=font_size)

    len_text1 = spacing(text1, ph_font)
    len_text2 = spacing(text2, ph_font)
    kinter_width = len_text1 + len_text2 + 110
    kinter_height = font_size + 100

    # 画布
    im = Image.new('RGBA', (kinter_width, kinter_height), color=bg_color)

    drawObject = ImageDraw.Draw(im)

    # 画矩形
    x, y = len_text1 + 45, 50
    w, h = len_text2 + 20, font_size
    r = 20

    drawObject.ellipse((x, y, x + r, y + r), fill=rectangle_color)
    drawObject.ellipse((x + w - r, y, x + w, y + r), fill=rectangle_color)
    drawObject.ellipse((x, y + h - r, x + r, y + h), fill=rectangle_color)
    drawObject.ellipse((x + w - r, y + h - r, x + w, y + h), fill=rectangle_color)

    drawObject.rectangle((x + r / 2, y, x + w - (r / 2), y + h), fill=rectangle_color)
    drawObject.rectangle((x, y + r / 2, x + w, y + h - (r / 2)), fill=rectangle_color)

    # 文字
    drawObject.text((25, 50), text1, font=ph_font)
    drawObject.text((len_text1 + 55, 50), text2, font=ph_font, fill=bg_color)

    # 保存
    # im.show()
    im.save('p.png')


ph = on_command("p", priority=2, block=True)


@ph.handle()
async def ph_(bot: Bot, event: Event):
    if event.get_user_id != event.self_id:
        try:
            ch = str(event.message)[2:]
            i = 0
            ss = [' '] * 2
            for it in ch.split(' ', maxsplit=1):
                if i == 2:
                    break
                ss[i] = it
                i = i + 1
            ph_generator(str(ss[0]), str(ss[1]))
            path_ = os.getcwd()
            path_ = path_ + '\p.png'
            mypath = 'file:///' + path_
            print(mypath)
            sst = MessageSegment.image(file=str(mypath))
            await bot.send(
                event=event,
                message=Message(sst)
            )
        except ValueError as e:
            await bot.send(event=event, message="p插件出现故障")
