from errors import errors

def error_404(e):
    return errors.Error404()

def error_500(e):
    return errors.Error500()


def register_all_errors_from_app(app):
    app.register_error_handler(404, error_404)
    app.register_error_handler(500, error_500)