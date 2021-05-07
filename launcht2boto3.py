import boto3
### Creates in AWS: 2 new users with CLI access keys and runs a CloudFormation stack with one t2.micro.

# Creates a CF stack from t2config.yaml
cf_client = boto3.client('cloudformation')
cf_template = open('t2config.yaml').read()
cf_client.create_stack(StackName='myec2wSSH', TemplateBody=cf_template)


# Creates two users with EC2 full access and creates an AWS CLI access key for each user.
iam = boto3.client('iam')
user1 = iam.create_user(UserName='user1',
				PermissionsBoundary='arn:aws:iam::aws:policy/AmazonEC2FullAccess')
user2 = iam.create_user(UserName='user2',
				PermissionsBoundary='arn:aws:iam::aws:policy/AmazonEC2FullAccess')
ak1 = iam.create_access_key(UserName='user1')
ak2 = iam.create_access_key(UserName='user2')

## Prints an access key ID and secret access key for a user.
def cliKey(key):
	m=[]
	for k,v in key['AccessKey'].items():
		if k == 'AccessKeyId':
			m.append(k)
			m.append(v)
		if k == 'SecretAccessKey':
			m.append(k)
			m.append(v)
	print(m)

# Prints user1 and user2 AccessKeyId and SecretAccessKey in that order.
cliKey(ak1)
cliKey(ak2)








