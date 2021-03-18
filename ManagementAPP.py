import paho.mqtt.client as mqtt

mqttc = mqtt.Client()
mqttc.connect("test.mosquitto.org", 1883, 60)

while True:
    print("Please enter your name")
    name = input()
    print("Name entered:", name)

    print("Please set your preferred temperature (Celsius)")
    temp = input()
    print("Temperature entered:", temp)


    mqttc.publish("Family Members", payload=name, qos=0, retain=False)
    mqttc.publish("Preferred Temp", payload=temp, qos=0, retain=False)