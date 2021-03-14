import paho.mqtt.client as mqtt

print("Please enter your name")
name = input()
print("Name entered:", name)

print("Please et your preferred temperature (Celsius)")
temp = input()
print("Temperature entered:", temp)

mqttc = mqtt.Client()
mqttc.connect(host, port=1883, keepalive=60, bind_address="")