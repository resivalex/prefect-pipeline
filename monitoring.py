import subprocess
from dotenv import load_dotenv


def start_prefect_server():
    load_dotenv()
    subprocess.run(["prefect", "server", "start"], check=True)


if __name__ == "__main__":
    start_prefect_server()
