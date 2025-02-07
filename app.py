#載入LineBot所需要的模組
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *
from linebot.models import FlexSendMessage
from linebot.models import (
    MessageEvent,
    TextSendMessage,
    ImageSendMessage,
    TemplateSendMessage,
    ButtonsTemplate,
    MessageTemplateAction,
    PostbackEvent,
    PostbackTemplateAction,
    LocationSendMessage,
)
#載入flask模組
from flask import Flask, request, abort
#讀取模組
import configparser
import json
import os
#外部函數模組
from function.scraper_travel import *  
from function.weather import *   
from function.oil_price import*  
from function.stay_map_roda import*
from function.random_statement import*
from function.waffle_secret import* #鬆餅秘方暫時用不到 圖片非http則無法使用
#bert模組
from predict import bert


# LINE 聊天機器人的基本資料 讀取config.ini檔案配置 檔案要放在同個資料夾
app = Flask(__name__)
config = configparser.ConfigParser()
config.read('config.ini')
line_bot_api = LineBotApi(config.get('line-bot', 'channel_access_token'))
handler = WebhookHandler(config.get('line-bot', 'channel_secret'))

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    #將訊息轉換為 json 格式並儲存文字
    json_data = json.loads(body)
    with open('./data.json', 'a', encoding="utf8") as fp:
        json.dump( json_data , fp, indent=3, ensure_ascii=False ) #自動換行 轉換編碼Flase
        fp.write('\n') #json自動空行
    #print( "類別:" +json_data['events'][0]['type'] )  #確認類別
    #print( "文字: " + json_data['events'][0]['message']['text'] ,"\n目的地: " +json_data['destination'] )    
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'   
    
