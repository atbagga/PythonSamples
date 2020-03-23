#!/bin/bash
echo Script Name: "$0"
echo Total Number of Argument Passed: "$#"
curl -L https://aka.ms/InstallAzureCli | bash
az login --service-principal -u  $1 -p  $2 --tenant $3
az keyvault create -n $4 -g $5
