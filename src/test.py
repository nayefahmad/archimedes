import os

from dotenv import load_dotenv

local_env = "../.env_example"
load_dotenv(local_env)

server = os.getenv("SERVER")
db = os.getenv("POSTGRES_DB")
