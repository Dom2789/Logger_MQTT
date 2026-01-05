from src.paramters import Parameters
from src.mqtt import MQTT
def main():
    print("Hello from logger-mqtt!")



    MQTT_SERVER = "192.168.178.100"
    MQTT_PATH = "climate/office/+"

    parameters = Parameters("", "logfile.txt", "local.host", 1883, "topic")
    parameters = Parameters("", "logfile.txt", "192.168.178.100", 1884, "climate/office/+")

    mqtt = MQTT(parameters)
    mqtt.subscribe()



if __name__ == "__main__":
    main()
