import json
import os
import boto3
import time
#Main Router for Cloudwatch Logs
def lambda_handler(event, context):

    cloudwatch_logs = boto3.client('logs')
    message = json.loads(event['Records'][0]['Sns']['Message'])
    for x in message:

        cloudwatch_message = json.dumps(x)

        log_stream = cloudwatch_logs.describe_log_streams(
        logGroupName=os.environ['logGroupName'],logStreamNamePrefix=os.environ['logStreamNamePrefix']
        )

        try:
            log_stream['logStreams'][0]['uploadSequenceToken']
        except KeyError:
           # print ("Index doesn't exist!")
            response = cloudwatch_logs.put_log_events(
            logGroupName=os.environ['logGroupName'],logStreamName=os.environ['logStreamNamePrefix'],
            logEvents=[
                {
                    'timestamp': int(round(time.time() * 1000)),
                    'message': cloudwatch_message
                },
            ]
            )
        else:
          #  print ("Index Exists")
            response = cloudwatch_logs.put_log_events(
            logGroupName=os.environ['logGroupName'],logStreamName=os.environ['logStreamNamePrefix'],
            logEvents=[
                {
                    'timestamp': int(round(time.time() * 1000)),
                    'message': cloudwatch_message
                },
            ],
            sequenceToken=log_stream['logStreams'][0]['uploadSequenceToken']
            )

       # print(response)
    return(response)