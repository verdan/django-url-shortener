from libs.presenter import BasePresenter


class TinyUrlPresenter(BasePresenter):
    def __init__(self, item, request):
        self.request = request
        super(TinyUrlPresenter, self).__init__(item=item)

    @property
    def shortified(self):
        protocol = 'https' if self.request.is_secure() else 'http'
        return '%s://%s/%s' % (protocol, self.request.get_host(), self._item.linked_with.slug)