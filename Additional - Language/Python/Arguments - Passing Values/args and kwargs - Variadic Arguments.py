# https://medium.com/understand-the-python/understanding-the-asterisk-of-python-8b9daaa4a558


# A function that shows the results of running competitions consisting of 2 to 4 runners.
def save_ranking(first, second, third=None, fourth=None, *args, **kwargs):
    rank = {}
    rank[1], rank[2] = first, second
    rank[3] = third if third is not None else "Nobody"
    rank[4] = fourth if fourth is not None else "Nobody"
    rank[5] = args
    rank[6] = kwargs

    print(rank)


# Pass the 2 positional arguments
save_ranking("alice", "ming")
# {1: 'alice', 2: 'ming', 3: 'Nobody', 4: 'Nobody', 5: (), 6: {}}

# Pass the 4 positional arguments
save_ranking("alice", "ming", "mike", "jim")
# {1: 'alice', 2: 'ming', 3: 'mike', 4: 'jim', 5: (), 6: {}}

# Pass the 2 positional arguments and 2 keyword arguments (But, one of them was passed as like positional argument)
save_ranking("alice", "ming", fourth="jim", third="mike")
# {1: 'alice', 2: 'ming', 3: 'mike', 4: 'jim', 5: (), 6: {}}

save_ranking(
    "alice", "ming", "mike", "jim", "t", "e", "s", "t", t="t", e="e", s="s", tt="tt"
)
# {1: 'alice', 2: 'ming', 3: 'mike', 4: 'jim', 5: ('t', 'e', 's', 't'), 6: {'t': 't', 'e': 'e', 's': 's', 'tt': 'tt'}}
