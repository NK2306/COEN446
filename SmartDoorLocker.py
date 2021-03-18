import paho.mqtt.client as mqtt

mqttc = mqtt.Client()
mqttc.connect("test.mosquitto.org", 1883, 60)

while True:
    print("Leaving or entering? (1 for entering, 0 for leaving)")
    index = input()
    print("Code entered:", index)

    print("Name of person entering or leaving:")
    name = input()
    print("Name entered:", name)

    mqttc.publish("Smart/Locker", index+name, qos=0, retain=False)
