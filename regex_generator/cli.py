import argparse
import re
import sys

from .builder import build_exclude_regex, build_match_regex


def parse_tokens(raw: str) -> list[str]:
    tokens = [t.strip() for t in raw.split(",") if t.strip()]
    if not tokens:
        raise ValueError("Aucun caractère ou chaîne valide fourni.")
    return tokens


def prompt_tokens() -> list[str]:
    raw = input("Caractères/chaînes à filtrer (séparés par des virgules) : ")
    return parse_tokens(raw)


def prompt_mode() -> str:
    choice = input("Mode [match/exclude] (défaut: match) : ").strip().lower()
    return choice or "match"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="regexgen",
        description="Génère une regex à partir de caractères/chaînes à filtrer.",
    )
    parser.add_argument(
        "-t",
        "--tokens",
        help="Caractères/chaînes à filtrer, séparés par des virgules (ex: 'a,b,cd'). "
        "Si omis, une saisie interactive est proposée.",
    )
    parser.add_argument(
        "-m",
        "--mode",
        choices=["match", "exclude"],
        default="match",
        help="match : la regex trouve les tokens dans un texte. "
        "exclude : la regex valide qu'une chaîne entière n'en contient aucun. Défaut : match.",
    )
    parser.add_argument(
        "--test",
        help="Texte optionnel sur lequel tester la regex générée.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        if args.tokens is not None:
            tokens = parse_tokens(args.tokens)
            mode = args.mode
        else:
            tokens = prompt_tokens()
            mode = prompt_mode()

        if mode not in ("match", "exclude"):
            raise ValueError(f"Mode invalide : {mode}")

        pattern = build_match_regex(tokens) if mode == "match" else build_exclude_regex(tokens)
    except ValueError as exc:
        print(f"Erreur : {exc}", file=sys.stderr)
        return 1

    print(pattern)

    if args.test is not None:
        compiled = re.compile(pattern)
        result = compiled.search(args.test) if mode == "match" else compiled.fullmatch(args.test)
        print(f"Test sur {args.test!r} : {'OK' if result else 'NON'}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
