
from prefect import flow, task
import time
from prefect.logging import get_run_logger


@task
def fecth_data():
    logger = get_run_logger()
    try:
        logger.info("Fetching data...")
        logger.info("Data fetched")
        return "Data fetched"
    except Exception as e:
        logger.error(f"Error in fecth_data: {e}")
        raise


@task
def process_data(data):
    logger = get_run_logger()
    try:
        logger.info("Processing data...")
        logger.info("Data processed")
        return f"Processed {data}"
    except Exception as e:
        logger.error(f"Error in process_data: {e}")
        raise


@task
def save_data(data):
    logger = get_run_logger()
    try:
        logger.info("Saving data...")
        logger.info("Data saved")
        return f"Saved {data}"
    except Exception as e:
        logger.error(f"Error in save_data: {e}")
        raise


@flow(name="Test Pipeline")
def data_pipeline():
    try:

        data = fecth_data()
        time.sleep(2)
        processed_data = process_data(data)
        time.sleep(2)
        save_data(processed_data)
        time.sleep(2)
    except Exception as e:
        logger = get_run_logger()
        logger.error(f"Error in data pipeline: {e}")
        time.sleep(5)


if __name__ == "__main__":
    i = 0
    while True:
        i += 1
        print(f"Iteration {i}")
        data_pipeline()
