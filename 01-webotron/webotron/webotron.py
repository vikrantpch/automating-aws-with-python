import boto3
import click

@click.group()
def cli():
    "Webotron deploys websites to AWS"
    pass

@cli.command('list-buckets')
def list_buckets():
    "List All S3 Buckets"
    for bucket in s3.buckets.all():
        print(bucket.name)
    return

@cli.command('list-bucket-objects')
@click.argument('bucket')
def list_bucket_objects(bucket):
    "List Objects in S3 Bucket"
    for obj in s3.Bucket(bucket).objects.all():
        print(obj)
    return

session = boto3.Session(profile_name='pythonAutomation')
s3=session.resource('s3')

if __name__ == '__main__':
    cli()
