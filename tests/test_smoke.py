import importlib


def test_main_exists():
    mod = importlib.import_module("promptforge_cli.cli")
    assert hasattr(mod, "main")
