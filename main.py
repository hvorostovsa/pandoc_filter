from panflute import *
import sys

headers = {}


def upper_str(elem, doc):
    if isinstance(elem, Str):
        elem.text = elem.text.upper()


def action(elem, doc):
    if isinstance(elem, Header):
        string = stringify(elem)
        if string in headers.keys():
            if headers.get(string) == elem.level:
                sys.stderr.write("Header repeated:  " + string + ". Level: " + str(elem.level))
        else:
            headers[string] = elem.level

    if isinstance(elem, Str) and elem.text.lower() == "bold":
        return Strong(elem)

    if isinstance(elem, Header) and elem.level <= 3:
        return elem.walk(upper_str)


def main(doc=None):
    return run_filter(action, doc=doc)


if __name__ == "__main__":
    main()
