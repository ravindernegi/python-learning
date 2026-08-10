import pandas
import numpy
import fastapi
import requests


def main():
    print("Project is running!")
    print("Requests:", requests.__version__)
    print("Pandas:", pandas.__version__)
    print("NumPy:", numpy.__version__)
    print("FastAPI:", fastapi.__version__)


if __name__ == "__main__":
    main()
