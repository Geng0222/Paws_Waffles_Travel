import requests

def get(city): #位置天氣
    token = 'your_api_key_here' #中央氣象局
    url = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=' + token + '&format=JSON&locationName=' + str(city)
    Data = requests.get(url)
    Data = Data.json()['records']['location'][0]['weatherElement']
    res = [[] , [] , []]
    for j in range(1):
        for i in Data:
            res[j].append(i['time'][j])
    situation = res[0][0]['parameter']['parameterName'] #天氣狀況 list-->dict-->str
    #print(situation)
    rain = res[0][1]['parameter']['parameterName']  #降雨機率
    #print(rain)
    note = res[0][3]['parameter']['parameterName']  #注意事項
    #print(note)
    low_temperature = res[0][2]['parameter']['parameterName'] #最低溫度
    #print(low_temperature)
    up_temperature = res[0][4]['parameter']['parameterName'] #最高溫度
    #print(up_temperature) 
    #刻一個FLEX bubble 變數直接帶入
    bubble = {
        "type": "bubble",
        "hero": {
            "type": "image",
            "url": "https://press.ikidane-nippon.com/wordpress/wp-content/uploads/2019/06/a00465_kv.jpg",
            "size": "full",
            "aspectRatio": "20:13",
            "aspectMode": "cover",
            "action": {
            "type": "uri",
            "uri": "http://linecorp.com/"
            }
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
            {
                "type": "text",
                "text": city +"  現在天氣",
                "weight": "bold",
                "size": "xl",
                "align": "center",
                "margin": "sm"
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "天氣狀況: " + situation,
                    "margin": "md",
                    "size": "md"
                },
                {
                    "type": "text",
                    "text": "降雨機率: " + rain,
                    "margin": "md",
                    "size": "md"
                },
                {
                    "type": "text",
                    "text": "溫度: " + low_temperature + " ~ " + up_temperature,
                    "margin": "md"
                },
                {
                    "type": "text",
                    "text": "注意: " + note,
                    "margin": "md"
                }
                ]
            }
            ]
        },
        "footer": {
            "type": "box",
            "layout": "vertical",
            "spacing": "none",
            "contents": [
            {
                "type": "button",
                "style": "link",
                "height": "sm",
                "action": {
                "type": "uri",
                "label": "交通部中央氣象局",
                "uri": "https://www.cwb.gov.tw/V8/C/"
                },
                "margin": "none"
            }
            ],
            "flex": 0
        }
        }
    return bubble

def weather(): #導引天氣
    bubble = {
        "type": "bubble",
        "size": "giga",
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
            {
                "type": "image",
                "url": "https://bravel.yas.com.hk/wp-content/uploads/2020/03/80745625_1330225683814530_2522022551606001664_o.jpg",
                "size": "full",
                "aspectMode": "cover",
                "aspectRatio": "1:1",
                "gravity": "center"
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "點擊左下角加號",
                    "color": "#ffffff",
                    "margin": "md",
                    "size": "lg",
                    "offsetStart": "lg",
                    "offsetTop": "xs"
                },
                {
                    "type": "text",
                    "text": "傳送位置資訊",
                    "color": "#ffffff",
                    "margin": "sm",
                    "size": "lg",
                    "offsetBottom": "none",
                    "offsetStart": "lg",
                    "offsetTop": "xs",
                    "wrap": True
                },
                {
                    "type": "text",
                    "text": "快速回復天氣",
                    "color": "#ffffff",
                    "margin": "sm",
                    "size": "lg",
                    "offsetBottom": "none",
                    "offsetStart": "lg",
                    "offsetTop": "xs",
                    "wrap": True
                }
                ],
                "position": "absolute",
                "paddingAll": "none",
                "paddingBottom": "none",
                "width": "150px",
                "borderWidth": "light",
                "offsetTop": "xs",
                "offsetBottom": "none",
                "offsetStart": "none",
                "offsetEnd": "none",
                "cornerRadius": "none",
                "spacing": "none",
                "margin": "none"
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [],
                "position": "absolute",
                "background": {
                "type": "linearGradient",
                "angle": "0deg",
                "endColor": "#00000000",
                "startColor": "#00000099"
                },
                "width": "100%",
                "height": "40%",
                "offsetBottom": "0px",
                "offsetStart": "0px",
                "offsetEnd": "0px"
            },
            {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "text",
                            "text": "前往中央氣象站",
                            "size": "xl",
                            "color": "#ffffff"
                        }
                        ]
                    }
                    ],
                    "spacing": "xs"
                }
                ],
                "position": "absolute",
                "offsetBottom": "0px",
                "offsetStart": "0px",
                "offsetEnd": "0px",
                "paddingAll": "20px"
            }
            ],
            "paddingAll": "0px"
        },
        "action": {
            "type": "uri",
            "label": "action",
            "uri": "https://www.cwb.gov.tw/V8/C/"
        }
        }
    return bubble