import json

with open("raw.json", "r") as f:
    nb = json.load(f)
with open("5_1d_parallelism.ipynb", "w") as f:
    f.write(json.dumps(nb, indent=2))