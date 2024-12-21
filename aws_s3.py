import boto3
import os
from werkzeug.utils import secure_filename
import botocore.exceptions

def upload_to_s3(file, folder):
    """
    ファイルをAWS S3にアップロードし、公開URLを返す関数。

    Args:
        file: アップロードするファイルオブジェクト
        folder (str): S3バケット内のフォルダパス

    Returns:
        str: アップロードされたファイルのURL
    """
    try:
        # S3クライアントの初期化
        s3 = boto3.client(
            's3',
            aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
            region_name=os.getenv('AWS_REGION')
        )
        
        # バケット名とファイルパス
        bucket_name = os.getenv('S3_BUCKET')
        filename = secure_filename(file.filename)
        s3_path = f"{folder}/{filename}"
        
        # S3にアップロード
        s3.upload_fileobj(file, bucket_name, s3_path, ExtraArgs={"ACL": "public-read"})
        
        # 公開URLを生成
        s3_url = f"https://{bucket_name}.s3.{os.getenv('AWS_REGION')}.amazonaws.com/{s3_path}"
        return s3_url
    
    except botocore.exceptions.BotoCoreError as e:
        print(f"S3 Upload Error: {e}")
        return None