from source.example.ex2.foobar import foo, bar

def test_foo():
    assert foo() == "foo"

def test_bar():
    assert bar() == "bar"
