from locall_context import LocallContext

def locall_function(obj):
    if isinstance(obj, type):
        for attr_name in dir(obj):
            attr_value = getattr(obj, attr_name)
            if callable(attr_value) and not attr_name.startswith('__'):
                LocallContext.register_function(attr_name, attr_value)
        return obj

    elif callable(obj):
        LocallContext.register_function(obj.__name__, obj)
        return obj