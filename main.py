#!/usr/bin/env python3
"""Write the Perfect Pickup Line entry to /output/entry.txt."""
import os

# Perfect Pickup Line entry: 64 characters.
PICKUP_LINE = "Are you my OTP? Because you are the only code I want to receive."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
    f.write(PICKUP_LINE)
