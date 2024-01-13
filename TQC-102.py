nums = {
    'a': eval(input()),
    'b': eval(input()),
    'c': eval(input()),
    'd': eval(input())
}
#利用字典儲存4個值

print('|%7.2f %7.2f|' % (nums['a'] ,nums['b']))
#向右印出a, b
print('|{:7.2f} {:7.2f}|'.format(nums['c'], nums['d']))
#向右印出c, d
print('|%-7.2f %-7.2f|' % (nums['a'] ,nums['b']))
#向左印出a, b
print('|{:<7.2f} {:<7.2f}|'.format(nums['c'], nums['d']))
#向左印出c, d


