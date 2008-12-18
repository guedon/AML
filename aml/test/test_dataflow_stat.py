from openalea.core.alea import *

pm = PackageManager()
pm.init(verbose=False)

def test_demo_corsican():
    """ Test changepoint demo corsican  """
    res = run(('demo.changepoint','Corsican pine change point'),{},pm=pm)
    assert res == []

def test_demo_mtg_multiplemtg():
    """ Test dataflow demo dycorinia """
    res = run(('demo.changepoint','Dycorinia change point'),{},pm=pm)
    assert res == []
