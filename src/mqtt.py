import paho.mqtt.client as mqtt
from src.paramters import Parameters


class MQTT:
    def __init__(self, parameters: Parameters):
        self.path = parameters.path
        self.file_name = parameters.file_name
        self.broker_IP = parameters.broker_IP
        self.broker_port = parameters.broker_port
        self.topic = parameters.topic


    # The callback for when the client receives a CONNACK response from the server.
    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code " + str(rc))

        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        client.subscribe(self.topic)

    # The callback for when a PUBLISH message is received from the server.
    def on_message(self, client, userdata, msg):
        print(msg.topic + " " + msg.payload.decode())
        # more callbacks, etc

    # subscribe method
    def subscribe(self):
        client = mqtt.Client(protocol=mqtt.MQTTv311, transport="tcp")
        client.on_connect = self.on_connect
        client.on_message = self.on_message

        client.connect(self.broker_IP, self.broker_port, 60, bind_address="0.0.0.0")
        print(f"subcribed to topic: {self.topic}")

        # Blocking call that processes network traffic, dispatches callbacks and
        # handles reconnecting.
        # Other loop*() functions are available that give a threaded interface and a
        # manual interface.
        client.loop_forever()