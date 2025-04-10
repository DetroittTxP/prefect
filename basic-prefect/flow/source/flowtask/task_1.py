from prefect import task, flow
from prefect.logging import get_run_logger
from prefect.task_worker import serve
import time


@task(log_prints=True)
def task_1():
    logger = get_run_logger()
    logger.info("Task 1 is running")

    for i in range(10):
        logger.info(f"Task 1 iteration {i}")
        time.sleep(1)
    logger.info("Task 1 completed")
    return "Task 1 result"


@flow(name="Task 1 Flow")
def task_1_flow():
    result = task_1()
    return result


if __name__ == "__main__":
    task_1_flow.serve()
    # Specify the flow)
