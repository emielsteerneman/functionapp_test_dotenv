import azure.functions as func
import dotenv
from dotenv import load_dotenv

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route('hello')
def main(req):
    return func.HttpResponse("Hello World! : " + str(load_dotenv), mimetype="text/plain")