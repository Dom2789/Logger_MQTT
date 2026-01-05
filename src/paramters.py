from dataclasses import dataclass

@dataclass
class Parameters:
    path : str
    file_name : str
    broker_IP : str
    broker_port : int
    topic : str

