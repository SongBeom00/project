from flask import Flask,request,jsonify
import sys

application = Flask(__name__)


@application.route("/")
def hello():
    return "<h1>Hello goorm!</h1>"

@application.route("/mykakao",methods=['POST']) 
def mykakao():
    req= request.get_json() #클라이언트 쪽에서 보낸 메시지를 json화 한 것
    print(req) #클라이언트 측에서 보낸 메시지 프린트해보기
    usrTxt=req['userRequest']['utterance'] #실제로 카톡에 적힌 메시지
    responseBody={
        "version" : "2.0", # 카톡 가이드 문서 참조
        "template" : {
            "outputs" : [
                {
                'simpleText' : {
                    'text' : usrTxt
                }
              },
                               {
                   'simpleText' : {
                         'text' : "최재혁 롤 개못함"
                }
              }
            ]
        }
    }
    return responseBody


if __name__ == "__main__":
    application.run(host='0.0.0.0', port=5000, threaded=True)