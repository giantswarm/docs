from script import link_pull_requests

if __name__ == "__main__":

    s1 = "Adds something (#123) to fix #45"
    result = link_pull_requests(s1, "org/repo")
    print(result)
    assert result == "Adds something ([#123](https://github.com/org/repo/pull/123)) to fix [#45](https://github.com/org/repo/pull/45)"

    s2 = "Blah blah [otherrepo#7](https://github.com/giantswarm/otherrepo/pull/7)"
    result = link_pull_requests(s2, "org/thisrepo")
    print(result)
    assert result == s2
