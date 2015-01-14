from django.template.response import TemplateResponse


class BaseView(object):
    template_name = None

    def __init__(self, request):
        self.request = request
        self.http_method_names = ['get', 'post']

    def get_context_data(self, **kwargs):
        return kwargs

    def get(self, *args, **kwargs):
        raise NotImplementedError

    def post(self, *args, **kwargs):
        raise NotImplementedError

    def put(self, *args, **kwargs):
        raise NotImplementedError

    def dispatch(self, *args, **kwargs):
        handler = getattr(self, self.request.method.lower(), self.get)
        response = handler(*args, **kwargs)
        is_dict = type(response) is dict
        if is_dict:
            return TemplateResponse(self.request, self.template_name, response)

        return response

    def respond_with(self, *args, **kwargs):
        return self.dispatch(*args, **kwargs)