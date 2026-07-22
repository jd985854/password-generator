# Secure Password Generator CLI

A command-line tool written in Python that generates cryptographically secure passwords and memorable passphrases using Python's `secrets` library.

## Features
- **Cryptographically Secure**: Utilizes OS-level CSPRNG source via `secrets`.
- **Customizable**: Control length, include/exclude digits, special symbols, or ambiguous characters (`O`, `0`, `I`, `1`).
- **Passphrase Mode**: Generates human-friendly, Diceware-style multi-word passphrases.

## Installation & Setup

1. **Clone repository:**
   ```bash
   git clone [https://github.com/YOUR-USERNAME/password-generator.git](https://github.com/YOUR-USERNAME/password-generator.git)
   cd password-generator
2.**Run the generator:**
```bash
# Basic 16-character password
python generator.py

# 24-character clean password (no ambiguous characters)
python generator.py -l 24 --clean

# Memorable 5-word passphrase
python generator.py --passphrase -w 5
