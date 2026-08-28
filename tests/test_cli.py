from regex_generator.cli import main


def test_cli_match_mode(capsys):
    exit_code = main(["--tokens", "a,b", "--mode", "match"])
    captured = capsys.readouterr()
    assert exit_code == 0
    assert captured.out.strip() == "[ab]"


def test_cli_exclude_mode(capsys):
    exit_code = main(["--tokens", "a,b", "--mode", "exclude"])
    captured = capsys.readouterr()
    assert exit_code == 0
    assert captured.out.strip() == "^(?:(?!a|b).)*$"


def test_cli_with_test_string(capsys):
    exit_code = main(["--tokens", "a", "--test", "banana"])
    captured = capsys.readouterr()
    assert exit_code == 0
    assert "OK" in captured.out


def test_cli_no_valid_tokens_errors(capsys):
    exit_code = main(["--tokens", "", "--mode", "match"])
    captured = capsys.readouterr()
    assert exit_code == 1
    assert "Erreur" in captured.err
