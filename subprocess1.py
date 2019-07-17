import subprocess
import json
aks_list = subprocess.check_output('az aks list -o json', shell=True)
aks_list = json.loads(aks_list)

for aks_clusters in aks_list:
    print(aks_clusters['name'])