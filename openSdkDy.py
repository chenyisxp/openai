# coding=utf-8

import logging
import os
from openai import OpenAI
from flask import Flask, request
import json
from tips import draw_numbers
# 配置日志
logging.basicConfig(filename='app.log',
                    filemode='w',
                    format='%(name)s - %(levelname)s - %(message)s')
 
# 创建一个日志器
logger = logging.getLogger(__name__)
app = Flask(__name__)
@app.route('/stream_data', methods=['POST'])
def stream_data():
    global before
    # def generate_data():
    #     for i in range(10):  # 示例中生成10次流数据
    #         yield f'{{"data": "{i}"}}\n'  # 假设每次流发送的是JSON数据
    #         import time
    #         time.sleep(1)  # 每秒发送一次

    # return stream_with_context(generate_data())
    # print(request.form)
    # print(request.form.get('jsonparams'))
    jsonparams = request.form.get('jsonparams')
    if jsonparams:
        param = json.loads(jsonparams)
        # let params ={
        #     api_key:'xxxxxxxxx1123213',
        #     model_id:'ep-20240701134229-qh72q'
        # }
    # print(param['api_key'])
    # print(param['model_id'])
    
    
   
    
    if param['demoId']:
        # switch(param['demoId'])
        beforeContent = draw_numbers(param['demoId'])
        print("beforeContent")
        print(param['demoId'])
        if beforeContent:
            shiftWord = {"role": "system", "content": beforeContent}
            param['messages'].insert(0, shiftWord)
        
    
    # print(param['messages'])
    # print('before')
    # print(before)
    
    # return '11'
    # return 'over'
    try:
        client = OpenAI(
            api_key = param['api_key'],
            base_url = param['base_url'],
        )

        # Non-streaming:
        print("----- standard request -----")
