import paho.mqtt.client as mqtt

mqttc = mqtt.Client()
mqttc.connect("localhost", 1883, 60)

while True:
    while True:
        print("Leaving or entering? (1 for entering, 0 for leaving)")
        index = input()
        if index.isdigit():
            print("Code entered:", index)
            break
        else:
            print("Please type in 1 or 0")
            continue

    while True:
        print("Name of person entering or leaving:")
        name = input()
        if name.isdigit():
            print("Name must be alphabetical")
            continue
        else:
            print("Name entered:", name)
            print("Publishing data to server:", name + ',' + index)
            mqttc.publish("Smart/Locker", name + ',' + index, qos=0, retain=False)
            break


