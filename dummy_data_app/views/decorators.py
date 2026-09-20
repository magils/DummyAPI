import functools
from types import SimpleNamespace

def view_query_params(serializer_class):
    def decorator(view_func):
        @functools.wraps(view_func)
        def wrapper(request, *args, **kwargs):
            serializer = serializer_class(data=request.query_params)
            serializer.is_valid(raise_exception=True)
            view_params = SimpleNamespace(**serializer.validated_data)
            return view_func(request, view_params, *args, **kwargs)
        return wrapper
    return decorator