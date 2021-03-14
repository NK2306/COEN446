import paho.mqtt.client as mqtt

mqttc = mqtt.Client()
mqttc.connect(host, port=1883, keepalive=60, bind_address="")
