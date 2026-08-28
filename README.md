# Regex Generator

Générateur de regex : l'utilisateur saisit les caractères ou chaînes qu'il veut filtrer, et le programme construit l'expression régulière correspondante.

## Objectif

- Saisir une liste de caractères et/ou de chaînes à filtrer (inclure ou exclure).
- Générer automatiquement la regex correspondante.
- Fournir un aperçu / test de la regex sur un exemple de texte.

## Installation

```bash
pip install -e ".[dev]"
```

## Usage

Mode interactif :

```bash
regexgen
```

Mode non interactif :

```bash
# Regex qui trouve n'importe lequel des tokens
regexgen --tokens "a,b,cd" --mode match
# -> (?:[ab]|(?:cd))

# Regex qui valide qu'une chaîne ne contient aucun des tokens
regexgen --tokens "bad,worse" --mode exclude
# -> ^(?:(?!bad|worse).)*$

# Tester directement la regex générée sur un texte
regexgen --tokens "a,b" --test "banana"
```

- `match` : trouve les occurrences des caractères/chaînes fournis dans un texte.
- `exclude` : valide qu'une chaîne entière ne contient aucun des caractères/chaînes fournis.

## Tests

```bash
pytest
```

## Statut

CLI Python fonctionnelle (modes `match` et `exclude`). Une interface web pourra être ajoutée plus tard.
