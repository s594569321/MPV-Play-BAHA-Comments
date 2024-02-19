import json
import os
from pickle import TRUE
import random
from re import sub, compile
import sys
import xml.etree.cElementTree as ET 
import requests
import random
from bs4 import BeautifulSoup
import re

# data from BAHA
def download(sn, full_filename,dir):
    h = get_header()
    data = {'sn': str(sn)}
    r = requests.post(
        'https://ani.gamer.com.tw/ajax/danmuGet.php', data=data, headers=h)

    if r.status_code != 200:
        print('sn=' + str(sn) + ' 彈幕下載失敗, status_code=' + str(status_code))
        return

    output = open(full_filename, 'w', encoding='utf8')
    with open(dir+'/DanmuTemplate.ass', 'r', encoding='utf8') as temp:
        for line in temp.readlines():
            output.write(line)

    j = json.loads(r.text)

    height = 50

    roll_channel = list()
    roll_time = list()

    for danmu in j:
        output.write('Dialogue: ')
        output.write('0,')

        start_time = int(danmu['time'] / 10)-7
        hundred_ms = danmu['time'] % 10
        m, s = divmod(start_time, 60)
        h, m = divmod(m, 60)
        output.write(f'{h:d}:{m:02d}:{s:02d}.{hundred_ms:d}0,')

        if danmu['position'] == 0:  # Roll danmu
            height = 0
            end_time = 0
            for i in range(len(roll_channel)):
                if roll_channel[i] <= danmu['time']:
                    height = i * 54 + 27
                    roll_channel[i] = danmu['time'] + (len(danmu['text']) * roll_time[i]) / 8 + 1
                    end_time = start_time + roll_time[i]
                    break
            if height == 0:
                roll_channel.append(0)
                roll_time.append(random.randint(20, 28))
                roll_channel[-1] = danmu['time'] + (len(danmu['text']) * roll_time[-1]) / 8 + 1
                height = len(roll_channel) * 54 - 27
                end_time = start_time + roll_time[-1]

            m, s = divmod(end_time, 60)
            h, m = divmod(m, 60)
            output.write(f'{h:d}:{m:02d}:{s:02d}.{hundred_ms:d}0,')

            output.write(
                'Roll,,0,0,0,,{\\move(1920,' + str(height) + ',-1000,' + str(height) + ')\\1c&H4C' + danmu['color'][1:] + '}')
        elif danmu['position'] == 1:  # Top danmu
            end_time = start_time + 5
            m, s = divmod(end_time, 60)
            h, m = divmod(m, 60)
            output.write(f'{h:d}:{m:02d}:{s:02d}.{hundred_ms:d}0,')
            output.write(
                'Top,,800,0,800,,{\\1c&H4C' + danmu['color'][1:] + '}')
        else:  # Bottom danmu
            end_time = start_time + 5
            m, s = divmod(end_time, 60)
            h, m = divmod(m, 60)
            output.write(f'{h:d}:{m:02d}:{s:02d}.{hundred_ms:d}0,')
            output.write(
                'Bottom,,200,0,200,,{\\1c&H4C' + danmu['color'][1:] + '}')

        output.write(danmu['text'])
        output.write('\n')

    print('彈幕下載完成 file: ' + full_filename)


def downlaod_all(sn, bangumi_path, format_str='{anime_name}[{episode}].ass'):
    h = h = get_header()
    r = requests.get(
        'https://ani.gamer.com.tw/animeVideo.php?sn=' + str(sn), headers=h)

    if r.status_code != 200:
        print(str(sn) + '彈幕下載失敗, status_code=' + str(status_code))
        return

    soup = BeautifulSoup(r.text, 'lxml')
    anime_name = re.match(r'(^.+)\s\[.+\]$', soup.find_all('div',
                                                           class_='anime_name')[0].h1.string).group(1)
    print(anime_name)

    # This may fail 抓不到其他集數 可能為劇場版 套用單集下載策略
    sn_list = soup.find_all('section', class_='season')[0].find_all('a')

    os.makedirs(os.path.join(bangumi_path, anime_name), exist_ok=True)

    for s in sn_list:
        episode = s.string
        download(s['href'][4:], os.path.join(bangumi_path, anime_name,
                                             format_str.format(anime_name=anime_name, episode=episode)))


def get_info(sn):
    h = get_header()
    r = requests.get('https://ani.gamer.com.tw/animeVideo.php?sn=' + str(sn), headers=h)

    if r.status_code != 200:
        print(str(sn) + '獲取資訊失敗, status_code=' + str(status_code))
        return

    soup = BeautifulSoup(r.text, 'lxml')
    anime_name = re.match(r'(^.+)\s\[.+\]$', soup.find_all('div',
                                                           class_='anime_name')[0].h1.string).group(1)
    episode = re.match(r'^.+\s\[(.+)\]$', soup.find_all('div',
                                                        class_='anime_name')[0].h1.string).group(1)
    return anime_name, episode


def get_header():
    return {
        'Content-Type':
        'application/x-www-form-urlencoded;charset=utf-8',
        'origin':
        'https://ani.gamer.com.tw',
        'authority':
        'ani.gamer.com.tw',
        'user-agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
    }
def get_comments(sn,dir):
    anime_name, episode = get_info(sn)
    print(dir+"/123.ass")
    download(int(sn), dir+"/123.ass",dir)

    
print(str(sys.argv))
print(len(sys.argv))       
get_comments(sys.argv[1],sys.argv[2])
