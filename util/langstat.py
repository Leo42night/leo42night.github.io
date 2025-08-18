#!/data/data/com.termux/files/usr/bin/python

import os
from collections import defaultdict

stats = defaultdict(int)
total = 0

for root, _, files in os.walk("."):
    for f in files:
        _, ext = os.path.splitext(f)
        if ext:  # hanya file dengan ekstensi
            try:
                with open(os.path.join(root, f), "r", encoding="utf-8", errors="ignore") as file:
                    lines = sum(1 for _ in file)
                    stats[ext] += lines
                    total += lines
            except Exception:
                pass

for ext, count in sorted(stats.items(), key=lambda x: x[1], reverse=True):
    print(f"{ext}: {count} lines ({count/total*100:.2f}%)")

print(f"\nTotal: {total} lines")
