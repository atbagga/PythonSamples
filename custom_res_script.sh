. ./az_install_script.sh
echo Azure CLI is installed successfully
az login --service-principal -u  $1 -p  $2 --tenant $3
echo Login Done.
az keyvault create -n $4 -g $5
echo KeyVault Created.
