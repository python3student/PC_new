import requests
import re
import os
import time


headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
    'Host': 'image.baidu.com',
    'Referer': 'https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct'
               '201326592&cl=2&lm=&st=-1&fm=result&fr=&sf=1&fmq=1610952036123_R&pv=&ic=&nc=1&z=&hd=&latest=&copyr'
               'ight=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&sid=&word=%E6%98%9F%E9%99%85',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'X-Requested-With': 'XMLHttpRequest'}

url = 'http://image.baidu.com/search/index?tn=baiduimage&fm=result&ie=utf-8&word='
print("无尘爬图")
keyword = input("请输入图片关键词：")
# keyword='cyberpunk'
countmax = eval(input("请输入要爬取的图片数量："))
url = url + keyword + "&pn="
time_start = time.time()

strhtml = requests.get(url, headers=headers)
string = str(strhtml.text)


totalnum = re.findall('<div id="resultInfo" style="font-size: 13px;">(.*?)</div>', string)
print("百度图片" + totalnum[0])

img_url_regex = '"thumbURL":"(.*?)",'  # 正则匹配式
count = 0  # 总共下载的图片数
index = 0  # 链接后面的序号
page = 0  # 当前搜集的页
while 1:
    strhtml = requests.get(url + str(index), headers=headers)  # get方式获取数据
    string = str(strhtml.text)
    print("已爬取网页")
    pic_url = re.findall(img_url_regex, string)  # 先利用正则表达式找到图片url
    print("第" + str(page + 1) + "页共收集到" + str(len(pic_url)) + "张图片")
    index += len(pic_url)  # 网址索引向后，跳到下一页继续搜刮图片
    try:  # 如果没有文件夹就创建
        os.mkdir('.' + r'\\' + keyword)
    except:
        pass

    for each in pic_url:
        print('正在下载第' + str(count + 1) + '张图片，图片地址:' + str(each))
        try:
            if each is not None:
                pic = requests.get(each, timeout=5)
            else:
                continue
        except BaseException:
            print('错误，当前图片无法下载')
            continue
        else:
            string = '.' + r'\\' + keyword + r'\\' + keyword + '_' + str(count + 1) + '.jpg'
            fp = open(string, 'wb')
            fp.write(pic.content)
            fp.close()
            count += 1
        if countmax == count:
            break
    if countmax == count:
        break
time_end = time.time()  # 获取结束时间
print('处理完毕，共耗时:' + str(time_end - time_start) + "秒")


