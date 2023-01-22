#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# jsonmerge.py by shinrax2
VERSION = "0.1"

import json
import sys

print(f"jsonmerge {VERSION} by shinrax2")
print("Usage: jsonmerge BASEFILE HEADFILE OUTPUTFILE")
print("HEADFILE will be merged into BASEFILE, output will be written to OUTPUTFILE")
if len(sys.argv) < 4:
    sys.exit(0)

head_path = sys.argv[2]
base_path = sys.argv[1]
out_path = sys.argv[3]

with open(base_path, "r", encoding="utf8") as f:
    base = json.loads(f.read())
with open(head_path, "r", encoding="utf8") as f:
    head = json.loads(f.read())

for k, v in head.items():
    base[k] = v

with open(out_path, "w", encoding="utf8") as f:
    f.write(json.dumps(base, sort_keys=True, indent=4, ensure_ascii=False))