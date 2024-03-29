from celery import shared_task

from time import sleep


@shared_task(bind=True)
def process_file(self):
    """Background tasl"""
    print("\n Started Background Task\n")
    sleep(3)
    print("\n Completed Background Task\n")