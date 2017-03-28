CODE, COMMENT, MAYBE_COMMENT, MAYBE_END_COMMENT = tuple(range(4))


def strip_comments(code):
    out = ''
    state = CODE
    prev_c = ''
    for c in code:
        if state == CODE:
            if c == '/':
                state = MAYBE_COMMENT
            else:
                out += c
        elif state == COMMENT:
            if c == '*':
                state = MAYBE_END_COMMENT
            else:
                state = COMMENT
        elif state == MAYBE_COMMENT:
            if c == '*':
                state = COMMENT
            else:
                state = CODE
                out += prev_c + c
        elif state == MAYBE_END_COMMENT:
            if c == '/':
                state = CODE
            elif c == '*':
                state = MAYBE_END_COMMENT
            else:
                state = COMMENT
        prev_c = c
    return out

code = """
function add(a, b){
    /**
    * Function that adds two items
    **/
    return a + b;
}
add(a, b); /* call add function */
"""

print(strip_comments(code))
