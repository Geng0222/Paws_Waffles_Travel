#爬蟲模組
from bs4 import BeautifulSoup
import requests

def oil_price(): #油價
    url = 'https://gas.goodlife.tw/'
    res = requests.get(url, verify=False)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text,'html.parser') 
    card = soup.find("div",id="cpc")
    [s.extract() for s in soup('h3')]  #刪除頁面上所有h3標籤
    o_92 = card.find_all("li")[0].text #92
    o_95 = card.find_all("li")[1].text #95
    o_98 = card.find_all("li")[2].text #98
    o_diesel = card.find_all("li")[3].text #超柴
    #print(o_92)
    #print(o_95)
    #print(o_98)
    #print(o_diesel)
    bubble = {
        "type": "bubble",
        "hero": {
            "type": "image",
            "url": "https://storystudio.tw/storage/upload/article/%E4%B8%AD%E6%B2%B9.jpg",
            "size": "full",
            "aspectRatio": "11:10",
            "aspectMode": "cover"
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
            {
                "type": "text",
                "text": "即時油價",
                "weight": "bold",
                "size": "xxl",
                "align": "center"
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "92油價:" +o_92+"元 "+" || "+ "98油價:" +o_98+"元",
                    "size": "md",
                    "margin": "xs"
                },
                {
                    "type": "text",
                    "text": "95油價:" +o_95+"元 "+" || "+ "柴油油價:" +o_diesel+"元",
                    "size": "md",
                    "margin": "sm"
                }
                ],
                "spacing": "xs",
                "margin": "lg"
            }
            ]
        },
        "footer": {
            "type": "box",
            "layout": "vertical",
            "contents": [
            {
                "type": "button",
                "action": {
                "type": "uri",
                "label": "查看更多",
                "uri": "https://www.cpc.com.tw/"
                }
            }
            ]
        }
        }
    return bubble    
    