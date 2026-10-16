import boto3            

s3 = boto3.resource("s3")

def show_buckets(s3):
    for bucket in s3.buckets.all():       
        print(bucket.name)

def create_bucket(s3,bucket_name,region):
    s3.create_bucket(Bucket = bucket_name , CreateBucketConfiguration={
        "LocationConstraint" : "ap-south-1",
    },)

    print("Bucket Created Successfully")

def upload_backup(s3,file_name,bucket_name,key_name):
    data = open(file_name, "rb")     
    s3.Bucket(bucket_name).put_object(Key=key_name, Body=data)
    print("Backup Upload Successfully")

bucket_name = "python-for-devops-555"
region = "ap-south-1"
create_bucket(s3,bucket_name,region)
show_buckets(s3)
file_name = r"D:\Daily-DevOps-Practice\Python\backups\backup_2026-10-06.tar.gz"     
upload_backup(s3,file_name,bucket_name,"my-backup.tar.gz")