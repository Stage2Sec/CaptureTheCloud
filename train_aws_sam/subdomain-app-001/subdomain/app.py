import json
import socket

import sys
import traceback

# import requests

# --- # --- # --- # --- # --- # --- # --- # --- # --- # --- # --- # --- # --- # --- # --- # --- # --- # --- # --- #

__author__ = '@TweekFawkes'

# --- # --- # --- # --- # --- # --- # --- # --- # --- # --- # --- # --- # --- # --- # --- # --- # --- # --- # --- #

def sortUniqList(lMyList):
    lMyList = sorted(set(lMyList))
    return lMyList

# --- # --- # --- # --- # --- # --- # --- # --- # --- # --- # --- # --- # --- # --- # --- # --- # --- # --- # --- #

def checkIfStringIsAnIpAddress(ip_Str):
    try:
        socket.inet_aton(ip_Str)
        # legal
        return True
    except socket.error:
        # Not legal
        return False

# --- # --- # --- # --- # --- # --- # --- # --- # --- # --- # --- # --- # --- # --- # --- # --- # --- # --- # --- # --- #

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
    sReturn = "[+] START\n"
    
    try:
        sRootDomainName = event['queryStringParameters']['RootDomainName']
        #print(sRootDomainName)
        #
        filepath = 'namelist.txt'
        with open(filepath) as f:
            for line in f:
                lIpAddresses = []
                line = line.strip()
                #print(line)
                #sReturn = sReturn + str(line) + "\n"
                sFqdn = line + '.' + sRootDomainName
                #print(sFqdn)
                try:
                    addrs_List = [str(i[4][0]) for i in socket.getaddrinfo(sFqdn, 65535)]
                    for item in addrs_List:
                        if checkIfStringIsAnIpAddress(item):
                            lIpAddresses.append(item)
                    #sReturn = sReturn + str(socket.getaddrinfo('0.lizardblue.com', 80))
                    lIpAddresses = sortUniqList(lIpAddresses)
                    sDiscovered = sFqdn + " -> " + str(", ".join(lIpAddresses))
                    sReturnNow = "[+] Subdomain discovered: " + sDiscovered + "\n"
                    sReturn = sReturn + sReturnNow
                except:
                    #sReturnNow = "[!] Exception: socket.getaddrinfo() failed to lookup\n"
                    sReturnNow = "[!] Exception: socket.getaddrinfo() failed to lookup: " + sFqdn + "\n"
                    #print(sReturnNow)
                    #sReturn = sReturn + sReturnNow
                #print(sReturn)
        #
    except Exception as e:
        sReturn = sReturn + "[!] Exception\n"
        sReturn = sReturn + "[!] sys.exc_info()[0]: " + str(sys.exc_info()[0]) + "\n"
        sReturn = sReturn + "[!] traceback.format_exc(): " + str(traceback.format_exc()) + "\n"
        sReturn = sReturn + "[!] e: " + str(e) + "\n"
        print(sReturn)
        
    sReturn = sReturn + "[+] END\n"
    print(sReturn)

    # try:
    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)
    #     raise e
    
    return {
        "statusCode": 200,
        "body": sReturn
    }
    
    '''
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "bye world: " + str(sReturn),
            # "location": ip.text.replace("\n", "")
        }),
    }
    '''


if __name__=="__main__":
    event = dict({'queryStringParameters':{'RootDomainName':'lizardblue.com'}})
    context = ''
    lambda_handler(event, context)