# https://www.agiliq.com/blog/2012/06/understanding-args-and-kwargs/
# Additional Reference

"""  When use only positional arguments """
def save_ranking1(*args):
    print(args)


save_ranking1("ming", "alice", "tom", "wilson", "roy")
# ['ming', 'alice', 'tom', 'wilson', 'roy']


""" When use only keyword arguments """
def save_ranking2(**kwargs):
    print(kwargs)


save_ranking2(first="ming", second="alice", fourth="wilson", third="tom", fifth="roy")
# {'first': 'ming', 'second': 'alice', 'fourth': 'wilson', 'third': 'tom', 'fifth': 'roy'}


""" When use both positional arguments and keyword arguments """
def save_ranking3(*args, **kwargs):
    print(args)
    print(kwargs)


save_ranking3(
    "ming", "alice", "tom", test2="wilson", test1="roy"
)  
# ('ming', 'alice', 'tom')
# {'test2': 'wilson', 'test1': 'roy'}
