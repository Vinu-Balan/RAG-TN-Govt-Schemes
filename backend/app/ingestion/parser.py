import hashlib


def clean_text(text: str):
    lines = text.split("\n")

    clean_lines = []
    seen = set()

    for line in lines:
        line = line.strip()

        if len(line) < 50:
            continue

        # Remove noise
        if any(keyword in line.lower() for keyword in [
            "skip to content",
            "copyright",
            "all rights reserved",
            "privacy policy",
            "terms of use",
            "policy notes"
        ]):
            continue

        # Deduplicate
        hash_val = hashlib.md5(line.encode()).hexdigest()
        if hash_val in seen:
            continue
        seen.add(hash_val)

        clean_lines.append(line)

    return "\n".join(clean_lines)


# Section extraction
def extract_sections(text: str):
    sections = []
    current = {"title": "General", "content": ""}

    for line in text.split("\n"):
        if len(line) < 100 and line.isupper():
            if current["content"]:
                sections.append(current)
            current = {"title": line, "content": ""}
        else:
            current["content"] += " " + line

    if current["content"]:
        sections.append(current)

    return sections