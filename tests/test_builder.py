import re

import pytest

from regex_generator.builder import build_exclude_regex, build_match_regex


def test_match_single_chars():
    regex = re.compile(build_match_regex(["a", "b", "c"]))
    assert regex.search("xbz")
    assert not regex.search("xyz")


def test_match_strings():
    regex = re.compile(build_match_regex(["cd", "ef"]))
    assert regex.search("abcdxx")
    assert regex.search("xxefxx")
    assert not regex.search("abxx")


def test_match_mixed_chars_and_strings():
    regex = re.compile(build_match_regex(["a", "cd"]))
    assert regex.search("xax")
    assert regex.search("xcdx")
    assert not regex.search("xbx")


def test_match_escapes_special_characters():
    regex = re.compile(build_match_regex(["."]))
    assert regex.search("a.b")
    assert not regex.search("axb")


def test_match_empty_tokens_raises():
    with pytest.raises(ValueError):
        build_match_regex([])


def test_exclude_single_chars():
    regex = re.compile(build_exclude_regex(["a", "b"]))
    assert regex.fullmatch("xyz")
    assert not regex.fullmatch("xay")


def test_exclude_strings():
    regex = re.compile(build_exclude_regex(["bad", "worse"]))
    assert regex.fullmatch("this is fine")
    assert not regex.fullmatch("this is bad")
    assert not regex.fullmatch("this is worse")


def test_exclude_empty_tokens_raises():
    with pytest.raises(ValueError):
        build_exclude_regex([])
