from app import LoiqdevFrameApp

app = LoiqdevFrameApp()

@app.route("/home")
def home(request,response):
    response.text = "Hello from home page"

@app.route("/about")
def about(request,response):
    response.text = "Hello from about page"

@app.route("/hello/{name}")
def greeting(request, response, name):
    response.text = f"Assalomu aleykum {name}"

@app.route("/books")
class Books:
    def get(self,request,response):
        response.text = "Hello from books page"

    def post(self,request,response):
        response.text = "Endpoint to create a book"

@app.route("/template")
def template_handler(req, resp):
    resp.body = app.template(
        "home.html",
        context={"new_title": "Best title", "new_body": "Best body"}
    )