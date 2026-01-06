import argparse
from dataclasses import dataclass
from pathlib import Path

@dataclass
class Parameters:
    file_output_active: bool
    path : str
    file_name : str
    broker_IP : str
    broker_port : int
    topic : str


def parsing_for_parameters(args: argparse.Namespace, parameters:Parameters):
    if args.x:
        parameters.file_output_active = True

    if args.o is not None:
        p = Path(args.o)
        print(p.is_dir())

    if args.i is not None:
        print(args.i)

    if args.p is not None and args.p.isnumeric():
        print(args.p)

    if args.t is not None:
        print(args.t)