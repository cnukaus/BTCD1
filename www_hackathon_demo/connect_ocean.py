import requests
import json
import gzip
import shutil
import re
import sys
import os
import time
import logging as log




class OceanAPIWrapper:
    """Ocean API Wrapper Class

    This class facilitates requests to the Ocean API.

    Args:
        

    """

    def __init__(self, bmid, token, file_split_size):
        self.bmid = bmid
        self.urlBase = "https://localhost/api"
        self.apiVersion = "v1"
        self.url = ("%s/%s/services/download") % (
            self.urlBase,
            self.apiVersion,

        )


    def createDownload(
        self,documentId, ,dataToken, consumerAddress,signature,transferTxId, serviceType="access", serviceId=0,fileIndex=0
    ):
        """
        Create download session function with additional logic
        Args:
 
        """
        payload =   {
            "documentId":documentId,
            "serviceId": serviceId,
            "serviceType": serviceType,
            "fileIndex": fileIndex,
            "dataToken": dataToken,
            "consumerAddress":consumerAddress",
            "signature":signature,
            "transferTxId": transferTxId,
        }
        response = requests.post(self.url, data=payload)
        # If existing session is open, close it and try again
        json_response = json.loads(response.text)

        try:
            pass
        except KeyError:
            pass

        if error_code == 100:
            pass
        self.processResponse(response)
        session_id = json.loads(response.text)["session_id"]
        return session_id


    def uploadData(
        self,
        session,
        fileLocation,
        includeHeader="false",
        index="1",
        fileFormat="application/gzip",
    ):

        payload = {
            "dataToken": self.token,
          
        }
        files = {"file": ("file", open(fileLocation, "rb"), fileFormat)}
        log.info("Trying to upload %s" % fileLocation)
