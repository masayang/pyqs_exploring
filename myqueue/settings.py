from os.path import join, dirname
from dotenv import load_dotenv
import os
import json


dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


config = {
    "AWS_ACCESS_KEY_ID": os.environ.get("AWS_ACCESS_KEY_ID"),
    "AWS_SECRET_ACCESS_KEY": os.environ.get("AWS_SECRET_ACCESS_KEY")
}


if __name__ == '__main__':
    print json.dumps(config, indent=4)