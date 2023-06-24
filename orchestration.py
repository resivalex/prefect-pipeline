from dotenv import load_dotenv

load_dotenv()

from prefect_pipeline.my_favorite_function import my_favorite_function
from prefect_pipeline.get_repo_info import get_repo_info


if __name__ == "__main__":
    my_favorite_function()
    get_repo_info()
