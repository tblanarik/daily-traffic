import azure.functions as func

app = func.FunctionApp()

@app.function_name(name="ManualRun")
@app.route(route="hello") # HTTP Trigger
def test_function(req: func.HttpRequest) -> func.HttpResponse:
    return func.HttpResponse("ManualRun function processed a request!!!")