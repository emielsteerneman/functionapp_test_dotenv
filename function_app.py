import azure.functions as func

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route('hello')
def main(req):
    return func.HttpResponse("Hello World!", mimetype="text/plain")