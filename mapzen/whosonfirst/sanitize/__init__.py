import codecs

# please put me in a library somewhere...
# please to be porting this at the same time...
# https://github.com/exflickr/flamework/blob/master/www/include/lib_sanitize.php
# (20150831/thisisaaronland)

# I have put this in its own library! And next I will port lib_sanitize.php.
# (20160204/dphiffer)

'''

We are going to make an abstract pony factory for this some day.
(20160205/dphiffer)

def get_param(k, sanitize=None):

    param = flask.request.args.getlist(k)
    
    if len(param) == 0:
        return None
        
    if sanitize:
        param = map(sanitize, param)

    return param

def get_single(v):

    if v and type(v) == types.ListType:
        v = v[0]

    return v

def get_str(k):

    param = get_param(k, sanitize_str)
    return param

def get_int(k):

    param = get_param(k, sanitize_int)
    return param

def get_float(k):

    param = get_param(k, sanitize_float)
    return param
	
'''

def sanitize_str(str):

    if str:
        str = codecs.encode(str, 'utf-8')
        str = str.strip()

    return str
    
def sanitize_int(i):

    if i:
        i = int(i)

    return i

def sanitize_float(f):

    if f:
        f = float(f)

    return f
