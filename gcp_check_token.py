import requests
import json

sBanner = """

 ######    ######  ########     ########  #######  ##    ## ######## ##    ## 
##    ##  ##    ## ##     ##       ##    ##     ## ##   ##  ##       ###   ## 
##        ##       ##     ##       ##    ##     ## ##  ##   ##       ####  ## 
##   #### ##       ########        ##    ##     ## #####    ######   ## ## ## 
##    ##  ##       ##              ##    ##     ## ##  ##   ##       ##  #### 
##    ##  ##    ## ##              ##    ##     ## ##   ##  ##       ##   ### 
 ######    ######  ##              ##     #######  ##    ## ######## ##    ## 

"""

# Ref: http://patorjk.com/software/taag/#p=testall&f=Graffiti&t=GCP%20Token

sUserAgent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"

print(sBanner)

sAccessToken = raw_input("Enter GCP Access Token: ")

sAccessToken = sAccessToken.strip()

print("[+] sToken: |" + sAccessToken + "|")

sEnter = raw_input("Press the [Enter] key to continue... ")

sUrl = 'https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=' + sAccessToken
dHeaders = {'user-agent': sUserAgent}

r = requests.get(sUrl, headers=dHeaders)

print("[+] Response Headers: " + str(r.headers) + "")
print("[+] Response Status Code: " + str(r.status_code) + "")
print("[+] Response Content: " + str(r.content) + "")

jContent = json.loads(r.content)
print("[+] Scope: " + str(jContent['scope']) + "")

sContent = str(jContent['scope'])
lContent = sContent.split(" ")
for sItem in lContent:
    print("[+] (in)Scope: " + str(sItem))