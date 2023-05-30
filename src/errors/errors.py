from werkzeug.exceptions import HTTPException


class BaseHTTPException(HTTPException):

    code = 404
    description = ''

    
    def get_body(self, environ: None = None, scope: dict | None = None) -> str:
        resp = self.name if self.description == '' else self.description
        return '{'+f'{self.code}: {resp}'+'}'
    
    def get_headers(self, environ: None = None, scope: dict | None = None) -> list[tuple[str, str]]:
        return[("Content-type", "text/json; charset=utf-8   ")] 
    

class Error404(BaseHTTPException):
    code = 404

class Error500(BaseHTTPException):
    code = 500