#訊息傳遞區塊
##### 基本上程式編輯都在這個function 
@handler.add(MessageEvent ,message=TextMessage)
def handle_message(event):
    print(event.message.text)
    #不經過bert 可能用於圖文選單
    if event.message.text[0:3] == "@基隆" :                         #1
        content_arr = []
        content_arr.append(TextSendMessage(random_statement(keelung)))
        line_bot_api.reply_message(event.reply_token,content_arr)
        return 0  
    if event.message.text[0:3].replace('臺','台') == "@台北" :      #2
        content_arr = []
        content_arr.append(TextSendMessage(random_statement(Taipei)))
        line_bot_api.reply_message(event.reply_token,content_arr) 
        return 0
    if event.message.text[0:3] == "@新北":                          #3
        content_arr = []
        content_arr.append(TextSendMessage(random_statement(new_Taipei)))
        line_bot_api.reply_message(event.reply_token,content_arr)
        return 0
    if event.message.text[0:3] == "@桃園" :                         #4
        content_arr = []
        content_arr.append(TextSendMessage(random_statement(Taoyuan)))
        line_bot_api.reply_message(event.reply_token,content_arr)
        return 0
    if event.message.text[0:3].replace('臺','台') == "@台中":       #5
        content_arr = []
        content_arr.append(TextSendMessage(random_statement(Taichung)))
        line_bot_api.reply_message(event.reply_token,content_arr)
        return 0
    if event.message.text[0:3].replace('臺','台') == "@台南" :      #6
        content_arr = []
        content_arr.append(TextSendMessage(random_statement(Tainan)))
        line_bot_api.reply_message(event.reply_token,content_arr) 
        return 0   
    if event.message.text[0:3] == "@高雄" :                         #7
        content_arr = []
        content_arr.append(TextSendMessage(random_statement(Kaohsiung)))
        line_bot_api.reply_message(event.reply_token,content_arr) 
        return 0 
    if event.message.text[0:3] == "@新竹" :                         #8
        content_arr = []
        content_arr.append(TextSendMessage(random_statement(Hsinchu)))
        line_bot_api.reply_message(event.reply_token,content_arr) 
        return 0 
    if event.message.text[0:3] == "@苗栗" :                         #9
        content_arr = []
        content_arr.append(TextSendMessage(random_statement(Miaoli)))
        line_bot_api.reply_message(event.reply_token,content_arr) 
        return 0
    if event.message.text[0:3] == "@彰化" :                         #10
        content_arr = []
        content_arr.append(TextSendMessage(random_statement(Changhua)))
        line_bot_api.reply_message(event.reply_token,content_arr) 
        return 0
    if event.message.text[0:3] == "@南投" :                         #11
        content_arr = []
        content_arr.append(TextSendMessage(random_statement(Nantou)))
        line_bot_api.reply_message(event.reply_token,content_arr) 
        return 0
    if event.message.text[0:3] == "@雲林" :                         #12
        content_arr = []
        content_arr.append(TextSendMessage(random_statement(Yilan)))
        line_bot_api.reply_message(event.reply_token,content_arr) 
        return 0
    if event.message.text[0:3] == "@嘉義" :                         #13
        content_arr = []
        content_arr.append(TextSendMessage(random_statement(Chiayi)))
        line_bot_api.reply_message(event.reply_token,content_arr) 
        return 0  
    if event.message.text[0:3] == "@屏東" :                         #14
        content_arr = []
        content_arr.append(TextSendMessage(random_statement(Pingtung)))
        line_bot_api.reply_message(event.reply_token,content_arr) 
        return 0 
    if event.message.text[0:3] == "@宜蘭" :                         #15
        content_arr = []
        content_arr.append(TextSendMessage(random_statement(Yilan)))
        line_bot_api.reply_message(event.reply_token,content_arr) 
        return 0
    if event.message.text[0:3] == "@花蓮" :                         #16
        content_arr = []
        content_arr.append(TextSendMessage(random_statement(Hualien)))
        line_bot_api.reply_message(event.reply_token,content_arr) 
        return 0                               
    if event.message.text[0:3].replace('臺','台') == "@台東" :      #17
        content_arr = []
        content_arr.append(TextSendMessage(random_statement(Taitung)))
        line_bot_api.reply_message(event.reply_token,content_arr) 
        return 0 
    if event.message.text[0:3] == "@澎湖" :                         #18
        content_arr = []
        content_arr.append(TextSendMessage(random_statement(Penghu)))
        line_bot_api.reply_message(event.reply_token,content_arr) 
        return 0 
    if event.message.text[0:3] == "@金門" :                         #19
        content_arr = []
        content_arr.append(TextSendMessage(random_statement(Golden_Gate)))
        line_bot_api.reply_message(event.reply_token,content_arr) 
        return 0  
    if event.message.text[0:3] == "@馬祖" :                         #20
        content_arr = []
        content_arr.append(TextSendMessage(random_statement(mazu)))
        line_bot_api.reply_message(event.reply_token,content_arr) 
        return 0                            
       
    ####################
    #bert啟動器#########  
    text = event.message.text     
    text = bert([text])  #文本分類函式        
    print(text)
    ####################
    if text == "旅遊建議" :   #關鍵字錯誤
        a01 = ["這是我的建議喔~","你覺得這個建議怎麼樣?","給你點我的想法吧~"]
        content_arr = [] 
        content_arr.append(TextSendMessage("需要一點想法嗎?"))
        content_arr.append(TextSendMessage(random_statement(a01)))
        content_arr.append(TextSendMessage(random_statement(travel)))
        line_bot_api.reply_message(event.reply_token,content_arr)
        return 0   

    if text == "建議行程" :  
        content_arr = []
        content_arr.append(TextSendMessage("這是我推薦給你的行程"))
        content_arr.append(TextSendMessage("想查詢縣市地點嗎?麻煩幫我加上@"))
        content_arr.append(TextSendMessage(random_statement(itinerary)))
        line_bot_api.reply_message(event.reply_token,content_arr)
        return 0

    if text == "旅遊規劃" : 
        content_arr = []
        content_arr.append(TextSendMessage("開始規劃囉~"))#隨機語塊
        content_arr.append(TextSendMessage("連結麻煩幫我選擇亞洲台灣喔"))
        content_arr.append(TextSendMessage("https://www.trip-jam.com/viewer/zh_TW"))
        line_bot_api.reply_message(event.reply_token,content_arr)#預計加入使用者幫助
        return 0          
    
    if text == "旅遊新聞": 
        content_arr = []
        content_arr.append(TextSendMessage("以下是最新的旅遊資訊"))
        content_arr.append(FlexSendMessage('旅遊新聞', news_travel()))
        line_bot_api.reply_message(event.reply_token,content_arr)    
        return 0

    if text == "美食新聞": 
        content_arr = []
        content_arr.append(TextSendMessage("以下是最新的美食資訊"))
        content_arr.append(FlexSendMessage('旅遊新聞', news_food()))
        line_bot_api.reply_message(event.reply_token,content_arr)  
        return 0 

    if text == "旅行意義" :         
        content_arr = []
        content_arr.append(TextSendMessage(random_statement(significance)))
        line_bot_api.reply_message(event.reply_token,content_arr)
        return 0         

    if text == "即時油價":
        content_arr = []
        content_arr.append(TextSendMessage("給您的即時油價"))
        content_arr.append(FlexSendMessage('油價', oil_price()))
        line_bot_api.reply_message(event.reply_token,content_arr) 
        return 0   

    if text == "即時路況":
        content_arr = []
        content_arr.append(TextSendMessage("給您的即時路況"))
        content_arr.append(FlexSendMessage('路況', road()))
        line_bot_api.reply_message(event.reply_token,content_arr) 
        return 0  

    if text == "訂房住宿":
        content_arr = []
        content_arr.append(TextSendMessage("給你的訂房網站"))
        content_arr.append(FlexSendMessage('住宿', lodging()))
        line_bot_api.reply_message(event.reply_token,content_arr) 
        return 0       

    if text == "即時氣象":  
        content_arr = []
        content_arr.append(TextSendMessage("查詢天氣狀況"))
        content_arr.append(FlexSendMessage('氣象', weather()))
        line_bot_api.reply_message(event.reply_token,content_arr) 
        return 0 

    if text == "導航地圖":  
        content_arr = []
        content_arr.append(TextSendMessage("找路嗎? 順邊看看周邊景點吧~"))
        content_arr.append(FlexSendMessage('導航', google_map()))
        line_bot_api.reply_message(event.reply_token,content_arr) 
        return 0
    
    if text == "水上運動":
        a02 = ["務必小心安全喔","除了游泳外 均應穿著救生衣喔","趕快出發吧!",]  
        content_arr = []
        content_arr.append(TextSendMessage("水上運動"))
        content_arr.append(TextSendMessage(random_statement(a02)))
        content_arr.append(TextSendMessage(random_statement(dabble)))
        line_bot_api.reply_message(event.reply_token,content_arr)
        return 0 

    if text == "爬山健行": 
        a03 = ["小心山林的昆蟲喔","防蚊液攜帶了嗎?","記得隨時補充水分~",] 
        content_arr = []
        content_arr.append(TextSendMessage("爬山健行"))
        content_arr.append(TextSendMessage(random_statement(a03)))
        content_arr.append(TextSendMessage(random_statement(alpinism)))
        line_bot_api.reply_message(event.reply_token,content_arr)
        return 0    

    if text == "遊樂園": 
        a04 = ["痛快的玩樂吧!","一定要坐旋轉木馬喔"] 
        content_arr = []
        content_arr.append(TextSendMessage("遊樂園"))
        content_arr.append(TextSendMessage(random_statement(a04)))
        content_arr.append(TextSendMessage(random_statement(amusement_park)))
        line_bot_api.reply_message(event.reply_token,content_arr)
        return 0

    if text == "情侶約會":  
        a05 = ["壞壞💑","注意伴侶心情喔~",]
        content_arr = []
        content_arr.append(TextSendMessage("情侶約會"))
        content_arr.append(TextSendMessage(random_statement(a05)))
        content_arr.append(TextSendMessage(random_statement(lovers)))
        line_bot_api.reply_message(event.reply_token,content_arr)
        return 0 

    if text == "家庭出遊":  
        a06 = ["要注意小朋友安全喔","快去跟小朋友玩吧~",]
        content_arr = []
        content_arr.append(TextSendMessage("家庭出遊"))
        content_arr.append(TextSendMessage(random_statement(a06)))
        content_arr.append(TextSendMessage(random_statement(family)))
        line_bot_api.reply_message(event.reply_token,content_arr)
        return 0 

    if text == "休閒娛樂":  
        a07 = ["來點輕鬆的旅程吧","一個人走走也很不錯呢~"]
        content_arr = []
        content_arr.append(TextSendMessage("休閒娛樂"))
        content_arr.append(TextSendMessage(random_statement(a07)))
        content_arr.append(TextSendMessage(random_statement(leisure)))
        line_bot_api.reply_message(event.reply_token,content_arr)
        return 0     
         
    if text == "歡迎":  #打招呼以及使用者幫助 
        greet = ["你好~ 今天過得好嗎?","哈囉~ 工作辛苦啦😄","嗨~ 很開心見到你~", ] 
        content_arr = []
        content_arr.append(TextSendMessage(random_statement(greet)))#隨機語塊
        content_arr.append(TextSendMessage("我是你的旅遊幫手\n希望可以跟你有個愉快的互動\n不管任何問題都可以詢問我喔😉"))
        content_arr.append(TextSendMessage("查詢縣市麻煩幫我加上@ \nex: @台北"))#隨機語塊
        content_arr.append(TextSendMessage("我可以幫助你查詢\n路況、油價、天氣的資訊\n最新的旅遊、美食報導想先了解嗎?\n決定了地點 想訂房也難不倒我喔😄"))
        line_bot_api.reply_message(event.reply_token,content_arr)#預計加入使用者幫助
        return 0     

    if text == "喜歡": 
        like = ["能幫上你的忙我也很高興", "能回答你的問題真是太好了","喜歡嗎? 開始規劃吧~","謝謝你 還可以再問我其他問題喔",] 
        content_arr = []
        content_arr.append(TextSendMessage(random_statement(like)))
        line_bot_api.reply_message(event.reply_token,content_arr)
        return 0   

    if text == "討厭": 
        notlike = ["我很抱歉😢","你不喜歡嗎? 對不起😥","很抱歉😥 沒能幫上你的忙",]
        b01 = ["希望可以再次服務您","您還需要甚麼服務嗎?",]
        content_arr = []
        content_arr.append(TextSendMessage(random_statement(notlike)))
        content_arr.append(TextSendMessage(random_statement(b01)))
        line_bot_api.reply_message(event.reply_token,content_arr)
        return 0   

    if text == "出發" :  
        content_arr = []
        content_arr.append(TextSendMessage("準備好要出發了嗎?"))
        content_arr.append(TextSendMessage("住宿、路況、天氣、隨身物品\n都準備好了嗎?\n出去旅遊請務必小心喔"))
        content_arr.append(TextSendMessage("最重要的是\n要保持一顆愉快的心😊"))
        line_bot_api.reply_message(event.reply_token,content_arr)
        return 0 

    if text == "酒吧夜景" : 
        a08 = ["飲酒要適量喔","答應我! 開車不喝酒","好好的喝個喝爛吧😂",] 
        content_arr = []
        content_arr.append(TextSendMessage(random_statement(a08)))
        content_arr.append(FlexSendMessage('酒吧夜景', night_bar()))
        line_bot_api.reply_message(event.reply_token,content_arr)
        return 0   

    if text == "熱氣球" : 
        a09 = ["熱氣球是有季節性的喔","記得注意活動時間~",] 
        content_arr = []
        content_arr.append(TextSendMessage(random_statement(a09)))
        content_arr.append(FlexSendMessage('熱氣球', hot_air_balloon()))
        line_bot_api.reply_message(event.reply_token,content_arr)
        return 0 

    if text == "畢業旅行" : 
        a10_1 = ["我們會一起畢業的吧","約定好了喔 一起畢業","今天沒課，以後也沒有課了",] 
        a10_2 = ["才沒有畢業旅行的建議勒~","畢旅建議行程? 沒有的喔~","都要畢業旅行了 還在問?"]
        a10_3 = ["願所有新的開始，\n都是離別開出的花。","我們笑著說再見，\n卻深知再見遙遙無期。","拍照三秒的時間，\n卻定格著青春的匆匆歲月。",]
        a10_4 = ["國內畢旅:小琉球","國內畢旅:澎湖","國內畢旅:墾丁","國內畢旅:花東地區"]
        a10_5 = ["國外畢旅:日本京都&奈良、大阪","國外畢旅:印尼峇厘島","國外畢旅:泰國曼谷"]
        content_arr = []
        content_arr.append(TextSendMessage(random_statement(a10_1)))
        content_arr.append(TextSendMessage(random_statement(a10_2)))
        content_arr.append(TextSendMessage(random_statement(a10_3)+"\n還是給你一些大地點吧~"))
        content_arr.append(TextSendMessage(random_statement(a10_4)))
        content_arr.append(TextSendMessage(random_statement(a10_5)))
        line_bot_api.reply_message(event.reply_token,content_arr)
        return 0            
   
@handler.add(MessageEvent, message=LocationMessage)      
def handle_location_message(event):  
    if event.message.type == 'location':  #傳送位置資訊 回傳當地天氣  //只支援縣或市 鄉鎮地區還在想
        city = event.message.address[5:8].replace('台','臺') #字串分割取值，"臺"取代"台"
        print(city)  #顯示擷取到的內容
        content = get(city)
        line_bot_api.reply_message(event.reply_token,FlexSendMessage('天氣', content)) 
        return 0 

#主程式
import os 
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8022))
    app.run(host='0.0.0.0', port=port)    

