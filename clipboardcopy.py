import pyperclip

print("Please create a GitHub secret in your repository with variable name: DOCKER_USERNAME")
print("The value is copied to your clipboard and just be pasted directly in the secret value section.")
pyperclip.copy("MyDockerUsernameValue")
