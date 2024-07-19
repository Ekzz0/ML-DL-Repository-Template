import os
import subprocess

from dotenv import load_dotenv

load_dotenv()


def run_command(command: str) -> None:
    """Выполняет указанную команду"""
    subprocess.run(command, shell=True, check=True)


def setup_mlflow_server() -> None:
    """Запускает MLflow сервер с заданными переменными окружения"""

    try:
        # Формирование команды для запуска MLflow сервера
        mlflow_command = (
            f'mlflow server --host 0.0.0.0 --port {os.getenv("MLFLOW_PORT")} '
            f'--backend-store-uri {os.getenv("BACKEND_STORE_URI")} '
            f'--default-artifact-root {os.getenv("MLFLOW_S3_REMOTE_URL")} '
            f'--artifacts-destination {os.getenv("MLFLOW_S3_REMOTE_URL")} '
        )

        # Запускаем БД
        run_command("docker-compose up -d")

        # Запуск MLflow сервера
        run_command(mlflow_command)
    except KeyboardInterrupt:
        pass
    finally:
        run_command("docker-compose stop")


if __name__ == "__main__":
    setup_mlflow_server()
