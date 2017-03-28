# try:
#     print 'trying...'
#     r = 10/0
#     print 'result',r
# except BaseException,e:
#     print  'except:',e
# finally:
#     print 'finally...'
# print  'END'
def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    try:
        bar('0')
    except StandardError, e:
        print  'error %s' % e
    finally:
        print 'finally...'


main()
