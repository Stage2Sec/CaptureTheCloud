import requests
import time
import json

sApiKey = '...REDACTED...'
sUserAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
sDomainName = 'signin.aws.amazon.com'

sUrl = 'https://www.virustotal.com/vtapi/v2/domain/report?apikey=' + sApiKey + '&domain=' + sDomainName

try:
    headers = {
        "User-Agent": sUserAgent
    }
    r = requests.get(sUrl, allow_redirects=False, headers=headers) # verify=False, timeout=5

    sTimeStamp = str(time.strftime('%Y%m%d%H%M%S'))

    f = open('api_' + sTimeStamp + '.text', 'w')
    f.write(r.text)
    f.close()

    with open('api_' + sTimeStamp + '.json', 'w') as f:
        json.dump(r.json(), f)

    dResponse = r.json()
    lSubdomains = dResponse['subdomains']
    with open('api_' + sTimeStamp + '.list', 'w') as f:
        for item in lSubdomains:
            f.write("%s\n" % item)

except requests.RequestException as e:
    print(e)
