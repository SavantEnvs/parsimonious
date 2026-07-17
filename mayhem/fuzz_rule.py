#!/usr/bin/env python3

import atheris
import sys
import fuzz_helpers

with atheris.instrument_imports(include=['parsimonious']):
    from parsimonious.grammar import Grammar


from parsimonious.exceptions import IncompleteParseError, UndefinedLabel, ParsimoniousError


def TestOneInput(data):
    fdp = fuzz_helpers.EnhancedFuzzedDataProvider(data)
    try:
        grammar = Grammar(fdp.ConsumeRandomString())
        grammar.parse(fdp.ConsumeRandomString())
    except (RuntimeError, IncompleteParseError, UndefinedLabel, ParsimoniousError):
        return -1
def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
