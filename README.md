# AWS cost utility 

Get human readable costs data from AWS account.

## Installing

Go to the project's root directory and then types:

```
pip install -r requirements.txt
pip install .
```

## Using

In the command line, type:
```
awscosts --profile <your_aws_profile_name>
```

If you want to get costs from a specific service, do:
```
awscosts --profile <your_aws_profile_name> --type <service>
```

Allowed services are:

* ec2
* s3
* workmail
* tax
* cloudwatch
* sns
* route53
* rds
* codecommit
* dynamodb

You can get prices from several services at once separated by comma:

```
awscosts --profile <your_aws_profile_name> --type workmail,sns
```
