import sys
from function import resnet_predefined_classify

def get_stdin():
    #buf = ""
    #for line in sys.stdin:
    #    buf = buf + line
    #return buf
    return sys.stdin.read()

if(__name__ == "__main__"):
    st = get_stdin()
    handler.handle(st)