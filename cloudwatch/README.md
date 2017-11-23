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
             "Sid": "SNS2017",
            "Effect": "Allow",
            "Action": "sns:Publish",
            "Resource": "arn:aws:sns:REGION:ACCOUNTNUMBER:SNS-TOPIC"
        }
    ]
}
```
* At Deep Security -> Administration -> Event forwarding enter the SNS topic, the IAM Key and Secret. Test to ensure Credentials work
* At Cloudwatch Logs Create a Log Group and a Log Stream
* Create a new AWS Lambda Function from Scratch
** Under Policy, Create a custom Policy use the lambda_basic_execution Role
** Paste the code
** Change to Python 2.7
** Under Environment Variables, Enter the following
*** logGroupName - 
*** logStreamNamePrefix -
* Go back to Deep Security and Test the SNS again, you should see the Log event in Cloudwatch Logs