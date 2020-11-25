def list_contain(a, b, eq_len = True):
    '''
    Check if list a contained in list b.

    If eq_len = True -> Check if a, b are identical
    '''
    if eq_len and len(a) != len(b):
        return False

    return all([x in b for x in a])


def extract_keys(d, keys):
    '''
    Return a dictionary contain only designated keys.

    Param:
    -   d (dict)
    -   keys (list of key)
    '''
    return {k:d[k] for k in keys}


def algebra_split(string, split_char = ","):
    '''
    Split a string by designated character without violate parenthesis rule. 
    '''
    res = []
    brk = 0
    p_count = 0
    string = string + split_char
    for i in range(len(string)):
        if string[i] == "(":
            p_count += 1
        elif string[i] == ")":
            p_count -= 1
        elif string[i] == split_char:
            if p_count == 0:
                res.append(string[brk:i])
                brk = i+1
    return res