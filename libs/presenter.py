class BasePresenter(object):
    def __init__(self, item):
        self._item = item

    def __getattr__(self, item):
        if hasattr(self._item, item):
            return getattr(self._item, item)

        error_message = "Property or Method '%s' is not defined in either %s presenter or %s class" % \
                        (item, self.__class__, self._item.__class__)
        raise AttributeError(error_message)

    def __eq__(self, other):
        # noinspection PyProtectedMember
        return hasattr(other, '_item') and self._item == other._item

    @property
    def decorated(self):
        return self._item