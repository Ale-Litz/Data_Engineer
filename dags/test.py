from hello_operator import HelloOperator
from datetime import datetime, timedelta
from airflow import DAG

with DAG(
  dag_id="test_operator_hello",

  default_args={
    "depends_on_past": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5)
  }

  description="test consult dag",
  schedule=None,
  start)date=datetime(2023, 1, 1),
  catchup=False,
  tags=["DAG test"]
  
) as dag:

  hello_task = HelloOperator(task_id="sample-task", name="data_procurando_entios")

  hello_task
