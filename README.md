# hf-finetune-sagemaker

This code allows you to fully finetune a model via Hugging Face using AWS's multi nodes and FSDP configuration for big models.

## Requirements

* Python 3.10 or higher
* Sagemaker
* HF_TOKEN - Hugging Face's user access token with read and write permissions
* Your AWS RoleName to access AWS's gpus

## Usage example for [Jamba-1.5-Mini](https://huggingface.co/ai21labs/AI21-Jamba-1.5-Mini)

1. Download or clone the repo to you local computer.
2. Create a new virtual environment based on Python >= 3.10.
3. Add ```HF_TOKEN``` and ```AWS_ROLE_NAME``` as environment variables.
4. ```pip install sagemaker``` (and ```pip install setuptools``` in case of python >= 3.12)
5. Run ```python sagemaker_training.py``` from the main dir.

Track your job in [AWS training dashboard](https://console.aws.amazon.com/sagemaker/home?#/jobs)
