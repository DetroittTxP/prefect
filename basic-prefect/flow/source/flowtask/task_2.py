from prefect import task
from prefect.logging import get_run_logger
from prefect.task_worker import serve
import time


@task(task_run_name="Process Data", retries=5, retry_delay_seconds=5)
def task_2_process_data(data: object):
    logger = get_run_logger()
    logger.info("Task 2 is running")

    # Simulate some processing
    for i in range(5):
        logger.info(f"Task 2 processing iteration {i}")
        time.sleep(1)

    logger.info(data)
    logger.info("Task 2 completed")


@task(task_run_name="Save Data", retries=5, retry_delay_seconds=5)
def task_2_save_data(data):
    logger = get_run_logger()
    logger.info("Task 2 is saving data")

    # Simulate saving data
    time.sleep(2)

    logger.info("Task 2 data saved")
    return "Task 2 save result"


if __name__ == "__main__":
    serve(task_2_process_data, task_2_save_data)
