def strip_comments(code):
    out = ''
    it = iter(code)
    try:
        while True:
            c = next(it)
            if c == '/':
                n = next(it)
                if n == '*':
                    while True:
                        c = next(it)
                        # XXX: this is buggy, doesn't handle a closing **/
                        if c == '*':
                            c = next(it)
                            if c == '/':
                                break
                else:
                    out += '/' + n
            else:
                out += c
    except StopIteration:
        return out


code = """
function add(a, b){
    /**
    * Function that adds two items
    */
    return a + b;
}
add(a, b); /* call add function */
"""

print(strip_comments(code))
