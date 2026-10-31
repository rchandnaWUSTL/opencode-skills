#!/usr/bin/env python3
"""Scan text for AI-writing tells and rhythm uniformity.

Usage:
    python3 scan.py FILE [FILE ...]
    cat draft.md | python3 scan.py -

Reports, per input:
  - word count, em dashes per 1,000 words
  - sentence length mean / spread (low spread = uniform, machine-like rhythm)
  - repeated sentence openers
  - every pattern hit, grouped by category, with line numbers

Run it before and after a humanize pass and compare. Hits are prompts to
look, not verdicts: one hit is style, a cluster is a diagnosis.
Stdlib only.
"""

import re
import statistics
import sys
from collections import Counter

# (category, label, regex). Case-insensitive, matched per line.
PATTERNS = [
    # Constructions
    ("construction", "negation-reveal", r"\b(it'?s|this is|that'?s|is) not (just |only |merely |about )?[^.?!]{1,60}[,.;:—-]+\s*(it'?s|but|this is)\b"),
    ("construction", "not just / not only", r"\b(not (just|only|merely)|more than just|isn'?t just|aren'?t just)\b"),
    ("construction", "rather-than correction", r"\brather than\b"),
    ("construction", "copula avoidance", r"\b(serves as|stands as|acts as a|functions as|boasts|marks a)\b"),
    ("construction", "hollow -ing tail", r",\s+(highlighting|underscoring|emphasizing|showcasing|ensuring|fostering|reflecting|demonstrating|illustrating|signaling|cementing|solidifying|paving)\b"),
    ("construction", "significance flourish", r"\b(it'?s (important|worth|crucial) (to note|noting)|crucially|a testament to|what'?s (remarkable|notable|interesting) is|plays? a (pivotal|crucial|vital|key) role|setting the stage|key turning point|enduring legacy)\b"),
    ("construction", "register announcement", r"\b(to be honest|honest caveat|let me be (direct|clear)|here'?s the thing|fair question|the short answer|the truth is)\b"),
    ("construction", "hedging filler", r"\b(generally speaking|to some extent|in many ways|it could be argued|arguably)\b"),
    ("construction", "phantom attribution", r"\b(experts (say|argue|agree|believe|suggest)|studies (show|suggest|have shown)|research (shows|suggests)|industry (reports|observers)|observers (have )?(noted|cited)|critics (argue|say)|many (believe|argue))\b"),
    ("construction", "signposting", r"\b(let'?s (dive|delve|take a look|explore|break)|here'?s (what you need to know|why|how)|in this (post|article|guide),? (we|i)'?ll|without further ado)\b"),
    ("construction", "wrap-up", r"^\s*(in (summary|conclusion|short)|to (sum up|summarize|wrap up)|overall|ultimately|all in all)\b"),
    ("construction", "stock challenges/outlook", r"\b(despite (its|their|these) [^.]{0,40}(faces|face|challenges)|future outlook|looking ahead|remains to be seen)\b"),
    # Chatbot residue
    ("residue", "chatbot residue", r"\b(certainly!|great question|i hope this (helps|email finds you)|let me know if|feel free to|don'?t hesitate to|as an ai|based on (the )?available information|while specific details are limited|happy to help)\b"),
    # Vocabulary
    ("vocabulary", "AI-era word", r"\b(delve[sd]?|delving|tapestry|robust|seamless(ly)?|leverag(e|es|ed|ing)|streamline[sd]?|underscor(e|es|ed|ing)|pivotal|crucial|foster(s|ed|ing)?|comprehensive|landscape|empower(s|ed|ing)?|elevate[sd]?|meticulous(ly)?|realm|garner(s|ed)?|showcas(e|es|ed|ing)|testament|intricate|multifaceted|nuanced|holistic|enhanc(e|es|ed|ing)|align(s)? with|navigat(e|ing) the|ever-evolving|game-?changer|cutting-edge|unparalleled)\b"),
    ("vocabulary", "brochure tone", r"\b(nestled|vibrant|in the heart of|renowned|bustling|breathtaking|rich (history|heritage|tapestry)|commitment to|diverse array|world-class|state-of-the-art)\b"),
    ("vocabulary", "puffery", r"\b(significantly|dramatically|greatly|vastly|remarkabl[ey]|incredibl[ey]|truly) (improv|increas|reduc|enhanc|boost|better|faster|easier)"),
    # Formatting
    ("formatting", "em dash", r"—|\s--\s"),
    ("formatting", "emoji lead", r"^\s*([-*]\s*)?[\U0001F300-\U0001FAFF☀-➿]"),
    ("formatting", "bold-label bullet", r"^\s*([-*]|\d+\.)\s+\*\*[^*]{1,60}\*\*"),
    ("formatting", "colon-subtitle header", r"^#{1,6}\s+[^:\n]+:\s+\S"),
    ("formatting", "title-case header", r"^#{1,6}\s+([A-Z][a-z]+\s+){2,}[A-Z][a-z]+\s*$"),
]

