import os
import sys
import django


sys.path.append("..")
sys.path.append(".")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
django.setup()


import csv
from series.models.series import Serie
from series.models.genres import Genre


def main():
    file_path = os.path.join('fixtures', 'series-old.csv')
    print(file_path)

    if os.path.exists(file_path):
        index = 0
        with open(file_path, mode='r', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file, delimiter=';')
            for row in reader:
                if index == 0:
                    index += 1
                    continue

                Serie.objects.create(
                    name=row[1],
                    description="",
                    chapters=row[4],
                    status="F",
                    type="TV"
                )
                index += 1



if __name__ == '__main__':
    main()
