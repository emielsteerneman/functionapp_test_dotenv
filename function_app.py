import sys
import azure.functions as func
import dotenv
from dotenv import load_dotenv

print(sys.version)

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route('hello')
def main(req):
    return func.HttpResponse(f"Hello World! : python={sys.version}, dotenv={str(load_dotenv)}", mimetype="text/plain")