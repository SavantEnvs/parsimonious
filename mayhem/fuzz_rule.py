#!/usr/bin/env python3

import atheris
import sys
import fuzz_helpers

with atheris.instrument_imports(include=['parsimonious']):
    from parsimonious.grammar import Grammar


from parsimonious.exceptions import BadGrammar, IncompleteParseError, ParseError, UndefinedLabel, VisitationError


def TestOneInput(data):
    fdp = fuzz_helpers.EnhancedFuzzedDataProvider(data)
    try:
        grammar = Grammar(fdp.ConsumeRandomString())
        grammar.parse(fdp.ConsumeRandomString())
    except RecursionError:
        raise
    except (RuntimeError, ParseError, IncompleteParseError, BadGrammar, UndefinedLabel, VisitationError):
        return -1
def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
