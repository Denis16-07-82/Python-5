def val_checker(x=1):
    def _val_checker(func):
        def wrapper(*args):
            if type(args) == int and args > 0:
                resalt = func(*args)
                return resalt
            else:
                raise ValueError

        return wrapper

    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3
