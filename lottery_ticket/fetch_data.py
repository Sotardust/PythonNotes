import json

# coding=gbk
import time
import requests
import pandas as pd


def write_json_to_file(data, filename):
    with open(filename, 'a', encoding="utf8") as file:
        file.write(data)


url = "https://www.cwl.gov.cn/cwl_admin/front/cwlkj/search/kjxx/findDrawNotice"
params = {
    'name': 'ssq',
    'issueCount': '',
    'issueStart': '',
    'issueEnd': '',
    'dayStart': '',
    'dayEnd': '',
    'pageNo': 1,
    'pageSize': 30,
    'week': '',
    'systemType': 'PC',
}

header = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Cookie': 'HMF_CI=c5e50c6669ec97153ed140ea30f3eb070d8faea96fbcdf670ed7e2d8931d52333b32cced986c96d2e15287f95c0b17c77e9928eadb1275b99291225d5bbd4ca230; 21_vq=5',
    'Host': 'www.cwl.gov.cn',
    'Referer': 'https://www.cwl.gov.cn/ygkj/wqkjgg/ssq/',
    'Sec-Ch-Ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Microsoft Edge";v="122"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0',
    'X-Requested-With': 'XMLHttpRequest',
}

if __name__ == '__main__':

    def catch(i):
        params['pageNo'] = i
        try:
            response = requests.get(url=url, params=params, headers=header)
            if response.status_code == 200:
                write_json_to_file(response.text, "out.txt")
                result = response.json()['result']
                if not result:  # 如果结果为空，说明没有更多数据
                    return None
                data = [[int(a['code'])] + [int(k) for k in a['red'].split(',')] + [int(a['blue'])] for a in result]
                return pd.DataFrame(data, columns=['code', 'r1', 'r2', 'r3', 'r4', 'r5', 'r6', 'b1'])
            else:
                print('请求错误：', response.status_code)
        except Exception as e:
            print('发生异常：', e)


    try:
        data_frames = []  # 创建一个空列表来存储数据帧
        page = 1
        while True:
            print("正在爬取第{}页数据....".format(page))
            new_data = catch(page)  # 假设 catch() 函数返回一个数据帧
            if new_data is not None:
                print("爬取成功，正在整合数据...")
                data_frames.append(new_data)  # 将新数据帧添加到列表中
            else:
                print("已经没有更多数据，爬取结束。")
                break  # 如果没有新数据，则退出循环
            page += 1
            # time.sleep(1)
        df = pd.concat(data_frames, ignore_index=True)  # 循环结束后一次性合并所有数据帧
        # 反序DataFrame
        df = df.iloc[::-1]
        # 保存反序后的DataFrame到新的CSV文件
        df.to_csv('reversed_data.csv', index=False, encoding='gbk')
    except Exception as e:
        print('出错或到达页数最底层：', e)
