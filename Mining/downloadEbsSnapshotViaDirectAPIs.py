#!/usr/bin/env python3
import boto3
import sys
import os
import time
from pathlib import Path
from random import SystemRandom
import argparse
import json
import shutil
import random
from tqdm import tqdm
import hashlib
import io
import base64

art = '''
Pentest with the Best! ( or Die Like the Rest! ) Use S2.Security for your next Engagement! :)



    ___ _               _        ___                    _                 _ 
   /   (_)_ __ ___  ___| |_     /   \_____      ___ __ | | ___   __ _  __| |
  / /\ / | '__/ _ \/ __| __|   / /\ / _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |
 / /_//| | | |  __/ (__| |_   / /_// (_) \ V  V /| | | | | (_) | (_| | (_| |
/___,' |_|_|  \___|\___|\__| /___,' \___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_|
                                                                            


Direct Download of Public EBS Snapshots

Author: Bryce Kunz ( @TweekFawkes )
Website: https://S2.Security/

python3 downloadEbsSnapshotViaDirectAPIs.py -i "AKIA_UNKNOWN" -k "kxjy_UNKNOWN" -s "snap-0ba327fe66dd62152" -r "us-west-1"

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
input("[+] Press [ENTER] to Continue...")

### ### ###

### START - Variables for User to Set - START ###
sFolderName = 'ec2_ebs_snapshots_public_json'
sRegion = 'us-west-1'  # us-west-1 is NoCal; Starting Region; Used to List Other Regions
### END - Variables for User to Set - END ###

### START - Args for User to Set - START ###
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--id", help="id", default="AKIA_UNKNOWN")
parser.add_argument("-k", "--key", help="key", default="kxjy_UNKNOWN")
parser.add_argument("-s", "--snapshotid", help="snapshotid", default="_UNKNOWN")
parser.add_argument("-r", "--region", help="region", default=sRegion)

args = parser.parse_args()

sAccessKeyId = args.id
sAccessKeyId = sAccessKeyId.strip()

sSecretAccessKey = args.key
sSecretAccessKey = sSecretAccessKey.strip()

sSnapshotIdDirty = args.snapshotid
sSnapshotId = sSnapshotIdDirty.strip()

sRegionDirty = args.region
sRegion = sRegionDirty.strip()
### END - Args for User to Set - END ###

### Variables Generated Based on User's Settings ###
cryptorand = SystemRandom()
### ### ###

### Create Access to AWS ###
print("[+] START - Create Access to AWS - START")
try:
    ec2_client = boto3.client('ec2', region_name=sRegion, aws_access_key_id=sAccessKeyId,
                              aws_secret_access_key=sSecretAccessKey)
    ec2_resource = boto3.resource('ec2', region_name=sRegion, aws_access_key_id=sAccessKeyId,
                                  aws_secret_access_key=sSecretAccessKey)
    ebs_client = boto3.client('ebs', region_name=sRegion, aws_access_key_id=sAccessKeyId,
                              aws_secret_access_key=sSecretAccessKey)
    # ebs_resource = boto3.resource('ebs', region_name=sRegion, aws_access_key_id=sAccessKeyId, aws_secret_access_key=sSecretAccessKey)
except Exception as e:
    print("[!] ERROR #062 e: " + str(e) + " |-| " + str(sys.exc_info()[0]))
### END ###


###
try:
    dResponseFromListSnapshotBlocks = ebs_client.list_snapshot_blocks(
        SnapshotId=sSnapshotId
    )

    iVolumeSize = dResponseFromListSnapshotBlocks['VolumeSize']
    print("[~] iVolumeSize: " + str(iVolumeSize) + " |-| " + str(type(iVolumeSize)))

    sVolumeSize = str(iVolumeSize)
    print("[~] sVolumeSize: " + str(sVolumeSize) + " |-| " + str(type(sVolumeSize)))

    iBlockSize = dResponseFromListSnapshotBlocks['BlockSize']
    print("[~] iBlockSize: " + str(iBlockSize) + " |-| " + str(type(iBlockSize)))

    sBlockSize = str(iBlockSize)
    print("[~] sBlockSize: " + str(sBlockSize) + " |-| " + str(type(sBlockSize)))

    print("[~] dResponseFromListSnapshotBlocks: " + str(dResponseFromListSnapshotBlocks))
    for dItemBlock in dResponseFromListSnapshotBlocks['Blocks']:
        print("[~] dItemBlock: " + str(dItemBlock) + " |-| " + str(type(dItemBlock)))

        iBlockIndex = dItemBlock['BlockIndex']
        print("[~] iBlockIndex: " + str(iBlockIndex) + " |-| " + str(type(iBlockIndex)))

        sBlockIndex = str(iBlockIndex)
        print("[~] sBlockIndex: " + str(sBlockIndex) + " |-| " + str(type(sBlockIndex)))

        sBlockToken = dItemBlock['BlockToken']
        print("[~] sBlockToken: " + str(sBlockToken) + " |-| " + str(type(sBlockToken)))

        dResponseFromGetSnapshotBlock = ebs_client.get_snapshot_block(
            SnapshotId=sSnapshotId,
            BlockIndex=iBlockIndex,
            BlockToken=sBlockToken
        )

        sDataLength = dResponseFromGetSnapshotBlock['DataLength']
        print("[~] sDataLength: " + str(sDataLength) + " |-| " + str(type(sDataLength)))

        sChecksumAlgorithm = dResponseFromGetSnapshotBlock['ChecksumAlgorithm']
        print("[~] sChecksumAlgorithm: " + str(sChecksumAlgorithm) + " |-| " + str(type(sChecksumAlgorithm)))

        with io.FileIO(sSnapshotId + '.tmp', 'ab') as f:
            for b in dResponseFromGetSnapshotBlock['BlockData']:
                # sha256_hash.update(b)
                f.write(b)
        f.close()
    shutil.move(sSnapshotId + '.tmp', sSnapshotId + '.done')
except Exception as e:
    print("[!] ERROR #141 e: " + str(e) + " |-| " + str(sys.exc_info()[0]))
