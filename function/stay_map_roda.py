
def lodging(): #訂房
    bubble = {
            "type": "bubble",
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "image",
                    "size": "full",
                    "aspectMode": "cover",
                    "aspectRatio": "1:1",
                    "gravity": "center",
                    "url": "https://play-lh.googleusercontent.com/eJuvWSnbPwEWAQCYwl8i9nPJXRzTv94JSYGGrKIu0qeuG_5wgYtb982-2F_jOGtIytY"
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
                                "text": "前往訂房",
                                "size": "xxl",
                                "color": "#ffffff",
                                "margin": "none"
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
                "paddingAll": "0px",
                "action": {
                "type": "uri",
                "label": "action",
                "uri": "https://www.booking.com/index.zh-tw.html?aid=376396;label=booking-name-yefrPbbyS*FIINHgyCnmNgS267725091255:pl:ta:p1:p22,563,000:ac:ap:neg:fi:tikwd-65526620:lp9040292:li:dec:dm:ppccp=UmFuZG9tSVYkc2RlIyh9YfqnDqqG8nt1O4nYvDr1lms;ws=&gclid=CjwKCAjw6MKXBhA5EiwANWLODLuJ5v1SIAIZvloQ6hBL8gvSJ7OBTLlNQk4Wz3MStciy03xfR2ZBWhoCwRYQAvD_BwE"
                }
            }
            }
    return bubble

def google_map(): #地圖
    bubble = {
      "type": "bubble",
      "size": "giga",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://res.klook.com/image/upload/q_85/c_fill,w_750/fl_lossy.progressive/q_auto/blogtw/2018/06/%E5%8F%B0%E5%8C%97101%E8%A7%80%E6%99%AF%E5%8F%B0%E9%96%80%E7%A5%A8.jpg",
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "1:1",
            "gravity": "center"
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
                        "text": "前往Google地圖",
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
        "uri": "https://www.google.com.tw/maps/place/%E5%8F%B0%E7%81%A3/@23.7701324,120.7352226,7.75z/data=!4m5!3m4!1s0x346ef3065c07572f:0xe711f004bf9c5469!8m2!3d23.4512782!4d121.2615967?hl=zh-TW"
      }
    }

    return bubble

def road(): #路況
    bubble = {
            "type": "bubble",
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "image",
                    "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b9/Autobahnnetz_Taiwan.svg/800px-Autobahnnetz_Taiwan.svg.png",
                    "size": "full",
                    "aspectMode": "cover",
                    "aspectRatio": "1.1:1.5",
                    "gravity": "center"
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
                                "text": "即時路況",
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
                "paddingAll": "0px",
                "action": {
                "type": "uri",
                "label": "action",
                "uri": "https://1968.freeway.gov.tw/"
                }
            },
            "size": "giga"
            }
    return bubble  

def night_bar(): #酒吧夜景
  bubble = {
      "type": "bubble",
      "size": "giga",
      "hero": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://assets.funliday.com/posts/wp-content/uploads/2022/08/09124931/limeishu-1-1024x1024.jpg",
            "size": "full"
          },
          {
            "type": "text",
            "text": "Google 酒吧推薦",
            "offsetTop": "none",
            "color": "#FFFFFF",
            "offsetBottom": "xl",
            "offsetStart": "xxl",
            "offsetEnd": "none",
            "position": "absolute",
            "gravity": "bottom",
            "size": "xl"
          }
        ]
      },
      "action": {
        "type": "uri",
        "label": "action",
        "uri": "https://www.google.com.tw/maps/search/%E9%85%92%E5%90%A7%E5%A4%9C%E6%99%AF/@24.4010173,120.71359,9.5z/data=!4m4!2m3!5m1!4e9!6e5?hl=zh-TW"
      }
    }

  return bubble

def hot_air_balloon(): #熱氣球
  bubble = {
      "type": "bubble",
      "size": "giga",
      "hero": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://taiwan.sharelife.tw/tw-news-img/49770/1619230120415923.jpg",
            "size": "full",
            "offsetTop": "none",
            "offsetBottom": "none",
            "offsetEnd": "none",
            "offsetStart": "none",
            "aspectMode": "cover"
          },
          {
            "type": "text",
            "offsetTop": "lg",
            "color": "#484891",
            "offsetBottom": "none",
            "offsetStart": "lg",
            "offsetEnd": "none",
            "position": "absolute",
            "gravity": "top",
            "size": "xl",
            "text": "台灣國際熱氣球嘉年華",
            "margin": "none"
          }
        ]
      },
      "action": {
        "type": "uri",
        "label": "action",
        "uri": "https://balloontaiwan.taitung.gov.tw/zh-tw"
      }
  }

  return bubble
