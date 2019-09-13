import os
from flask import Flask, request, redirect, render_template

import requests
from urlparse import urlparse
import re

class VscodeExtensionUrl:

    DOWNLOAD_URL = "https://ms-vscode.gallery.vsassets.io/_apis/public/gallery/publisher/%(publisher)s/extension/%(name)s/%(version)s/assetbyname/Microsoft.VisualStudio.Services.VSIXPackage"

    @staticmethod
    def download(marketplace_url):
        url = urlparse(marketplace_url)
        if url.netloc!="marketplace.visualstudio.com" or not url.query:
            raise Exception("not a marketplace url")

        params = {}
        for kv in url.query.strip().split("&"):
            k, v = kv.split("=")
            params[k] = v

        itemName = params.get("itemName")
        if not itemName:
            raise Exception("not a marketplace url - missing extension name")

        publisher, extension = itemName.strip().split(".")

        version = re.findall(r'"version":"([^"]+)"',requests.get(marketplace_url).text)

        if not len(version):
            raise Exception("not a marketplace url - missing version")

        return VscodeExtensionUrl.DOWNLOAD_URL % {"publisher":publisher, "name":extension, "version": version.pop(0)}

# initialization
app = Flask(__name__)
app.config.update(
    DEBUG = True,
)

# controllers
@app.route("/")
def hello():
    url = request.args.get('url')
    if url:
        return redirect(VscodeExtensionUrl.download(url), code=302)

    return render_template('index.html')




# launch
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)