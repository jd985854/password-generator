import argparse
import secrets
import string

# Small sample wordlist for Diceware passphrases
WORD_LIST = [
    "correct", "horse", "battery", "staple", "cipher", "matrix",
    "shield", "vector", "kernel", "shadow", "anchor", "beacon",
    "dragon", "fossil", "galaxy", "harbor", "island", "jungle"
]

def generate_random_password(length=16, use_digits=True, use_symbols=True, exclude_ambiguous=False):
    """Generates a cryptographically secure random password."""
    letters = string.ascii_letters
    digits = string.digits if use_digits else ""
    symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?" if use_symbols else ""

    if exclude_ambiguous:
        ambiguous = "O0I1lI"
        letters = "".join([c for c in letters if c not in ambiguous])
        digits = "".join([c for c in digits if c not in ambiguous])

    character_pool = letters + digits + symbols

    if not character_pool:
        raise ValueError("At least one character set must be selected.")

    while True:
        password = "".join(secrets.choice(character_pool) for _ in range(length))
        
        # Ensure password contains at least one character from each requested pool
        has_letter = any(c in letters for c in password)
        has_digit = not use_digits or any(c in digits for c in password)
        has_symbol = not use_symbols or any(c in symbols for c in password)

        if has_letter and has_digit and has_symbol:
            return password

def generate_passphrase(words=4, separator="-"):
    """Generates a Diceware-style memorable passphrase."""
    chosen_words = [secrets.choice(WORD_LIST) for _ in range(words)]
    return separator.join(chosen_words)

def main():
    parser = argparse.ArgumentParser(description="Cryptographically Secure Password Generator")
    parser.add_argument("-l", "--length", type=int, default=16, help="Length of password (default: 16)")
    parser.add_argument("--no-digits", action="store_true", help="Exclude digits")
    parser.add_argument("--no-symbols", action="store_true", help="Exclude symbols")
    parser.add_argument("--clean", action="store_true", help="Exclude ambiguous characters (O, 0, I, 1, l)")
    parser.add_argument("--passphrase", action="store_true", help="Generate a memorable word passphrase instead")
    parser.add_argument("-w", "--words", type=int, default=4, help="Number of words for passphrase (default: 4)")

    args = parser.parse_args()

    print("=" * 45)
    print("      SECURE PASSWORD GENERATOR CLI           ")
    print("=" * 45)

    if args.passphrase:
        result = generate_passphrase(words=args.words)
        print(f"Generated Passphrase : {result}")
    else:
        result = generate_random_password(
            length=args.length,
            use_digits=not args.no_digits,
            use_symbols=not args.no_symbols,
            exclude_ambiguous=args.clean
        )
        print(f"Generated Password   : {result}")
    
    print("=" * 45)

if __name__ == "__main__":
    main()
