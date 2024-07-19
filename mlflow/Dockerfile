FROM python:3.11

WORKDIR /mlflow/

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && \
  rm requirements.txt

EXPOSE 5000

CMD mlflow server --host 0.0.0.0 --port 5000 --backend-store-uri ${MLFLOW_BACKEND_STORE_URI} --default-artifact-root ${MLFLOW_DEFAULT_ARTIFACT_ROOT}
