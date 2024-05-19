import Recode1 as R

def test_cost():
    expected_result=18.0
    test_result=R.cost_of_fruits('pear', 20)
    assert(test_result==expected_result)


def test_totalcost():
    test_result=R.total_cost_shopping()
    assert(test_result==46.75)
    



















