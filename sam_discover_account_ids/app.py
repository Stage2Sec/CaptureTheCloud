import secrets
import json
import requests
import time
import boto3

def lambda_handler(event, context):
    sReturn = ""

    iCount = 0
    iLimit = 33

    iFourOhFourCount = 0
    lFourOhFour = []

    iThreeOhTwoCount = 0
    lThreeOhTwo = []

    iOtherCount = 0
    lOther = []

    while iCount < iLimit:
        sRandomNumber = str(secrets.randbelow(1000000000000)).zfill(12)
        sUrl = 'https://' + sRandomNumber + '.signin.aws.amazon.com'
        iCount = iCount + 1

        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
            }

            requestsResponse = requests.get(sUrl, allow_redirects=False, headers=headers, verify=False, timeout=5)
            sResponseStatusCode = str(requestsResponse.status_code)
            sLine = sResponseStatusCode + "-" + sUrl

            if sResponseStatusCode == "404":
                iFourOhFourCount = iFourOhFourCount + 1
                lFourOhFour.append(sLine)
                print("[*] sLine: " + sLine)
                print("[*] iFourOhFourCount: " + str(iFourOhFourCount) + "\n")
                print("[*] lFourOhFour: " + str(iFourOhFourCount) + "\n")
            elif sResponseStatusCode == "302":
                iThreeOhTwoCount = iThreeOhTwoCount + 1
                lThreeOhTwo.append(sLine)
                print("[*] sLine: " + sLine)
                print("[*] iThreeOhTwoCount: " + str(iThreeOhTwoCount) + "\n")
                print("[*] lThreeOhTwo: " + str(lThreeOhTwo) + "\n")
            else:
                iOtherCount = iOtherCount + 1
                lOther.append(sLine)

            time.sleep(int(secrets.randbelow(3)))
        except requests.RequestException as e:
            print(e)
        if iCount == iLimit:
            sBucket = 'YourGloballyUniqueS3BucketName'  # already created on S3
            sTimeStamp = str(time.strftime('%Y%m%d%H%M%S'))

            if lThreeOhTwo:
                sFileNameThreeOhTwo = "302_" + sTimeStamp + ".txt"
                sFileContentsThreeOhTwo = str(lThreeOhTwo)
                client = boto3.client('s3')
                client.put_object(Body=sFileContentsThreeOhTwo, Bucket=sBucket, Key=sFileNameThreeOhTwo)

            if lFourOhFour:
                sFileNameFourOhFour = "404_" + sTimeStamp + ".txt"
                sFileContentsFourOhFour = str(lFourOhFour)
                client = boto3.client('s3')
                client.put_object(Body=sFileContentsFourOhFour, Bucket=sBucket, Key=sFileNameFourOhFour)

            if lOther:
                sFileNameOther = "000_" + sTimeStamp + ".txt"
                sFileContentsOther = str(lOther)
                client = boto3.client('s3')
                client.put_object(Body=sFileContentsOther, Bucket=sBucket, Key=sFileNameOther)

            iCount = 0

    print("[*] sReturn: " + sReturn)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": sReturn
        }),
    }