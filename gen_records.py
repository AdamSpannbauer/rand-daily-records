import csv
import datetime
import logging
import os
import random

logging.basicConfig(level=logging.INFO)

try:
    filepath = os.environ["DATAFILE"]
    logging.warning(f"Records will be generated in {filepath} (from DATAFILE var)")
except KeyError:
    filepath = "yesterdays-records.txt"
    logging.warning(f"DATAFILE env var not found; defaulting to {filepath}")

rng = random.SystemRandom()
n_records = rng.randrange(32, 257)

today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)

regions = ["A", "B", "C", "D", "E"]

logging.info(f"Generating {n_records} for 'salesdate': {yesterday}")
with open(filepath, "w", newline="") as f:
    writer = csv.writer(f)
    for _ in range(n_records):
        productid = rng.randrange(100, 600, 5)
        region = rng.choice(regions)
        freeship = rng.choice([0, 1])
        discount = round(rng.uniform(0.01, 10), 2)
        itemssold = rng.randrange(1, 257)

        writer.writerow([yesterday, productid, region, freeship, discount, itemssold])

with open(filepath, "r") as f:
    n_written_lines = len(f.readlines())

if n_written_lines != n_records:
    logging.warning(
        f"n_records ({n_records}) differs from resulting file size ({n_written_lines})"
    )
else:
    logging.info(f"Successfully generated and wrote {n_records} records")
