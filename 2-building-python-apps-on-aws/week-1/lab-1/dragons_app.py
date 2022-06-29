
import os
import sys
import mimetypes
from os.path import expanduser
import boto3

s3 = boto3.client('s3')
mybucket = os.getenv('MYBUCKET')

def create_dragons_bucket():
  "create a bucket"
  s3.create_bucket(Bucket=mybucket)
  print(f"Created {mybucket}")

def list_all_buckets():
  "list buckets"
  response = s3.list_buckets()

  print('Existing buckets:')
  for bucket in response['Buckets']:
    print(f'  {bucket["Name"]}')

def upload_dragons_app():
  "upload files"
  directory = expanduser('~/webapp1/')

  print('Uploading...')

  for root, _, files in os.walk(directory):
    for file in files:
      full_file = os.path.join(root, file)
      rel_file = os.path.relpath(full_file, directory)
      content_type = mimetypes.guess_type(full_file)[0]
      print(full_file)
      s3.upload_file(full_file, mybucket, 'dragonsapp/' + rel_file,
               ExtraArgs={'ACL': 'public-read','ContentType': content_type})

  print('URL: https://%s.s3.amazonaws.com/dragonsapp/index.html' % (mybucket))

def upload_dragons_data():
  "upload data file"
  cwd = os.getcwd()

  print('Uploading dragon_stats_one.txt')

  s3.upload_file(os.path.join(cwd, 'dragon_stats_one.txt'), mybucket, 'dragon_stats_one.txt')

  s3_resource = boto3.resource('s3')
  bucket = s3_resource.Bucket(mybucket)
  # the objects are available as a collection on the bucket object
  for obj in bucket.objects.all():
    print(obj.key, obj.last_modified)

def put_dragons_parameters():
  "set the SSM parameters"
  client = boto3.client('ssm')

  print('Setting parameter store parameters')

  client.put_parameter(
    Name='dragon_data_bucket_name',
    Value=mybucket,
    Type='String',
    Overwrite=True
  )

  client.put_parameter(
    Name='dragon_data_file_name',
    Value='dragon_stats_one.txt',
    Type='String',
    Overwrite=True
  )

def print_menu():
  "print options menu"
  print("1. Create the dragons bucket")
  print("2. List all buckets")
  print("3. Upload dragons app")
  print("4. Upload dragons data")
  print("5. Set parameter store parameters")
  print("6. Exit")

def main():
  "script requires MYBUCKET environment variable"
  if not mybucket:
    sys.exit("Please set MYBUCKET environment variable")
  loop = True

  while loop:
    print_menu()    ## Displays menu
    choice = input("Enter your choice [1-5]: ")

    if choice=="1":
      create_dragons_bucket()
    elif choice=="2":
      list_all_buckets()
    elif choice=="3":
      upload_dragons_app()
    elif choice=="4":
      upload_dragons_data()
    elif choice=="5":
      put_dragons_parameters()
    elif choice=="6":
      print("Exiting...")
      loop=False
    else:
      input("I don't know that option..")

main()
