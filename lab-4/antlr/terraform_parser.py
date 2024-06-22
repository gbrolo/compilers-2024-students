import sys
import requests
from antlr4 import *
from TerraformSubsetLexer import TerraformSubsetLexer
from TerraformSubsetParser import TerraformSubsetParser
from TerraformSubsetListener import TerraformSubsetListener

# This is just an example, don't take this as a magical code.
# You can use this file as a baseline for your implementation. This uses listeners, you can use a visitor pattern instead.

# In this example, the token is hardcoded. You MUST change this behavior to grab the token as well from the Terraform file.
API_TOKEN = "your_digitalocean_api_token"

class TerraformListener(TerraformSubsetListener):
    def __init__(self):
        self.provider = {}
        self.resources = []

    def enterProvider(self, ctx:TerraformSubsetParser.ProviderContext):
        provider_name = ctx.IDENTIFIER().getText()
        self.provider[provider_name] = {}
        for kv in ctx.providerBody().keyValuePair():
            key = kv.IDENTIFIER().getText()
            value = kv.STRING().getText().strip('"')
            self.provider[provider_name][key] = value

    def enterResource(self, ctx:TerraformSubsetParser.ResourceContext):
        resource_type = ctx.IDENTIFIER(0).getText()
        resource_name = ctx.IDENTIFIER(1).getText()
        resource = {"type": resource_type, "name": resource_name, "attributes": {}}
        for kv in ctx.resourceBody().keyValuePair():
            key = kv.IDENTIFIER().getText()
            value = kv.STRING().getText().strip('"')
            resource["attributes"][key] = value
        self.resources.append(resource)

    def getProvider(self):
        return self.provider

    def getResources(self):
        return self.resources

def create_droplet(api_token, resource):
    url = "https://api.digitalocean.com/v2/droplets"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_token}"
    }
    data = {
        "name": resource["attributes"]["name"],
        "region": resource["attributes"]["region"],
        "size": resource["attributes"]["size"],
        "image": resource["attributes"]["image"]
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 202:
        droplet = response.json()["droplet"]
        print(f"Droplet created with ID: {droplet['id']}")
        return droplet['id']
    else:
        print(f"Failed to create droplet: {response.text}")
        return None

def delete_droplet(api_token, droplet_id):
    url = f"https://api.digitalocean.com/v2/droplets/{droplet_id}"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.delete(url, headers=headers)
    if response.status_code == 204:
        print(f"Droplet with ID {droplet_id} has been destroyed")
    else:
        print(f"Failed to destroy droplet: {response.text}")

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = TerraformSubsetLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = TerraformSubsetParser(stream)
    tree = parser.terraform()

    listener = TerraformListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    provider = listener.getProvider()
    resources = listener.getResources()

    if provider and resources:
        for resource in resources:
            if resource["type"] == "droplet":
                droplet_id = create_droplet(API_TOKEN, resource)
                if droplet_id:
                    # You MUST destroy all of your droplets.
                    delete_droplet(API_TOKEN, droplet_id)
                    pass

if __name__ == '__main__':
    main(sys.argv)
