"""
@name:      TheoremLLC.py
@author:    Pascal R. Jardin
@date:      1/17/2020
@version:   1.0
@contact:   pjardin@me.com
@contact:   this is an interview question about how to flatten an array
"""

#this function is to flatten an array
def flatten(a):
    flat = []
    for e in a:
        if isinstance(e, int):
            flat.append(e)
        elif isinstance(e, list):
            flat += flatten(e)#calls on itself if array in side array
    return flat


# to test: run pytest TheoremLLC.py, it passed in 0.01 secounds
#------------for tetsing--------------
def test0():
    results = flatten([[1,2,[3]],4])
    assert results == [1,2,3,4]

def test1():
    results = flatten([1, [2, 3, [4]], 5, [[6]]])
    assert results == [1, 2, 3, 4, 5, 6]


def test2():
    results = flatten([1, [2, 3, [4], []], [], 5, [[], [6]]])
    assert results == [1, 2, 3, 4, 5, 6]
#------------for tetsing--------------
