class LocallContext:
    functions = {}

    @classmethod
    def register_function(cls, name, func):
        cls.functions[name] = func

    @classmethod
    def get_function(cls, name):
        return cls.functions.get(name)

    @classmethod
    def call_function(cls, name, *args, **kwargs):
        func = cls.get_function(name)
        if func:
            return func(*args, **kwargs)
        else:
            raise ValueError(f"Function '{name}' is not registered.")