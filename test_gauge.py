from gauge import convert, gauge

def main():
    test_gauge()
    test_convert()
   

def test_convert():
    convert(1/2) == "50%"


def test_gauge():
    ...


if __name__ == "__main__":
    main()