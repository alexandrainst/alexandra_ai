"""Unit tests for the imported subpackages."""


def test_evaluator_import():
    from aiai_eval import Evaluator

    assert hasattr(Evaluator, "evaluate")
