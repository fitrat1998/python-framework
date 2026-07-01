from webob import Request
from webob import Response

class LoiqdevFrameApp:
    def __call__(self,environ,start_response):
       request = Request(environ)
       response = self.handle_request(request)
       return response(environ,start_response)

    def handle_request(selfself,request):
        user_agent = request.environ.get("HTTP_USER_AGENT", "User Agent not Found")

        response = Response()
        response.text = f"Hello my friend with user agent {user_agent}"

        return response


