"""
@File    :   video.py
@Author  :   邹磊
@Modify Time  :  2019/12/30 下午12:57

"""
import re
import subprocess

import requests

import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def video_download(url: str, name: str):
    """
    下载视频
    :param name:
    :param url:
    :return:
    """
    url = 'https://jx.618g.com/?url={}'.format(url)

    response = requests.get(url, verify=False).text

    video_m = re.search('url=(.*?m3u8)', response).group(1)
    command = r'ffmpeg -i ' + video_m + ' -vcodec copy -acodec copy geekbang{}.mp4'.format(name)

    subprocess.call(command, shell=True)


video_download(
    "https://static001.geekbang.org/files/vod/8aee20496a62478c908344b3c4edc7fa/c2b20554f2b9502379507006d2726432-sd.m3u8",
    "1继承和成员修饰符")
