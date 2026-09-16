from datetime import date, datetime, timedelta, timezone

from script import as_utc, link_pull_requests, resolve_relative_links

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

    # Test as_utc
    print("\nTesting as_utc:")

    # A bare date becomes midnight UTC
    assert as_utc(date(2025, 3, 14)) == datetime(2025, 3, 14, tzinfo=timezone.utc)

    # A naive datetime is assumed to be UTC already
    assert as_utc(datetime(2025, 3, 14, 9, 30)) == datetime(2025, 3, 14, 9, 30, tzinfo=timezone.utc)

    # An aware datetime is converted to UTC
    cet = timezone(timedelta(hours=1))
    assert as_utc(datetime(2025, 3, 14, 9, 30, tzinfo=cet)) == datetime(2025, 3, 14, 8, 30, tzinfo=timezone.utc)

    # Front matter date strings are parsed, with and without offset
    assert as_utc('2025-03-14T09:30:00') == datetime(2025, 3, 14, 9, 30, tzinfo=timezone.utc)
    assert as_utc('2025-03-14T09:30:00+01:00') == datetime(2025, 3, 14, 8, 30, tzinfo=timezone.utc)
    print("as_utc: ok")

    # Test the age comparison as the script performs it
    print("\nTesting age cutoff:")
    now = datetime(2026, 9, 16, 12, 0, tzinfo=timezone.utc)
    cutoff = now - timedelta(days=365)

    # One day inside the window is kept, one day outside is dropped
    assert as_utc('2025-09-17T00:00:00') >= cutoff
    assert as_utc('2025-09-15T00:00:00') < cutoff

    # Mixed sources compare correctly against the cutoff
    assert as_utc(date(2019, 2, 22)) < cutoff
    assert as_utc(datetime(2026, 9, 15, 6, 49, 10)) >= cutoff
    print("age cutoff: ok")

    print("\nAll tests passed!")
