# ds_cloudwatch
### What is it:
This Lambda Function allows users to send Deep Security System events to AWS Cloudwatch Logs
### How to Use:
* Create a SNS Topic
* Create an IAM User with the following Policy Permissions (Note Please Change ARN for the Topic):
```{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": "sns:Publish",
            "Resource": "arn:aws:sns:REGION:ACCOUNTNUMBER:SNS-TOPIC"
        }
    ]
}
```
* At Deep Security -> Administration -> Event forwarding enter the SNS topic, the IAM Key and Secret. Test to ensure Credentials work
* Create a Policy for the AWS Lambda to be able to post to Cloudwatch Logs
```{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "CloudWatchLogs2017",
            "Effect": "Allow",
            "Action": "logs:PutLogEvents",
            "Resource": [
                "arn:aws:logs:REGION:ACCOUNTNUMBER:log-group:LOGGROUP:*:LOGSTREAM",
                "arn:aws:logs:REGION:ACCOUNTNUMBER:log-group:LOGGROUP"
            ]
        }
    ]
}
```