#         return """【文本】：1.姐姐是神女，却天生少了一根情丝。&【提示词-分词版本】1.姐姐，冷漠，站立，地点是仙境，背景是云雾，仙草，仙树，仙池，远景镜头，正面拍摄
# 【文本】：2.性格顽劣，经常以欺辱我为乐。&【提示词-分词版本】2.姐姐，得意，手指着我，地点是庭院，背景是花草，石凳，假山，水池，中景镜头，斜角度拍摄
# 【文本】：3.爹娘兄长都说，是我偷走了她的情丝。&【提示词-分词版本】3.爹娘兄长，愤怒，围着我，地点是客厅，背景是桌椅，茶具，屏风，书画，全景镜头，高角度拍摄
# 【文本】：4.叫我处处忍耐，只因这是我生来就欠她的。&【提示词-分词版本】4.我，委屈，低着头，地点是房间，背景是床铺，衣柜，梳妆台，窗户，近景镜头，侧光拍摄
# 【文本】：5.父母偏爱姐姐，事事以她为先。&【提示词-分词版本】5.父母，宠溺，看着姐姐，地点是餐桌，背景是饭菜，餐具，花瓶，蜡烛，中景镜头，正面拍摄
# 【文本】：6.长兄溺爱姐姐，所有珍贵的东西都如同流水一般送给她。&【提示词-分词版本】6.长兄，开心，拿着礼物，地点是花园，背景是花朵，蝴蝶，亭子，走廊，远景镜头，低角度拍摄
# 【文本】：7.就连我那从小定下婚约的竹马，也是在遇难时毫不犹豫地抛下我。&【提示词-分词版本】7.竹马，决绝，转身离开，地点是山林，背景是树木，草丛，山路，悬崖，全景镜头，逆光拍摄
# 【文本】：8.后来，我一步步跪上仙山。&【提示词-分词版本】8.我，坚定，跪着前行，地点是仙山台阶，背景是云雾，山峰，寺庙，神像，远景镜头，正面拍摄
# 【文本】：9.求仙人抽走我体内的情丝，来换取他们一家人圆满。&【提示词-分词版本】9.我，虔诚，双手合十，地点是仙殿，背景是仙桌，仙椅，仙灯，香炉，特写镜头，侧光拍摄
# 【文本】：10.从此我再无七情六欲，我孑然一身。&【提示词-分词版本】10.我，冷漠，独自站立，地点是荒野，背景是枯草，风沙，落日，孤狼，全景镜头，逆光拍摄
# 【文本】：11.活得没心没肺，他们却又红着眼。&【提示词-分词版本】11.他们，伤心，看着我，地点是庭院，背景是花草，石凳，假山，水池，中景镜头，斜角度拍摄
# 【文本】：12.小心翼翼地来摸我的头：，我求求你。&【提示词-分词版本】12.他们，哀求，伸手摸我头，地点是房间，背景是床铺，衣柜，梳妆台，窗户，近景镜头，侧光拍摄
# 【文本】：13.对我笑一笑好不好，但我不明白他们为什么要哭。&【提示词-分词版本】13.他们，哭泣，看着我笑，地点是客厅，背景是桌椅，茶具，屏风，书画，全景镜头，高角度拍摄
# 【文本】：14.明明这一切，是他们想要的啊。&【提示词-分词版本】14.我，疑惑，看着他们，地点是庭院，背景是花草，石凳，假山，水池，中景镜头，斜角度拍摄"""
#         return """【文本】: 1. 做过新娘的都知道，婚礼应该是最幸福的时刻。&【提示词-分词版本】1.女主角，面带微笑，手捧鲜花，地点是婚礼现场，背景是婚礼舞台，鲜花拱门，香槟塔，宾客座椅，气球，全景镜头，柔和光线
# 【文本】: 2. 可我的婚礼，却被老公的青梅搅得一塌糊涂。&【提示词-分词版本】2.女主角，震惊的表情，呆立原地，地点婚礼现场，背景是混乱的场景，翻倒的桌椅，洒落的花瓣，破碎的酒杯，惊恐的宾客，中景镜头，顶光照射
# 【文本】: 3. 她割腕大闹，老公竟毫不犹豫地抱着她离开。&【提示词-分词版本】3.老公，紧张的表情，抱着青梅，地点婚礼现场，背景是血迹，围观人群，哭泣的新娘，摔倒的花瓶，凌乱的地毯，近景镜头，侧光
# 【文本】: 4. 而我却在绝望中发现自己怀的竟是双胞胎。&【提示词-分词版本】4.女主角，绝望的凝视，手抚肚子，地点婚礼现场，背景是黯淡的灯光，丢弃的头纱，地上的首饰，飘落的彩带，破碎的心形装饰，特写镜头，逆光
# 【文本】: 5. 答应嫁给老公前，我知道他有个青梅。&【提示词-分词版本】5.女主角，忧虑的皱眉，坐在沙发上，地点家中客厅，背景是茶几，沙发抱枕，窗帘，电视，盆栽，中景镜头，平光
# 【文本】: 6. 但双方恩断义绝，覆水难收。&【提示词-分词版本】6.女主角，决绝的表情，转身离开，地点街道，背景是路灯，垃圾桶，电线杆，落叶，行人，远景镜头，侧逆光
# 【文本】: 7. 我怀着孕，放心地准备婚礼。&【提示词-分词版本】7.女主角，期待的目光，挑选婚纱，地点婚纱店，背景是各种婚纱，试衣镜，衣架，高跟鞋，头纱，近景镜头，顶光
# 【文本】: 8. 然后，青梅意外失忆了，又变成16岁时的那朵白玫瑰。&【提示词-分词版本】8.青梅，迷茫的眼神，坐在床上，地点医院病房，背景是白色床单，输液瓶，窗户，柜子，椅子，中景镜头，自然光
# 【文本】: 9. 老公让我包容她，让着病人。&【提示词-分词版本】9.老公，严肃的表情，指指点点，地点家中，背景是餐桌，椅子，吊灯，壁画，花瓶，近景镜头，侧光
# 【文本】: 10. 我的首饰、化妆品、衣服包包，她要就给。&【提示词-分词版本】10.女主角，无奈的表情，递出物品，地点家中卧室，背景是梳妆台，衣柜，床，地毯，窗帘，中景镜头，平光 。"""
        completion = client.chat.completions.create(
            model = param['model_id'],  # your model endpoint ID
            messages = param['messages'],
            temperature= param['temperature']
        )
        print(completion.choices[0].message.content)
        print('anser_end')
        return completion.choices[0].message.content
    except Exception as e:
        # 处理OpenAIError及其子类异常
        print(f"Exception: {e}")
        logger.error('发生错误: {}'.format(e), exc_info=True)  # 将错误信息记录到日志中
        return 'error'
        

if __name__ == '__main__':
    # debug=True
    app.run(host='0.0.0.0', port=5000,debug=True)
    


