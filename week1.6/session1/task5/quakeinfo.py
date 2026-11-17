# Week 1.6, Session 1: Task 5

import sys

from dataset import QuakeDataset
from feed import QuakeFeed


if len(sys.argv) == 3:
    level = sys.argv[1]
    period = sys.argv[2]
else:
    level = input("Significance level: ").strip()
    period = input("Time period: ").strip()

feed = QuakeFeed(level, period)
dataset = QuakeDataset(feed)
dataset.read_feed()

print(dataset)
print(f"Mean depth = {dataset.mean_depth():.2f} km")
print(f"Mean magnitude = {dataset.mean_magnitude():.1f}")

strongest = dataset.strongest_quake()
print()
print(
    f"Strongest quake occurred at {strongest.when:%H:%M:%S} "
    f"on {strongest.when:%Y-%m-%d}"
)
print(f"at {strongest.longitude:.1f}\u00b0 longitude, "
      f"{strongest.latitude:.1f}\u00b0 latitude")
print(f"The depth was {strongest.depth:.1f} km")
print(f"The magnitude was {strongest.magnitude:.1f}")
