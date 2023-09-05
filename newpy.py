import paho.mqtt.client as mqtt
import random, time, json, requests
import threading

def start_sendTH():
    t1 = threading.Thread(target=MQTT_SendData)
    t1.start()

def MQTT_SendData():
    #  �豸��������
    ACCESS_TOKEN = "eg0RFrhyRfeiMMmD4xqL"
    # ip��ַ
    broker = "121.37.166.17"
    # �˿�
    port = 1883

    # ʵ����һ���࣬����һ��MQTT�ͻ��˵���
    # �����control1�����Ǹ����MQTT�ͻ�������һ�����֣���������ȡ
    client1 = mqtt.Client("control1")
    client1.username_pw_set(ACCESS_TOKEN)
    client1.connect(broker, port, keepalive=60)

    # һֱ��ͣѭ���ϱ�
    while True:
        # payload��python���ݶ����ʽ��������Ҫ��json.dumpsת��Ϊjson���ݸ�ʽ
        payload = {
            "123543": str(random.randint(1, 10)),
            "nihao": "hello",
            "co2": str(random.randint(10, 500))
        }
        # �ϱ�����
        client1.publish("v1/devices/me/telemetry", json.dumps(payload))
        time.sleep(2)

def getToken(username: str, password: str):
    payload = {
        "password": password,
        "username": username
    }
    _ = requests.post(url=login_url, json=payload)
    token = _.json()['token']
    return str(token)

def getData(in_token):
    url = "http://tb.nlecloud.com/api/plugins/telemetry/DEVICE/10467650-4a26-11ee-a1f2-2ffdc8ae4b85/values/timeseries"

    head = {"X-Authorization": "Bearer " + in_token}

    par = {
        "keys": "123543,co2",
        "useStrictDataTypes": False
    }

    aguidjk = requests.get(url=url, params=par, headers=head)

    print(aguidjk.json())
    return aguidjk.json()['co2'][0]['value']




start_sendTH()
username = "18843210010@mail.com.cn"
password = "n18843210010L"

login_url = 'http://121.37.166.17:80/api/auth/login'

while True:
    token = getToken(username, password)
    print(getData(token))
    time.sleep(2)
