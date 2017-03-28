def coroutine(func):
    def start(*args, **kwargs):
        cr = func(*args, **kwargs)
        cr.next()
        return cr
    return start


@coroutine
def strip_comments(target):
    while True:
        c = yield
        if c == '/':
            n = yield
            if n == '*':
                while True:
                    c = yield
                    break_outer = False
                    while c == '*':
                        c = yield
                        if c == '/':
                            break_outer = True
                            break
                    if break_outer:
                        break
            else:
                target.send('/')
                target.send(n)
        else:
            target.send(c)


@coroutine
def sink():
    out = ''
    while True:
        c = yield
        if c is None:
            print(out)
        else:
            out += c


code = """
function add(a, b){
    /**
    ** Function that adds two items
    **/
    return a + b;
}
add(a, b); /* call add function */
"""

stripper = strip_comments(target=sink())

for c in code:
    stripper.send(c)
stripper.send(None)
