from flask import Flask, request, jsonify
import openai

application = Flask(__name__)

@application.route("/")
def hello():
    return "<h1>Hello goorm!</h1>"

# OpenAI API 키 설정
api_key = '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'  # 실제 API 키로 변경해주세요
openai.api_key = api_key

@application.route("/mykakao", methods=['POST'])
def mykakao():
    req = request.get_json()  # 클라이언트 쪽에서 보낸 메시지를 JSON으로 변환
    usrTxt = req['userRequest']['utterance']  # 실제로 카카오톡에 적힌 메시지

    # OpenAI API로 사용자 메시지를 전송하여 응답 받기
    response_from_gpt = get_chat_response(usrTxt)

    responseBody = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    'simpleText': {
                        'text': usrTxt
                    }
                },
                {
                    'simpleText': {
                        'text': response_from_gpt  # OpenAI GPT에서 받은 응답 사용
                    }
                }
            ]
        }
    }
    return jsonify(responseBody)

def get_chat_response(message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # 사용할 GPT 모델 선택
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message}
        ],
        temperature=0.7,
        max_tokens=50
    )

    if response and 'choices' in response.keys() and len(response['choices']) > 0:
        return response['choices'][0]['message']['content']
    else:
        return "챗GPT가 응답하지 않았어요."

if __name__ == "__main__":
    application.run(host='0.0.0.0', port=5000, threaded=True)
