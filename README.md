# Logger MQTT
Logger subscribes to a single topic and outputs received messages to command line and optional to file.

## CLI parameters
All parameters are optional, if non is given default value is used.  

-x : if used, output to file is active
-o "logfile.txt": path and name of logfile  
-t "topic": topic to subscribe to  
-i "local.host": IP-address of MQTT-broker  
-p "1883": port of broker  
