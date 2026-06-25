import aws_cdk as cdk
from api_stack import DomainsRegistrationStack

app = cdk.App()
DomainsRegistrationStack(app, "domains-registration-stack")

app.synth()
