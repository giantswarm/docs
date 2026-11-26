import os
import sys
import unittest
import urllib.parse
from unittest import mock

import support  # noqa: F401 - sets up the import path

sys.path.insert(0, os.path.join(support.HERE, "..", ".."))
import run  # noqa: E402


class FakeResponse:
    def read(self):
        return b'{"hits": {"hits": [{"_source": {"url": "/a/"}}]}}'

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False


def requested_query(**kwargs):
    seen = []

    def fake_urlopen(req, timeout=None):
        seen.append(urllib.parse.parse_qs(urllib.parse.urlsplit(req.full_url).query))
        return FakeResponse()

    with mock.patch.object(run.urllib.request, "urlopen", side_effect=fake_urlopen):
        hits, _ = run.fetch("https://gw/searchapi/", "login", "Documentation", 5, 3.0, **kwargs)
    return seen[0], hits


class TestFetch(unittest.TestCase):
    def test_docs_query_has_no_breadcrumb(self):
        query, hits = requested_query()
        self.assertEqual(query, {"q": ["login"], "type": ["Documentation"], "size": ["5"]})
        self.assertEqual(hits, [{"url": "/a/"}])

    def test_changes_query_is_a_documentation_query_narrowed_to_changes(self):
        query, _ = requested_query(breadcrumb="changes")
        self.assertEqual(query["type"], ["Documentation"])
        self.assertEqual(query["breadcrumb"], ["changes"])


class TestChangesSize(unittest.TestCase):
    def test_reads_changes_size(self):
        self.assertEqual(run.changes_size({"changes_size": 7}), 7)

    def test_an_older_query_set_names_it_blog_size(self):
        self.assertEqual(run.changes_size({"blog_size": 4}), 4)

    def test_defaults_to_the_widget_size(self):
        self.assertEqual(run.changes_size({}), 5)


if __name__ == "__main__":
    unittest.main()
