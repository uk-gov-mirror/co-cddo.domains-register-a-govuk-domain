from aws_cdk import RemovalPolicy, Stack
from aws_cdk import aws_ecr as ecr
from constructs import Construct


class DomainsRegistrationStack(Stack):
    """
    This Stack represents all the resources required to stand up our application
    """

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super(DomainsRegistrationStack, self).__init__(scope, id, **kwargs)

        ecr.Repository(
            self,
            "cddo-domains-registration-ecr",
            repository_name="cddo-domains-registration-ecr",
            image_scan_on_push=True,
            removal_policy=RemovalPolicy.RETAIN,
            lifecycle_rules=[
                ecr.LifecycleRule(
                    max_image_count=5,
                    tag_status=ecr.TagStatus.ANY,
                    description="Keep the last 5 versioned images",
                )
            ],
        )
