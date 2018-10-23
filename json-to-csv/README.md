### json-to-csv

Convert `--source file` to csv.

### Run

```
▶ python json-to-csv -h
usage: json-to-csv.py [-h] [--source SOURCE]

Convert json to csv. Result csvs will be written to stdout.

optional arguments:
  -h, --help       show this help message and exit
  --source SOURCE  source folder with images
```

### Examples

```
python json-to-csv.py --source recs.json # result scsv will be store in csv_recs.json file

```
