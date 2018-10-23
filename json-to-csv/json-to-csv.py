import argparse
import json
import codecs
import io
import csv

def parse_args():
    parser = argparse.ArgumentParser(description='Convert json to csv. Result csvs will be written to stdout.')
    parser.add_argument('--source', dest='source', help='source folder with images')
    args = parser.parse_args()
    return args

def main():
    args = parse_args()
    source = args.source
    with io.open(source, 'r', encoding='utf-8') as f:
        source_data = f.read()
        print(source_data)
        # json_dump = json.dumps(source_data).decode('unicode-escape').encode('utf8')
        json_rating = json.loads(source_data)

    f2 = codecs.open('csv_'+source, 'w+', encoding='utf-8')
    keys = json_rating[0].keys()
    csv_file = csv.DictWriter(f2, keys)
    csv_file.writeheader()

    for item in json_rating:
        csv_file.writerow(item.values())

    f2.close()

def to_utf8(lst):
    return [unicode(elem).encode('utf-8') for elem in lst]

if __name__ == '__main__':
    main()
