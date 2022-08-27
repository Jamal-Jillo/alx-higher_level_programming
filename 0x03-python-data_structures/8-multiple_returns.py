#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        return None
    else:
        tupl = (len(sentence), sentence[0])
        return tupl
