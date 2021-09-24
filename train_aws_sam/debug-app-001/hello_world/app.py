import json

# import requests


def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    # try:
    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)

    #     raise e
    print(str(event))

    return {
        "statusCode": 200,
        "body": str(event),
    }

if __name__=="__main__":
    event = dict({'resource': '/hello', 'path': '/hello/', 'httpMethod': 'GET', 'headers': {'Accept': '*/*', 'CloudFront-Forwarded-Proto': 'https', 'CloudFront-Is-Desktop-Viewer': 'true', 'CloudFront-Is-Mobile-Viewer': 'false', 'CloudFront-Is-SmartTV-Viewer': 'false', 'CloudFront-Is-Tablet-Viewer': 'false', 'CloudFront-Viewer-Country': 'US', 'Host': 'jiy58cz051.execute-api.us-east-1.amazonaws.com', 'User-Agent': 'curl/7.58.0', 'Via': '2.0 6ff4697c5089876d94430beacc9a4d5e.cloudfront.net (CloudFront)', 'X-Amz-Cf-Id': 'N2AvPGKjnYO1pmEAEiw9WUFoDpVLAJZJLEir4IVYPiJ1CkCSOncd6Q==', 'X-Amzn-Trace-Id': 'Root=1-614cfd31-70f86876714f678132ccec87', 'X-Forwarded-For': '3.237.255.37, 130.176.133.131', 'X-Forwarded-Port': '443', 'X-Forwarded-Proto': 'https'}, 'multiValueHeaders': {'Accept': ['*/*'], 'CloudFront-Forwarded-Proto': ['https'], 'CloudFront-Is-Desktop-Viewer': ['true'], 'CloudFront-Is-Mobile-Viewer': ['false'], 'CloudFront-Is-SmartTV-Viewer': ['false'], 'CloudFront-Is-Tablet-Viewer': ['false'], 'CloudFront-Viewer-Country': ['US'], 'Host': ['jiy58cz051.execute-api.us-east-1.amazonaws.com'], 'User-Agent': ['curl/7.58.0'], 'Via': ['2.0 6ff4697c5089876d94430beacc9a4d5e.cloudfront.net (CloudFront)'], 'X-Amz-Cf-Id': ['N2AvPGKjnYO1pmEAEiw9WUFoDpVLAJZJLEir4IVYPiJ1CkCSOncd6Q=='], 'X-Amzn-Trace-Id': ['Root=1-614cfd31-70f86876714f678132ccec87'], 'X-Forwarded-For': ['3.237.255.37, 130.176.133.131'], 'X-Forwarded-Port': ['443'], 'X-Forwarded-Proto': ['https']}, 'queryStringParameters': {'AAAA': 'BBBB'}, 'multiValueQueryStringParameters': {'AAAA': ['BBBB']}, 'pathParameters': None, 'stageVariables': None, 'requestContext': {'resourceId': '8978if', 'resourcePath': '/hello', 'httpMethod': 'GET', 'extendedRequestId': 'GIx_yHemoAMFZPg=', 'requestTime': '23/Sep/2021:22:18:25 +0000', 'path': '/Prod/hello/', 'accountId': '580299357056', 'protocol': 'HTTP/1.1', 'stage': 'Prod', 'domainPrefix': 'jiy58cz051', 'requestTimeEpoch': 1632435505617, 'requestId': 'a8ad1156-d894-46c2-8c6d-c54a058ed420', 'identity': {'cognitoIdentityPoolId': None, 'accountId': None, 'cognitoIdentityId': None, 'caller': None, 'sourceIp': '3.237.255.37', 'principalOrgId': None, 'accessKey': None, 'cognitoAuthenticationType': None, 'cognitoAuthenticationProvider': None, 'userArn': None, 'userAgent': 'curl/7.58.0', 'user': None}, 'domainName': 'jiy58cz051.execute-api.us-east-1.amazonaws.com', 'apiId': 'jiy58cz051'}, 'body': None, 'isBase64Encoded': False})
    context = ''
    lambda_handler(event, context)