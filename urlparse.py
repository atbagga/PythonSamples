try:
    from urllib.parse import urlparse, quote
except ImportError:
    from urlparse import urlparse
    from urllib import quote


def uri_parse(url):
    return urlparse(url)

def uri_quote(query_data):
    return quote(query_data)

def uri_parse_instance_from_git_uri(uri):
    parsed_uri = None
    if "/_git" in uri:
        parsed_uri = urlparse(uri)
        print(parsed_uri)
        # old Uri format
        if "visualstudio.com" in uri:
            return '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
        # new Uri format
        if "dev.azure.com" in uri:
            org_name = parsed_uri.path.strip("/").split("/")[0]
            return parsed_uri.scheme + "://" + parsed_uri.hostname + "/" + org_name
    # azure devops ssh urls do not have ssh:// at the start -
    elif "vs-ssh.visualstudio.com" in uri:
        # e.g. org@vs-ssh.visualstudio.com:v3/org/project/repo
        # Append ssh at start to set correct scheme
        parsed_uri = urlparse("ssh://{original_uri}".format(original_uri=uri))
        print(parsed_uri)
        return '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
    elif "ssh.dev.azure.com" in uri:
        # e.g. git@ssh.dev.azure.com:v3/org/project/repo
        # Append ssh at start to set correct scheme
        parsed_uri = urlparse("ssh://{original_uri}".format(original_uri=uri))
        print(parsed_uri)
        org_name = parsed_uri.path.strip("/").split("/")[0]
        return parsed_uri.scheme + "://" + parsed_uri.hostname + "/" + org_name


# print("----------------------------------")
# print(uri_parse_instance_from_git_uri("baggaatul24@vs-ssh.visualstudio.com:v3/baggaatul24/PythonSamples/PythonSamples"))
# print("----------------------------------")
# print(uri_parse_instance_from_git_uri("git@ssh.dev.azure.com:v3/baggaatul24/PythonSamples/PythonSamples"))
# print("----------------------------------")
# print(uri_parse_instance_from_git_uri("ssh://fabrikops2@vs-ssh.visualstudio.com:22/DefaultCollection/_ssh/fabrikamtools"))
# print("----------------------------------")
# print(uri_parse_instance_from_git_uri("https://mseng.visualstudio.com/AzureDevOps/_git/AzureDevOps"))
# print("----------------------------------")
# print(uri_parse_instance_from_git_uri("https://mseng.visualstudio.com/"))
# print("----------------------------------")
# print(uri_parse_instance_from_git_uri("https://mseng@dev.azure.com/mseng/azuredevops/_git/azuredevops"))
# print("----------------------------------")
# print(uri_parse_instance_from_git_uri("https://dev.azure.com/mseng/azuredevops/_git/azuredevops"))
# print("----------------------------------")
print(uri_parse_instance_from_git_uri("git@ssh.dev.azure.com:v3/MIProtocolBugBash/NewProject/ML-Repo"))
print("----------------------------------")
print(uri_parse_instance_from_git_uri("MIProtocolBugBash@vs-ssh.visualstudio.com:v3/MIProtocolBugBash/NewProject/ML-Repo"))
print("----------------------------------")
print(uri_parse_instance_from_git_uri("MIProtocolBugBash@vs-ssh.visualstudio.com:22/MIProtocolBugBash/NewProject/_ssh/ML-Repo"))
print("----------------------------------")
print(uri_parse_instance_from_git_uri("MIProtocolBugBash@vs-ssh.visualstudio.com:22/NewProject/_ssh/ML-Repo"))