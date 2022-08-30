from aws_cdk.core import (
    Stack,
    Construct,
)
from aws_cdk.aws_ec2 import Vpc
from aws_cdk.aws_elasticloadbalancingv2 import ApplicationLoadBalancer

class AwsCdkSamplePythonNameErrorP0Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        vpc = Vpc.from_lookup(self, 'VPC', is_default=True)

        lb = ApplicationLoadBalancer(
            self, "MainLB",
            vpc=vpc,
            vpc_subnets={
                'subnet_group_name': "Public"
            },
            internet_facing=True
        )
