import re


def build_match_regex(tokens: list[str]) -> str:
    """Regex qui trouve n'importe laquelle des occurrences fournies."""
    if not tokens:
        raise ValueError("Aucun caractère ou chaîne fourni.")

    chars = sorted({t for t in tokens if len(t) == 1})
    strings = sorted({t for t in tokens if len(t) > 1})

    parts = []
    if chars:
        parts.append("[" + "".join(re.escape(c) for c in chars) + "]")
    if strings:
        parts.append("(?:" + "|".join(re.escape(s) for s in strings) + ")")

    return parts[0] if len(parts) == 1 else "(?:" + "|".join(parts) + ")"


def build_exclude_regex(tokens: list[str]) -> str:
    """Regex qui valide une chaîne entière ne contenant aucune des occurrences fournies."""
    if not tokens:
        raise ValueError("Aucun caractère ou chaîne fourni.")

    alternation = "|".join(re.escape(t) for t in sorted(set(tokens)))
    return f"^(?:(?!{alternation}).)*$"
