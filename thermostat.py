import paho.mqtt.client as mqtt

class UserInfo:
    def __init__(self, name, temp, status):
    self.name = name
    self.temp = temp
    self.status = status

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("$SYS/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

#Add new user profile from the management app
def add_new_user(dicts, userName, preferredTemp)
    if userName in dicts:
        print("Name is already in use. Please pick a different name")
    else:
        dicts[userName] = UserInfo(userName, preferredTemp, 0)

#Update new desired temperature for everyone in the house at the moment
def update_new_temp(dicts)
    sum = 0
    count = 0;
    for key in dicts:
        if(dicts[key].status == 1):
            sum = sum + dicts[key].temp
            count = count + 1
    
    return sum/count

#Update new user status to check if they are inside the house
def update_user_status(dicts, userName, status)
    if userName in dicts:
        dicts[userName].status = status
    else
        print("Unknown user. Can't update his/her status")
    
def main():
    #Create and connect the MQTT client to the broker server
    client = mqtt.Client()
    client.on_connect = on_connect
    #client.on_message = on_message
    
    client.connect("test.mosquitto.org", 1883, 60)

    # Blocking call that processes network traffic, dispatches callbacks and
    # handles reconnecting.
    # Other loop*() functions are available that give a threaded interface and a
    # manual interface.
    client.loop_forever()
    
if __name__ == "__main__":
    main()

