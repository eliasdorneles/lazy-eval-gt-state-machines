import re


def strip_comments(code):
    COMMENT_REGEX = '/[*]([^*]|[*][^/])*[*]/'
    return re.sub(COMMENT_REGEX, '', code)


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
