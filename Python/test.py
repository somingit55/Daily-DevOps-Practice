import shutil
import datetime
import os


def backup_files(source, destination):
    today = datetime.date.today()

    backup_files_name = os.path.join(
        destination,
        f"backup_{today}"
    )

    shutil.make_archive(
        backup_files_name,
        "gztar",
        source
    )

source = "/d/Daily-DevOps-Practice/Python"
destination = "/d/Daily-DevOps-Practice/Python/backups"

backup_files(source, destination)