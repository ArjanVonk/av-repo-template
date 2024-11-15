from {{ cookiecutter.__package_slug }}.{{ cookiecutter.__package_slug }} import hello_world


def test_hello_world():
    hello_world()