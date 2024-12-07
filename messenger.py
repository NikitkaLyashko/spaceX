subscribers=[]
def add_sub_def(def_):
    subscribers.append(def_)

def broadcast(mess,who,plus_dok=None):

    for a in subscribers:
        a(mess,who,plus_dok)