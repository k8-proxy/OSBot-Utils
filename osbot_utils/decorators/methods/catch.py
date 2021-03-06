from functools import wraps


def catch(function):
    """Catches any errors and returns an object with the error
    return: { 'status': 'error', 'error': f'{exception}', 'exception': exception }"""
    @wraps(function)                                                    # so that when we call the __name__ of the called we get the correct name (for example self.aws_lambda.alias.__name__)
    def wrapper(*args,**kwargs):
        try:
            return function(*args,**kwargs)
        except Exception as exception:
            return {'status': 'error', 'error': f'{exception}', 'exception': exception}
    return wrapper