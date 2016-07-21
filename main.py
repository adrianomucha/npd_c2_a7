def filter_custom(l,f):
    '''Filter a list using a function
    Return a new list that contains all the elements e of l
        for which f(e) is True

    :param l: a list
    :param f: a function that takes one argument and returns either
        True or False
    '''
    new_list[]

    return new_list
def map_custom(l,f):
    '''Map a list using a function

    Return a new list that applies f(e) for every element e in l

    :param l: a list
    :param m: a function that takes one argument and returns a value
    '''
    new_list = []
    for e in l:
        new_list.append(f(e))
    return new_list

def reduce_custom(l,f, starting_value):
    ''' Rdeuce a list using a reducer function and a starting value

    Return a single value that applies f(v, e) for every
        e in l from left to right. The initial value for v
        should be starting_value, and subsequent values should
        be the previously calculated value from f(v, e)

    :param l: a list
    :param f: a function that takes one argument and returns a value
    :param starting_value: the beggining value for the reducer function
        computation
    '''
    pass

if __name__ == '__main__':
    l = [7,8,9]
    f = lambda x: x * 10
    print(map_custom(l,f))

