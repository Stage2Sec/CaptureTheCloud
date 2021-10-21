#!/usr/bin/env python3
import boto3
import sys
import os
import time
from pathlib import Path
import shutil
from random import SystemRandom
import argparse

art = '''
Pentest with the Best! ( or Die Like the Rest! ) Use S2.Security for your next Engagement! :)


 _,  _  _, ___   __, _,_ __, _,  _  _,   __, __,  _,    _, _, _  _, __,  _, _,_  _, ___  _,
 |   | (_   |    |_) | | |_) |   | / `   |_  |_) (_    (_  |\ | /_\ |_) (_  |_| / \  |  (_ 
 | , | , )  |    |   | | |_) | , | \ ,   |   |_) , )   , ) | \| | | |   , ) | | \ /  |  , )
 ~~~ ~  ~   ~    ~   `~' ~   ~~~ ~  ~    ~~~ ~    ~     ~  ~  ~ ~ ~ ~    ~  ~ ~  ~   ~   ~ 


List Public EBS Snapshots

Author: Bryce Kunz ( @TweekFawkes )
Website: https://S2.Security/

python3 createListsOfPublicEbsSnapshots.py -i AKIA_UNKNOWN -k kxjy_UNKNOWN -f output_from_listpublicsnapshots -r us-east-1

Pentest with the Best! ( or Die Like the Rest! ) Use S2.Security for your next Engagement! :)
'''

def logPrint(sFileName, sText):
    print("[+] START - logPrint() - START")
    try:
        my_file = Path(sFileName)
        if my_file.is_file():
            print(str(
                sText))  # file exists; ref: https://stackoverflow.com/questions/82831/how-do-i-check-whether-a-file-exists-without-exceptions
            with open(sFileName, mode='at', encoding='utf-8') as myfile:
                myfile.write(sText)
                myfile.write('\n')
        else:
            print(str(sText))
            with open(sFileName, mode='wt', encoding='utf-8') as myfile:
                myfile.write(sText)
                myfile.write('\n')
    except Exception as e:
        print("[!] ERROR #038 e: " + str(e) + " |-| " + str(sys.exc_info()[0]))
    print("[+] END - logPrint() - END")


def getTimestamp():
    oTimestamp = time.strftime('%Y%m%d%H%M%S')
    sTimestamp = str(oTimestamp)
    return sTimestamp


def getFileContentsAsList(sFileName):
    print("[+] START - getFileContentsAsList() - START")
    try:
        text_file = open(sFileName, "r")
        lines = text_file.readlines()
        text_file.close()
        lines = [x for x in lines if not x.startswith('#')]  # get rid of lines starting with #
        lines = [s.rstrip() for s in lines]  # get rid of /n chars at the end of the lines
        lines = list(filter(None, lines))  # get rid of blank lines
        return lines
    except Exception as e:
        print("[!] ERROR #026 e: " + str(e) + " |-| " + str(sys.exc_info()[0]))
    print("[+] END - getFileContentsAsList() - END")


### ### ###

print(art)

### START - Variables for User to Set - START ###
sFolderName = 'ec2_ebs_snapshots_public'
sRegion = 'us-west-1'  # NoCal; Default Starting Region; Used to enumerate a list of all regions in AWS.
### END - Variables for User to Set - END ###

### START - Args for User to Set - START ###
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--id", help="id", default="AKIA_UNKNOWN")
parser.add_argument("-k", "--key", help="key", default="kxjy_UNKNOWN")
parser.add_argument("-f", "--folder", help="dir", default=sFolderName)
parser.add_argument("-r", "--region", help="region", default=sRegion)

args = parser.parse_args()

sAccessKeyId = args.id
sAccessKeyId = sAccessKeyId.strip()

sSecretAccessKey = args.key
sSecretAccessKey = sSecretAccessKey.strip()

sFolderDirty = args.folder
sFolderName = sFolderDirty.strip()

sRegionDirty = args.region
sRegion = sRegionDirty.strip()
### END - Args for User to Set - END ###

### START - Variables Generated Based on User's Settings - START ###
cryptorand = SystemRandom()

sRootFullPath = os.path.dirname(os.path.realpath(__file__))  # To get the full path to the directory a Python file is contained in, write this in that file
sFolderFullPath = os.path.join(sRootFullPath, sFolderName)

if not os.path.exists(sFolderFullPath):
    os.makedirs(sFolderFullPath)
