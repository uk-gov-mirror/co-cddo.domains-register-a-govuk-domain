import aws_cdk as cdk
from infra_stack import DomainsRegistrationStack

app = cdk.App()
DomainsRegistrationStack(app, "domains-registration-stack")

app.synth()
