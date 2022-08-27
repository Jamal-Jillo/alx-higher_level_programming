#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        tupl = (0, None)
    else:
        tupl = (len(sentence), sentence[0])
        return tupl
