#!/bin/bash
echo Script Name: "$0"
echo Total Number of Argument Passed: "$#"
sudo apt-get update
sudo apt-get install ca-certificates curl apt-transport-https lsb-release gnupg
echo Step 1 Completed.
curl -sL https://packages.microsoft.com/keys/microsoft.asc | 
    gpg --dearmor | 
    sudo tee /etc/apt/trusted.gpg.d/microsoft.asc.gpg > /dev/null
AZ_REPO=$(lsb_release -cs)
echo Step 2 Completed.
echo "deb [arch=amd64] https://packages.microsoft.com/repos/azure-cli/ $AZ_REPO main" | 
    sudo tee /etc/apt/sources.list.d/azure-cli.list
echo Step 3 Completed.
sudo apt-get update
echo Step 4 Completed.
sudo apt-get install azure-cli
echo "Installation Complete."
az --version
az login --service-principal -u  $1 -p  $2 --tenant $3
echo Login Done.
az keyvault create -n $4 -g $5
echo KeyVault Created.
