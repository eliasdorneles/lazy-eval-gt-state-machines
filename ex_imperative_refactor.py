def strip_comments(code):
    def skip_until_end_comment(it):
        while True:
            c = next(it)
            if c == '*':
                c = next(it)
                if c == '/':
                    break

    out = ''
    it = iter(code)
    try:
        while True:
            c = next(it)
            if c == '/':
                n = next(it)
                if n == '*':
                    skip_until_end_comment(it)
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
