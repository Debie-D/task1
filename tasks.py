aws_cdk import core
aws_cdk import aws_eks as eks
aws_cdk import aws_ec2 as ec2

class EKSClusterStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Create VPC
        vpc = ec2.Vpc(self, "MyVpc", max_azs=3)  # 3 availability zones

        # Create the EKS Cluster
        cluster = eks.Cluster(self, "MyCluster", 
                              default_capacity=2,  # 2 EC2 nodes for the EKS cluster
                              vpc=vpc)

app = core.App()
EKSClusterStack(app, "EKSClusterStack")
app.synth()
