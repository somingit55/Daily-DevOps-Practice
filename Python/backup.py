import shutil
import datetime
import os
def backup_files(source,destination):
    today = datetime.date.today()
    backup_files_name = os.path.join(destination, f"backup_{today}")
    shutil.make_archive(backup_files_name,"gztar",source)

source = r"D:\Daily-DevOps-Practice\Python"
destination = r"D:\Daily-DevOps-Practice\Python\backups"
backup_files(source,destination)