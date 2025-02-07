from bs4 import BeautifulSoup
import requests


def news_travel():    
    url = 'https://travel.ettoday.net/focus/%E6%9A%A2%E9%81%8A%E5%8F%B0%E7%81%A3/?from=travel_MainMenu_PC'
    res = requests.get(url, verify=False)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text,'html.parser') 
    cards = soup.find_all("div",class_="box_0 clearfix",limit = 10)
    Card = {"type":"carousel","contents":[]} #蓋子
    for card in cards :
        title = card.find("h3").find("a").getText()
        #print(title) #取標題
        href = card.find("h3").find("a").get("href")
        #print("https://travel.ettoday.net"+ href ) #取連結
        img = card.find("a").find("img").get("data-original")
        #print("https:"+ img) #取照片
        datea = card.find("em").getText()
        #print(datea) #取時間
        bubble = {
            "type": "bubble",
            "hero": {
                "type": "image",
                "url": "https:"+ img,
                "size": "full",
                "aspectRatio": "200:150",
                "aspectMode": "cover"
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "旅遊新聞",
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
                        "text": title,
                        "wrap": True,
                        "margin": "xxl",
                        "size": "lg",
                        "style": "italic"
                    }
                    ]
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": datea,
                        "size": "sm",
                        "margin": "xxl"
                    }
                    ]
                }
                ]
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "spacing": "sm",
                "contents": [
                {
                    "type": "button",
                    "style": "link",
                    "height": "sm",
                    "action": {
                    "type": "uri",
                    "label": "查看更多",
                    "uri": "https://travel.ettoday.net"+ href
                    }
                }
                ],
                "flex": 0
            }
            }       
        Card['contents'].append(bubble)  # 蓋子 + 瓶子
    return Card #回傳組合體

def news_food():    
    url = 'https://travel.ettoday.net/focus/%E7%BE%8E%E9%A3%9F%E5%9C%B0%E5%9C%96/?from=travel_MainMenu_PC'
    res = requests.get(url, verify=False)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text,'html.parser') 
    cards = soup.find_all("div",class_="box_0 clearfix",limit = 10)
    Card = {"type":"carousel","contents":[]} #蓋子
    for card in cards :
        title = card.find("h3").find("a").getText()
        #print(title) #取標題
        href = card.find("h3").find("a").get("href")
        #print("https://travel.ettoday.net"+ href ) #取連結
        img = card.find("a").find("img").get("data-original")
        #print("https:"+ img) #取照片
        datea = card.find("em").getText()
        #print(datea) #取時間
        bubble = {
            "type": "bubble",
            "hero": {
                "type": "image",
                "url": "https:"+ img,
                "size": "full",
                "aspectRatio": "200:150",
                "aspectMode": "cover"
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "美食新聞",
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
                        "text": title,
                        "wrap": True,
                        "margin": "xxl",
                        "size": "lg",
                        "style": "italic"
                    }
                    ]
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": datea,
                        "size": "sm",
                        "margin": "xxl"
                    }
                    ]
                }
                ]
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "spacing": "sm",
                "contents": [
                {
                    "type": "button",
                    "style": "link",
                    "height": "sm",
                    "action": {
                    "type": "uri",
                    "label": "查看更多",
                    "uri": "https://travel.ettoday.net"+ href
                    }
                }
                ],
                "flex": 0
            }
            }       
        Card['contents'].append(bubble)  # 蓋子 + 瓶子
    return Card #回傳組合體
