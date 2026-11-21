import requests
from pathlib import Path

SOURCE_URL = (
    "https://raw.githubusercontent.com/Override92/AiSList/"
    "main/AiSList/aislist_blocklist.txt"
)

OUTPUT_FILE = "aislist_brave_ios.txt"

FILTER_TEMPLATE = (
    'm.youtube.com##ytm-media-item '
    'a:not([class]):is([href="/{handle}"]):upward(ytm-media-item)'
)


def main():
    print("Downloading AiSList...")

    response = requests.get(SOURCE_URL, timeout=60)
    response.raise_for_status()

    handles = set()

    for line in response.text.splitlines():
        line = line.strip()

        # Ignore empty lines and comments
        if not line or line.startswith("!"):
            continue

        # Keep handles, excluding URL-encoded entries
        if line.startswith("@") and "%" not in line:
            handles.add(line)

    print(f"Found {len(handles)} valid channels")

    filters = [
        FILTER_TEMPLATE.format(handle=handle)
        for handle in sorted(handles, key=str.lower)
    ]

    output = (
        "! AiSList - Brave iOS YouTube channel blocklist\n"
        "! Source: " + SOURCE_URL + "\n"
        f"! Total channels: {len(handles)}\n\n"
        + "\n\n".join(filters)
        + "\n"
    )

    Path(OUTPUT_FILE).write_text(output, encoding="utf-8")

    print(f"Successfully generated {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
