class TinyUrlPresenter(object):
    def __init__(self, item, request):
        self.request = request
        self._item = item

    @property
    def short_url(self):
        protocol = 'https' if self.request.is_secure() else 'http'
        return '%s://%s/%s' % (protocol, self.request.get_host(), self._item.linked_with.slug)