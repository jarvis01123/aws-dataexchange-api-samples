## Glue Cloudformation Example
This example includes a Cloud Formation template to create a data pipeline from one of your AWS Data Exchange entitled data sets to automatically index new Revisions into a Glue data catalog. Once the data is in a Glue catalog it immediately becomes available in a number of different AWS analytics tools such as Athena, QuickSight, and Elastic Map Reduce.

## Running the sample
This template takes 2 parameters:

```
DatasetID - Required. Creates a data pipeline from this Data set into Glue.
RevisionID - Optional. If given, this revision will be loaded when the Stack is created.
```

Make sure that you have already subscribed to this Data set on AWS Data Exchange and that you can see the data set in your console under "Entitled Data sets."

You can either upload this template to the Cloud Formation console, or create the stack directly from the command line:

```
$ aws cloudformation create-stack \
    --stack-name="ADXGlueCrawlerStack" \
    --template-body="$(cat ./src/cfn/template.yaml)" \
    --capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND \
    --parameters ParameterKey=DatasetID,ParameterValue=ec7d4c68bef299bcd70815e6e91f4caf \
                 ParameterKey=RevisionID,ParameterValue=9ecc2e15dd21ba5d10fc8ffde42050c3
```
