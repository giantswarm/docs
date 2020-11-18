from script import link_pull_requests

if __name__ == "__main__":

    s = "Adds something (#123) to fix #45"
    result = link_pull_requests(s, "org/repo")
    print(result)
    assert result == "Adds something ([#123](https://github.com/org/repo/pulls/123)) to fix [#45](https://github.com/org/repo/pulls/45)"