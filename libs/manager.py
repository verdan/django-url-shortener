import collections


class Manager(object):
    def __init__(self, base_class):
        self._base_class = base_class
        self._base_queryset = base_class.objects

    @staticmethod
    def has_count_method(query_obj):
        return hasattr(query_obj, 'count') and hasattr(query_obj.count, '__call__')

    def find(self, query, **kwargs):
        return query(self._base_queryset, **kwargs)

    def exists(self, query, **kwargs):
        return query(self._base_queryset, **kwargs).exists()

    def all(self, query=None, **kwargs):
        if query is None:
            return self._base_queryset.all()
        return query(self._base_queryset, **kwargs).all()

    def count(self, query_obj, **kwargs):
        if self.has_count_method(query_obj):
            return query_obj.count()
        else:
            return query_obj(self._base_queryset, **kwargs).count()

    def get_first(self, query_obj, **kwargs):
        if not self.has_count_method(query_obj):
            query_obj = self.find(query_obj, **kwargs)
        if not isinstance(query_obj, collections.Iterable):
            return query_obj
        query_obj = query_obj[:1]
        return query_obj[0] if len(query_obj) > 0 else None

    def flat_values_list(self, queryset, field):
        return queryset.values_list(field, flat=True)

    def bulk_create(self, items):
        return self._base_queryset.bulk_create(items)

    def create(self, **kwargs):
        record = self._base_class(**kwargs)
        record.save()
        return record

    def update(self, item, **kwargs):
        for k, v in kwargs.iteritems():
            setattr(item, k, v)
        item.save()
