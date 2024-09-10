# hf-finetune-sagemaker

This code allows you to fully finetune a model using aws's multi nodes and fsdp configuration for big models.

## Requirements

* Python 3.11 or higher
* Sagemaker
* HF_TOKEN
* Your AWS RoleName to access AWS's gpus

## Usage Example of [Jamba-1.5-Mini](https://huggingface.co/ai21labs/AI21-Jamba-1.5-Mini)

1. Download or clone the repo to you local computer.
2. Create a new virtual environment based on Python 3.11.
3. Add ```HF_TOKEN``` and ```AWS_ROLE_NAME``` as environment variables.
4. ```pip install sagemaker```
5. Run ```python sagemaker_training.py``` from the main dir.
