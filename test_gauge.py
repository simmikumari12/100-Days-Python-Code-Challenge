from gauge import convert, gauge
import pytest

def main():
    test_gauge()
    test_convert()
   

def test_convert():
    assert convert(1/2) == "50%"
    assert convert(2/3) == "67%"
    with pytest.raises(ValueError):
        convert(3/2)


def test_gauge():
    ...


if __name__ == "__main__":
    main()