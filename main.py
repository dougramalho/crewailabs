import argparse
import src.lab as lab

def execute(tool):
    
    if(tool == "lab"):
        lab.main()


if __name__ == "__main__":

    parser = argparse.ArgumentParser("Comunidade de agentes")

    parser.add_argument("tool", choices=["lab"], help="Agentes disponíveis: lab")

    args = parser.parse_args()

    execute()