### END - Variables Generated Based on User's Settings - END ###

### Create Access to AWS to get a list of regions ###
try:
    ec2_client = boto3.client('ec2', region_name=sRegion, aws_access_key_id=sAccessKeyId,
                              aws_secret_access_key=sSecretAccessKey)
    ec2_resource = boto3.resource('ec2', region_name=sRegion, aws_access_key_id=sAccessKeyId,
                                  aws_secret_access_key=sSecretAccessKey)
    ebs_client = boto3.client('ebs', region_name=sRegion, aws_access_key_id=sAccessKeyId,
                              aws_secret_access_key=sSecretAccessKey)
except Exception as e:
    print("[!] ERROR #062 e: " + str(e) + " |-| " + str(sys.exc_info()[0]))

regions = ec2_client.describe_regions()
regions = [r['RegionName'] for r in regions['Regions']]
for sRegion in regions:
    print("[~] sRegion: " + str(sRegion) + " |-| " + str(type(sRegion)))

    ### Create Access to AWS specific region ###
    try:
        ec2_client = boto3.client('ec2', region_name=sRegion, aws_access_key_id=sAccessKeyId,
                                  aws_secret_access_key=sSecretAccessKey)
        ec2_resource = boto3.resource('ec2', region_name=sRegion, aws_access_key_id=sAccessKeyId,
                                      aws_secret_access_key=sSecretAccessKey)
        ebs_client = boto3.client('ebs', region_name=sRegion, aws_access_key_id=sAccessKeyId,
                                  aws_secret_access_key=sSecretAccessKey)
    except Exception as e:
        print("[!] ERROR #138 e: " + str(e) + " |-| " + str(sys.exc_info()[0]))
    ###

    ### List EC2 EBS Snapshots ###
    print("[+] START - List EC2 EBS Snapshots - START")
    try:
        dictResponse = ec2_client.describe_snapshots()
    except Exception as e:
        print("[!] ERROR #151 e: " + str(e) + " |-| " + str(sys.exc_info()[0]))

    sFileNameForListOfSnapshotsWithOwnerIds = 'UNKNOWNUNKNOWNUNKNOWN'

    try:
        sTimeStamp = getTimestamp()
        #print("[~] sTimeStamp: " + str(sTimeStamp))
    except Exception as e:
        print("[!] ERROR #160 e: " + str(e) + " |-| " + str(sys.exc_info()[0]))

    sFileNameForListOfSnapshotsWithOwnerIds = sRegion + "_-_" + sTimeStamp + ".list"
    sFFPForListOfSnapshotsWithOwnerIds = os.path.join(sFolderFullPath, sFileNameForListOfSnapshotsWithOwnerIds)

    listSnap = dictResponse["Snapshots"]
    print("[+] END - List EC2 EBS Snapshots - END")
    ###

    ### List EC2 EBS Snapshots ###
    for dictItem in listSnap:
        try:
            sOwnerId = str(dictItem["OwnerId"])
            sSnapshotId = str(dictItem["SnapshotId"])
            sEncrypted = str(dictItem["Encrypted"])
            sVolumeSize = str(dictItem["VolumeSize"])
            with open(sFFPForListOfSnapshotsWithOwnerIds, 'a') as the_file:
                the_file.write(
                    sOwnerId + ',' + sSnapshotId + ',' + sEncrypted + ',' + sVolumeSize + ',' + sRegion + ',' + sTimeStamp + '\n')
        except Exception as e:
            print("[!] ERROR #194 e: " + str(e) + " |-| " + str(sys.exc_info()[0]))

    try:
        sFileNameForListOfSnapshotsWithOwnerIdsLatest = sRegion + "_-_latest.list"
        sFFPForListOfSnapshotsWithOwnerIdsLatest = os.path.join(sFolderFullPath, sFileNameForListOfSnapshotsWithOwnerIdsLatest)
        if os.path.isfile(sFFPForListOfSnapshotsWithOwnerIdsLatest):
            os.remove(sFFPForListOfSnapshotsWithOwnerIdsLatest)
        shutil.copyfile(sFFPForListOfSnapshotsWithOwnerIds, sFFPForListOfSnapshotsWithOwnerIdsLatest)
    except Exception as e:
        print("[!] ERROR #128 e: " + str(e) + " |-| " + str(sys.exc_info()[0]))

    ###
