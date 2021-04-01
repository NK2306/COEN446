import paho.mqtt.client as mqtt

mqttc = mqtt.Client()
mqttc.connect("test.mosquitto.org", 1883, 60)

while True:
    print("Please enter your name")
    name = input()
    if name.isdigit():
        print("Name must be alphabetical")
        continue
    else:
        print("Name entered:", name)
        break

while True:
    print("Please set your preferred temperature (Celsius)")
    temp = input()
    if temp.isdigit():
        print("Temperature entered:", temp)
        print("Publishing data to server:", name + ',' + temp)
        mqttc.publish("Management/App", name + ',' + temp, qos=0, retain=False)
        break
    else:
        print("Temperature must be a numerical value!")
        continue
