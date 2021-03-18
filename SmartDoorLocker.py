import paho.mqtt.client as mqtt

print("Leaving or entering? (1 for entering, 0 for leaving)")
index = input()
print("Code entered:", index)

print("Name of person entering or leaving:")
name = input()
print("Name entered:", name)

mqttc = mqtt.Client()
mqttc.connect("test.mosquitto.org", 1883, 60)
mqttc.publish("Entering/Leaving", payload=index, qos=0, retain=False)
mqttc.publish("Member/entering/leaving", payload=name, qos=0, retain=False)