import pytest

from sre_agent import main


def test_main_prints_greeting(capsys: pytest.CaptureFixture[str]) -> None:
    main()
    capture = capsys.readouterr()
    expected = "Hello from sre-agent!\n"
    assert capture.out == expected
