from script import link_pull_requests, resolve_relative_links

if __name__ == "__main__":

    s1 = "Adds something (#123) to fix #45"
    result = link_pull_requests(s1, "org/repo")
    print(result)
    assert result == "Adds something ([#123](https://github.com/org/repo/pull/123)) to fix [#45](https://github.com/org/repo/pull/45)"

    s2 = "Blah blah [otherrepo#7](https://github.com/giantswarm/otherrepo/pull/7)"
    result = link_pull_requests(s2, "org/thisrepo")
    print(result)
    assert result == s2

    # Test resolve_relative_links
    print("\nTesting resolve_relative_links:")

    # Test relative link with ./ and 'main' branch
    s3 = "See [changelog](./docs/releases/v0.95.0-changelog.md) for more info."
    result = resolve_relative_links(s3, "giantswarm/backstage", "main")
    print(result)
    assert result == "See [changelog](https://github.com/giantswarm/backstage/blob/main/docs/releases/v0.95.0-changelog.md) for more info."

    # Test relative link without ./ and 'master' branch
    s4 = "Check the [README](README.md)."
    result = resolve_relative_links(s4, "giantswarm/oldrepo", "master")
    print(result)
    assert result == "Check the [README](https://github.com/giantswarm/oldrepo/blob/master/README.md)."

    # Test that absolute URLs are not modified
    s5 = "See [docs](https://example.com/docs) and [guide](./guide.md)."
    result = resolve_relative_links(s5, "giantswarm/backstage", "main")
    print(result)
    assert result == "See [docs](https://example.com/docs) and [guide](https://github.com/giantswarm/backstage/blob/main/guide.md)."

    # Test that anchors are not modified
    s6 = "Jump to [section](#section) or read [more](./more.md)."
    result = resolve_relative_links(s6, "giantswarm/backstage", "main")
    print(result)
    assert result == "Jump to [section](#section) or read [more](https://github.com/giantswarm/backstage/blob/main/more.md)."

    print("\nAll tests passed!")
