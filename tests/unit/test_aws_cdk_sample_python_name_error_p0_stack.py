import aws_cdk as core
import aws_cdk.assertions as assertions

from aws_cdk_sample_python_name_error_p0.aws_cdk_sample_python_name_error_p0_stack import AwsCdkSamplePythonNameErrorP0Stack

# example tests. To run these tests, uncomment this file along with the example
# resource in aws_cdk_sample_python_name_error_p0/aws_cdk_sample_python_name_error_p0_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = AwsCdkSamplePythonNameErrorP0Stack(app, "aws-cdk-sample-python-name-error-p0")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
