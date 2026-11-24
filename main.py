"""One Line of Earned Pride -- make.fun bounty entry.

Bounty: "One Line of Earned Pride"
(https://make.fun/bounty/u-mang-one-line-of-earned-pride-a0138557)

The entry is a single line of text, 1 to 240 characters: a quiet, earned
moment of pride for someone in a scene. The line is built here from three
named parts, kept in order in one tuple so each beat of the moment is
visible in the code and the line can only be assembled in that order:

  * setup   -- who Mara is in this moment, hands shaking over the work;
  * effort  -- the long difficulty carried into the scene (since March);
  * landing -- the seam holds, and the held breath finally lets go.

No trophy, no podium, no graduation: the pride arrives with the exhale,
in the last words, and nowhere is it asserted, congratulated or explained.
The program prints exactly that line and nothing else.
"""

# The line, in three beats, in order: who, what it cost, how it lands.
PARTS = (
    "Mara's hands shook as she lowered the welding torch,",  # setup
    "but the seam held,",  # effort
    "and she finally let out the breath she'd been holding since March.",  # landing
)

# The bounty gate: a valid entry is 1 to 240 characters of UTF-8 text.
MIN_LENGTH = 1
MAX_LENGTH = 240


def join_parts(*parts):
    """Join the beats of the line with single spaces, no extra whitespace."""
    return " ".join(part.strip() for part in parts if part.strip())


def build_line():
    """Assemble the entry line from its named parts, in order."""
    return join_parts(*PARTS)


def validate_line(line):
    """Check the line against the bounty gate before it is printed."""
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not MIN_LENGTH <= len(line) <= MAX_LENGTH:
        raise ValueError(
            "entry must be %d-%d characters, got %d"
            % (MIN_LENGTH, MAX_LENGTH, len(line))
        )
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    if "  " in line:
        raise ValueError("entry must not contain double spaces")
    if not line.endswith("."):
        raise ValueError("entry must end with a full stop")
    return line


def main():
    line = validate_line(build_line())
    print(line)


if __name__ == "__main__":
    main()
