from source.example.ex2.foobar_plus import foo_plus, bar_plus

def test_fib():
    assert bar_plus() == "bar" + " and more"
    assert foo_plus() == "foo" + " and more"
