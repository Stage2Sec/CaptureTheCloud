import json
import socket
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
    sReturn = "NULL"
    
    try:
        sTargetIp = str(event['queryStringParameters']['TargetIp'])
        sTcpPort = str(event['queryStringParameters']['TcpPort'])
        
        print("[~] sTargetIp: " + sTargetIp)
        print("[~] sTcpPort: " + sTcpPort)
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2) #2 Second Timeout
        result = sock.connect_ex((sTargetIp,int(sTcpPort)))
        
        if result == 0:
            print("Port is open")
            sReturn = sTargetIp + ":" + sTcpPort + "/TCP is open"
        else:
            print("Port is not open")
            sReturn = sTargetIp + ":" + sTcpPort + "/TCP is closed"
        
        sock.close()
    except Exception as e:
        print("[!] Exception (e):" + str(e))
    
    return {
        "statusCode": 200,
        "body": sReturn,
    }
