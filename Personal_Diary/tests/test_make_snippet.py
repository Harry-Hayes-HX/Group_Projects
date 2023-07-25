from lib.make_snippet import *


def test_snippets():
    build = make_snippet("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque condimentum rutrum enim non volutpat. Maecenas pretium faucibus placerat. Sed nec placerat nisi. Pellentesque tellus velit, elementum non orci a, porta tempor sapien.")
    assert build == "Lorem ipsum dolor sit amet,..."
