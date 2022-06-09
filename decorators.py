from datetime import datetime

def logger(fn):
    def inner(*args, **kwargs):
        print('entrando')
        result = fn(*args, **kwargs)
        print('saliendo')
        return result
    return inner

def timing(fn):
    def inner(*args, **kwargs):
        start = datetime.now()
        result = fn(*args,**kwargs)
        finish = datetime.now()
        print(f'the func took: {(finish - start).seconds} to complete')
        return result
    return inner

@timing
def hace_algo(arg) -> None:
    import time
    time.sleep(2)
    print(f'haciendo {arg}')

hace_algo('clases')