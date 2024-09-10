import sagemaker
import boto3
from sagemaker.huggingface import HuggingFace
import os
os.environ["AWS_DEFAULT_REGION"] = 'us-west-2'

try:
    role = sagemaker.get_execution_role()
except ValueError:
    iam = boto3.client('iam')
    assert 'AWS_ROLE_NAME' in os.environ, "AWS RoleName is required. Add AWS_ROLE_NAME env var value"
    role = iam.get_role(RoleName=os.environ["AWS_ROLE_NAME"])['Role']['Arn']

TORCH_DIST = {
    "torch_distributed": {
        "enabled": True
    }
} 

assert 'HF_TOKEN' in os.environ, "HF_TOKEN is required. Add HF_TOKEN env var value"
# creates Hugging Face estimator
huggingface_estimator = HuggingFace(
    distribution=TORCH_DIST,
    entry_point='run_sft.py',
    source_dir='sagemaker_training',
    instance_type='ml.p4d.24xlarge',
    instance_count=8,
    role=role,
    transformers_version='4.36.0', # will be updated later via sagemaker_training/requirements.txt
    pytorch_version='2.1.0',
    py_version='py310',
    keep_alive_period_in_seconds=60*60,
    environment={"HF_TOKEN": os.environ["HF_TOKEN"],
                 "TRANSFORMERS_CACHE": "/dev/shm/transformers_cache"})

# starting the train job
huggingface_estimator.fit()