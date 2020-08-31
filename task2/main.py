from celery import Celery
from download import download_comics

app = Celery("app")
app.config_from_object("celeryconfig")


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(3600.0, download_task.s())


@app.task
def download_task():
    print("Execute download task")
    download_comics()
