import boto3
import click
from jinja2 import Template
import os


def get_template_body():
    with open("./src/cfn/template.yaml") as f:
        return f.read()

@click.command()
@click.option('--stack-name')
@click.option('--data-set-id')
@click.option('--revision-id')
def cli(stack_name, data_set_id, revision_id):
    cfn = boto3.client('cloudformation')
    
    print(cfn.create_stack(
        StackName=f"ADX-Glue-Import-{data_set_id}",
        TemplateBody=get_template_body(),
        Capabilities=[
            "CAPABILITY_AUTO_EXPAND",
            "CAPABILITY_IAM",
            "CAPABILITY_NAMED_IAM"
        ],
        Parameters=[
            {
                "ParameterKey": "DatasetID",
                "ParameterValue": data_set_id,
            },
            {

                "ParameterKey": "RevisionID",
                "ParameterValue": revision_id
            }
        ]
    ))

if __name__ == '__main__':
    cli()
