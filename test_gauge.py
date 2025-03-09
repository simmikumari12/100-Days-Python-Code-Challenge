from gauge import convert, gauge
import pytest

def main():
    test_gauge()
    test_convert_value()
    test_convert_errors()
   

def test_convert_value():
    assert convert("1/2") == 50
    assert convert("2/3") == 67

def test_convert_errors():
    with pytest.raises(ValueError):
        convert("3/2")
    with pytest.raises(ZeroDivisionError):
        convert("0/0")
    with pytest.raises(ZeroDivisionError):
        convert("32/0")
    with pytest.raises(ValueError):
        convert("a/dh")
    with pytest.raises(ValueError):
        convert("adh")
    with pytest.raises(ValueError):
        convert("21")

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(0) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(50) == "50%"
    assert gauge(24) == "24%"


if __name__ == "__main__":
    main()