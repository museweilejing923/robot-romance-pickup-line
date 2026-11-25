"""Robot-romance pickup-line writer.

Writes one fixed neural-network pickup line to /output/entry.txt.
The bytes never change: no input, no clock, no network, no randomness.
"""

import os
import string
import sys

PICKUP = "Are you a neural network? Because every layer of you makes my loss function drop."
MAX_LEN = 200


def complain(problem):
    print("error: " + problem, file=sys.stderr)
    raise SystemExit(1)


def looks_blank(line):
    return line.strip() == ""


def looks_too_long(line):
    return len(line) > MAX_LEN


def has_control(line):
    return any(ord(ch) < 32 or ord(ch) == 127 for ch in line)


def has_bad_spacing(line):
    return line != line.strip() or "  " in line or "\n" in line


def has_triple_repeat(line):
    """True when one character shows up three times in a row.

    "drooop" is a typo, not emphasis, so tripled letters are refused.
    """
    run = 1
    for earlier, later in zip(line, line[1:]):
        if later == earlier:
            run += 1
            if run >= 3:
                return True
        else:
            run = 1
    return False


def check(line):
    if looks_blank(line):
        complain("the line is blank")
    if looks_too_long(line):
        complain("the line is over 200 characters")
    if has_control(line):
        complain("the line has a control character")
    if has_bad_spacing(line):
        complain("the line has bad spacing or a line break")
    if line[-1] not in ".!?":
        complain("the line has no closing punctuation")
    if all(ch in string.punctuation for ch in line):
        complain("the line is only punctuation")
    if line.isdigit():
        complain("the line is only digits")
    if not any(ch.isalpha() for ch in line):
        complain("the line has no letters")
    if "?" not in line:
        complain("the line asks no question")
    if has_triple_repeat(line):
        complain("the line repeats one character three times in a row")


def main():
    check(PICKUP)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(PICKUP + "\n")


if __name__ == "__main__":
    main()
