**Get details on a given key-pair-name**\
`aws ec2 describe-key-pairs --key-names key-pair-name`

**Launch a CloudFormation template (here in yml format) to create a stack called teststack**\
`aws cloudformation create-stack --stack-name teststack --template-body file://launch_ec2.yml`

**Get details on a given IAM user here called IAM_name**\
`aws iam get-user --user-name IAM_name`

**List the keypairs**\
`aws ec2 --profile default describe-key-pairs --query KeyPairs[].[KeyName]`
