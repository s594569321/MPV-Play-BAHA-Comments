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
from pathlib import Path




# data from BAHA
def download(sn, full_filename,dir,CK_):
    h = get_header()



    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
        #'Cookie':'_ga=GA1.1.1602084786.1744536963; ckM=2661347552; BAHAID=s594569321; BAHAHASHID=f3dc16c7016c45328911457898993d6822b165fe5049ae33c94d58d982d9d1c5; BAHANICK=%E7%B2%89%E5%85%94%E9%A8%8E%E5%A3%AB-%E7%8E%A5%E5%87%9C%E2%99%AC~%2A; BAHALV=47; BAHAFLT=1363446200; MB_BAHAID=s594569321; MB_BAHANICK=%E7%B2%89%E5%85%94%E9%A8%8E%E5%A3%AB-%E7%8E%A5%E5%87%9C%E2%99%AC~%2A; age_limit_content=1; ga_class1=J; ckFORUM_setting=111111222323211221; ckWwwRecommendBoardBlackList=[]; ANIME_dark_theme=0; ANIME_READ_TERM=1; ANIME_NOTICE_PERSONAL_MENU=2; _ga_PNRCS712G2=GS1.1.1746373189.1.0.1746373194.0.0.0; ck_forumCDonateShowHint=yes; PSID_WEB=1e872988ab264957bfc85ecc9d2f1361; avtrv=1750088207; ckBH_lastBoard=[[%2279354%22%2C%22MapleStory%20Worlds%22]%2C[%227650%22%2C%22%E6%96%B0%E6%A5%93%E4%B9%8B%E8%B0%B7%22]%2C[%2238660%22%2C%22%E5%A7%8B%E4%B8%96%E6%A8%82%E5%9C%9F%22]%2C[%2260599%22%2C%22Steam%20%E7%B6%9C%E5%90%88%E8%A8%8E%E8%AB%96%E6%9D%BF%22]%2C[%2260030%22%2C%22%E9%9B%BB%E8%85%A6%E6%87%89%E7%94%A8%E7%B6%9C%E5%90%88%E8%A8%8E%E8%AB%96%22]%2C[%2236390%22%2C%22%E5%8B%9D%E5%88%A9%E5%A5%B3%E7%A5%9E%EF%BC%9A%E5%A6%AE%E5%A7%AC%22]%2C[%2280950%22%2C%22%E4%B8%80%E6%AC%A1%E6%80%A7%E4%BA%A4%E6%98%93%E5%A4%A7%E5%B8%AB%22]%2C[%227200%22%2C%22%E5%A4%A7%E8%88%AA%E6%B5%B7%E6%99%82%E4%BB%A3%20Online%22]%2C[%2274934%22%2C%22%E9%B3%B4%E6%BD%AE%22]%2C[%2279062%22%2C%22inZOI%22]]; BAHAENUR=27d5556c2b797e56fe383b538fd96863; BAHARUNE=eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiJ9.eyJ1c2VyaWQiOiJzNTk0NTY5MzIxIiwidXNlcm5hbWUiOiJcdTdjODlcdTUxNTRcdTlhMGVcdTU4ZWItXHU3M2E1XHU1MWRjXHUyNjZjfioiLCJtb2JpbGVWZXJpZnkiOmZhbHNlLCJkZW55UG9zdCI6ZmFsc2UsImF2YXRhckxldmVsIjo0NywibWlkIjoyNjYxMzQ3NTUyLCJub25jZSI6MjE0MDAzNjEyMCwiamlkIjoiczU5NDU2OTMyMUBsaXRlLmdhbWVyLmNvbS50dyIsImV4cCI6MTc1MjI2NzYwMH0.1ovW144gEsXz0e5E2giUJU2h1GEzXTPiGQ3CgCFYJ42ku6O_2TyviFp24rXY3_6XJVovsVePVkDexu-bj0xytA; MB_BAHARUNE=eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiJ9.eyJ1c2VyaWQiOiJzNTk0NTY5MzIxIiwidXNlcm5hbWUiOiJcdTdjODlcdTUxNTRcdTlhMGVcdTU4ZWItXHU3M2E1XHU1MWRjXHUyNjZjfioiLCJtb2JpbGVWZXJpZnkiOmZhbHNlLCJkZW55UG9zdCI6ZmFsc2UsImF2YXRhckxldmVsIjo0NywibWlkIjoyNjYxMzQ3NTUyLCJub25jZSI6MjE0MDAzNjEyMCwiamlkIjoiczU5NDU2OTMyMUBsaXRlLmdhbWVyLmNvbS50dyIsImV4cCI6MTc1MjI2NzYwMH0.1ovW144gEsXz0e5E2giUJU2h1GEzXTPiGQ3CgCFYJ42ku6O_2TyviFp24rXY3_6XJVovsVePVkDexu-bj0xytA; ANIME_SIGN=02c245dc1232c51976d68940f94084342c23f18f8555327a685e8d7f; ckBahaAd=-------1F----------------; _ga_2Q21791Y9D=GS2.1.s1751029230$o148$g1$t1751029310$j53$l0$h0; ckBahamutCsrfToken=9becad9db0757a44; _ga_MT7EZECMKQ=GS2.1.s1751030927$o17$g0$t1751030927$j60$l0$h0'
        'Cookie': CK_
        }
    
    url = 'https://api.gamer.com.tw/anime/v1/danmu.php?videoSn=' + str(sn) + '&geo=TW%2CHK'

    r = requests.get(url, headers=headers)
  
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
 
    j = j['data']['danmu']
    output.write(f"CK:{CK_}\n")
    for danmu in j:
        output.write(danmu['text']+"\n")
        output.write(f"{danmu['time']}")    
        output.write(danmu['color'])
        output.write(f"{danmu['position']}")

    for danmu in j:
        try:
            print(danmu)
        
            output.write('Dialogue: ')
            output.write('0,')

            if danmu['position'] == 0:  # Roll danmu
                start_time = int(danmu['time'] / 10)-7
                hundred_ms = danmu['time'] % 10
                m, s = divmod(start_time, 60)
                h, m = divmod(m, 60)
                output.write(f'{h:d}:{m:02d}:{s:02d}.{hundred_ms:d}0,')
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
                start_time = int(danmu['time'] / 10)# 補正
                hundred_ms = danmu['time'] % 10
                m, s = divmod(start_time, 60)
                h, m = divmod(m, 60)
                output.write(f'{h:d}:{m:02d}:{s:02d}.{hundred_ms:d}0,')
                end_time = start_time + 5
                m, s = divmod(end_time, 60)
                h, m = divmod(m, 60)
                output.write(f'{h:d}:{m:02d}:{s:02d}.{hundred_ms:d}0,')
                output.write(
                    'Top,,800,0,800,,{\\1c&H4C' + danmu['color'][1:] + '}')
            else:  # Bottom danmu
                start_time = int(danmu['time'] / 10)# 補正
                hundred_ms = danmu['time'] % 10
                m, s = divmod(start_time, 60)
                h, m = divmod(m, 60)
                output.write(f'{h:d}:{m:02d}:{s:02d}.{hundred_ms:d}0,')
                end_time = start_time + 5
                m, s = divmod(end_time, 60)
                h, m = divmod(m, 60)
                output.write(f'{h:d}:{m:02d}:{s:02d}.{hundred_ms:d}0,')
                output.write(
                    'Bottom,,200,0,200,,{\\1c&H4C' + danmu['color'][1:] + '}')

            output.write(danmu['text'])
            output.write('\n')
        except: continue

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
def get_comments(sn,dir,CK_="123"):
    anime_name, episode = get_info(sn)
    print(dir+"/123.ass")
    download(int(sn), dir+"/123.ass",dir,CK_)

    
print(str(sys.argv))
print(len(sys.argv))

try:    
    get_comments(sys.argv[1],sys.argv[2],sys.argv[3])
except:pass
 
