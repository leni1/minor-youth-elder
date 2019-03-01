import minor_elder_youth


def test_func_return_youth():
    test_year = '2001'
    test_check_func = minor_elder_youth.check_func(test_year)
    assert test_check_func == 'Youth'


def test_func_return_minor():
    test_year = '2005'
    test_check_func = minor_elder_youth.check_func(test_year)
    assert test_check_func == 'Minor'


def test_func_return_elder():
    test_year = '1948'
    test_check_func = minor_elder_youth.check_func(test_year)
    assert test_check_func == 'Elder'