COMPILED = [(c, l, re.compile(p, re.IGNORECASE if c != "formatting" else 0)) for c, l, p in PATTERNS]

FENCE = re.compile(r"^\s*(```|~~~)")


def strip_code(lines):
    """Blank out fenced code blocks and inline code so they don't count."""
    out, in_fence = [], False
    for line in lines:
        if FENCE.match(line):
            in_fence = not in_fence
            out.append("")
            continue
        out.append("" if in_fence else re.sub(r"`[^`]*`", "", line))
    return out


def sentences(text):
    text = re.sub(r"^\s*([-*#>]+|\d+\.)\s*", "", text, flags=re.MULTILINE)
    parts = re.split(r"(?<=[.!?])\s+|\n{2,}", text)
    return [p.strip() for p in parts if len(p.split()) >= 3]


def scan(name, raw):
    lines = strip_code(raw.splitlines())
    text = "\n".join(lines)
    words = len(re.findall(r"\b\w[\w'-]*\b", text))
    print(f"=== {name} ===")
    if words == 0:
        print("  (no prose)\n")
        return

    dashes = len(re.findall(r"—|\s--\s", text))
    sents = sentences(text)
    lens = [len(s.split()) for s in sents]
    print(f"  words: {words}   em dashes: {dashes} ({dashes * 1000 / words:.1f} per 1k words)")
    if len(lens) >= 4:
        mean = statistics.mean(lens)
        sd = statistics.pstdev(lens)
        cv = sd / mean if mean else 0
        flag = "  <- uniform rhythm, vary it" if cv < 0.4 else ""
        print(f"  sentences: {len(lens)}   length mean {mean:.1f}, sd {sd:.1f}, spread (cv) {cv:.2f}{flag}")

    openers = Counter(s.split()[0].lower().strip("\"'*") for s in sents)
    repeated = [(w, n) for w, n in openers.most_common(5) if n >= 3 and n / max(len(sents), 1) >= 0.15]
    if repeated:
        print("  repeated openers: " + ", ".join(f"'{w}' x{n}" for w, n in repeated))

    hits = []
    for i, line in enumerate(lines, 1):
        for cat, label, rx in COMPILED:
            for m in rx.finditer(line):
                hits.append((cat, label, i, m.group(0).strip()))

    by_label = Counter((c, l) for c, l, _, _ in hits)
    print(f"  pattern hits: {len(hits)} ({len(hits) * 1000 / words:.1f} per 1k words)")
    for cat in ("residue", "construction", "vocabulary", "formatting"):
        group = [h for h in hits if h[0] == cat]
        if not group:
            continue
        print(f"  [{cat}]")
        for (c, label), n in sorted(by_label.items(), key=lambda kv: -kv[1]):
            if c != cat:
                continue
            where = [f"L{i}:{m!r}" for cc, ll, i, m in group if ll == label][:6]
            more = f" (+{n - 6} more)" if n > 6 else ""
            print(f"    {label} x{n}: " + ", ".join(where) + more)

    words_hit = Counter(m.lower() for c, l, _, m in hits if l == "AI-era word")
    clustered = [w for w, n in words_hit.items() if n >= 2]
    if len(words_hit) >= 3 or clustered:
        print("  note: AI-era vocabulary is clustering; one word is noise, several is a tell")
    print()


def main(argv):
    if not argv:
        print(__doc__)
        return 2
    for path in argv:
        if path == "-":
            scan("stdin", sys.stdin.read())
        else:
            with open(path, encoding="utf-8") as f:
                scan(path, f.read())
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
