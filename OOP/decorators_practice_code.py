from functools import wraps

def my_logger(orig_func):
    import logging
    logging.basicConfig(filename=f'{orig_func.__name__}.log', level=logging.INFO)
    #**args, **kwargs - allow you to pass an unspecified number of arguments
    @wraps(orig_func)
    def wrapper(*args,**kwargs):
        logging.info(
            f'Ran with args: {args}, and kwargs: {kwargs}')
        print('YESSS')
        return orig_func(*args,**kwargs)

    return wrapper

def prefix_decorator(prefix):
    def decorator_function(original_function):
        def wrapper_function(*args, **kwargs):
            print(prefix,'Executed Before', original_function.__name__)
            result = original_function(*args,**kwargs)
            print(prefix,'Executed After', original_function.__name__)
            return result
        return wrapper_function
    return decorator_function




@prefix_decorator('TESTING:')
def display_info(name, age):
    print(f'display_info ran with arguments ({name},{age})')


display_info('Hank',30)
