def with_attrs(queryset, **attrs):
    return queryset.filter(**attrs)