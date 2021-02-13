import requests
import json

sid="4976046362181531851"
token="d960806d9168f993c648ce91be8c290bb8765"
topic="1613135078445088815"
message="hello from python"
def get_chat_messages(sid, token, topic, size):
    headers={'X-Token':token, 'Session-ID':sid}
    url="https://capture.chat/api/topic/"+topic+"/message?count="+size
    request=requests.get(url, headers=headers)
    response=json.loads(request.text)
    print (response)


def send_message(token,sid,topic,message):
	headers={'X-Token':token,'Session-ID':sid}
	data={
	'text':message
	}
	data=json.dumps(data)
	url='https://capture.chat/api/topic/'+topic+'/message'
	request=requests.post(url=url,headers=headers,data=data)
	response=json.loads(request.text)
	print(response)


#https://capture.chat/api/topic//message?random_id=1613177037148294523