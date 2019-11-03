import pickle as p
class D:
    def l(s):s.__dict__=p.load(open('d', 'rb')).__dict__
    def __setattr__(s, k, v):super(D, s).__setattr__(k, v);p.dump(s, open('d', 'wb'))