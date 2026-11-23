"""Shared test setup: put the modules under test on the import path."""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
FIXTURES = os.path.join(HERE, "fixtures")


def load_fixture(name):
    with open(os.path.join(FIXTURES, name), encoding="utf-8") as f:
        return json.load(f)


def read_page(name):
    with open(os.path.join(FIXTURES, "pages", name), encoding="utf-8") as f:
        return f.read()
