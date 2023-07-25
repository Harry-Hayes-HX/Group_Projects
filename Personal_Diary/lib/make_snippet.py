def make_snippet(string):
    sentence = string.split()
    first_five = " ".join(sentence[:5])
    return first_five + "..."
make_snippet("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque condimentum rutrum enim non volutpat. Maecenas pretium faucibus placerat. Sed nec placerat nisi. Pellentesque tellus velit, elementum non orci a, porta tempor sapien.")
