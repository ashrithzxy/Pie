import textwrap
def wrap(str, max_width):
    para = textwrap.fill(str, max_width)
    return para
string, max_width = input(), int(input())
result = wrap(string, max_width)
print(result)
