# front.py - visible interface

import json
from gate import Sluice

def main():
    print("Nak Utility v1.0")
    print("1. Test translation")
    print("2. Exit")
    choice = input("> ")

    if choice == "1":
        s = Sluice("test", "test")
        result = s.translate({"sample": "data"})
        print("Result:", json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
