from src.paramters import Parameters, parsing_for_parameters
from src.mqtt import MQTT
import argparse

def main():
    print("Hello from logger-mqtt!")

    # default values
    parameters = Parameters(False, "", "logs/logfile.txt", "192.168.178.100", 1884, "climate/office/+")

    # parsing command-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-x", action="store_true")
    parser.add_argument("-o", help= "name or full path of logfile")
    parser.add_argument("-i", help= "IP of MQTT-broker")
    parser.add_argument("-p", help= "port of MQTT-broker")
    parser.add_argument("-t", help= "topic to subscribe to")
    args = parser.parse_args()

    parsing_for_parameters(args, parameters)

    print(parameters.__repr__())

    # instantiation of MQTT-class and subscribe to topic
    #mqtt = MQTT(parameters)
    #mqtt.subscribe()



if __name__ == "__main__":
    main()
