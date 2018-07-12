from yalgaar import Yalgaar

key = 'YourClientKey'

def on_connect(code, error_str):
     print(error_str)

def on_message(topic, data):
     print(data)

def on_presence(data):
     print(data)

def on_error(data):
     print(data)

objYalgaar = Yalgaar()
objYalgaar.yalgaarConnect(key, False, on_connect, None, None, None)
objYalgaar.yalgaarSubscribe('ChannelName', on_message, on_presence, on_error)
objYalgaar.yalgaarPublish('ChannelName', 'This is Yalgaar Python SDK Example')
objYalgaar.yalgaarUnSubscribe('ChannelName')
objYalgaar.loop_forever()

#following code can also be used instead of loop_forever API.
#while True:
#    objYalgaar.loop()