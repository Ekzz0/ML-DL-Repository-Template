import os

from dotenv import load_dotenv

# Загрузка переменных окружения из файла
env_path = ".env"
load_dotenv(dotenv_path=env_path)

# Получение значений из переменных окружения
remote_name = os.getenv("DVC_REMOTE_NAME")
remote_url = os.getenv("DVC_REMOTE_URL")
endpoint_url = os.getenv("S3_API_HOST")
access_key_id = os.getenv("S3_ACCESS_KEY")
secret_access_key = os.getenv("S3_SECRET_KEY")
use_ssl = os.getenv("DVC_USE_SSL")

# Настройка DVC удаленного хранилища
os.system(f"dvc remote add -d {remote_name} {remote_url}")
os.system(f"dvc remote modify {remote_name} endpointurl {'https://' + endpoint_url}")
os.system(f"dvc remote modify {remote_name} access_key_id {access_key_id}")
os.system(f"dvc remote modify {remote_name} secret_access_key {secret_access_key}")
os.system(f"dvc remote modify {remote_name} use_ssl {use_ssl}")

print("DVC configuration has been set up.")
