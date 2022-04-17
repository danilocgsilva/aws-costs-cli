# AWS cost utility 

Get human readable costs data from AWS account.

By default, bring each day cost since a month ago. You can custom the period of fetching the data.

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



if you want to set a starting period, do:
```
awscosts --profile <your_aws_profile_name> --start-time 2022-02-16
```

Maybe you want to plot the day-by-day costs in a graph. You can change the data output to csv format, so you can use in your own application as data input or to plot a graph i Libreoffice.

```
awscosts --profile <your_aws_profile_name> --format csv
```

![Graph generated by CSV](docs/graph-from-csv.png)

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

You can set an starting period since from you want to get the costs.
