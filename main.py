from app import LoiqdevFrameApp

app = LoiqdevFrameApp()

@app.route("/home")
def home(request,response):
    response.text = "Hello from home page"

@app.route("/about")
def about(request,response):
    response.text = "Hello from about page"