import sys
import csv


def arg():
    if len(sys.argv) < 3:
        return f"No arg"
    elif len(sys.argv) > 3:
        return f"Too many arg"
    else:
        return csvSort(sys.argv[1], sys.argv[2])


def csvSort(before, after):
    try:
        with open(before) as beforeFile:
            split = []
            reader = csv.DictReader(beforeFile)
            for row in reader:
                split.append({"name": row["name"], "house": row["house"]})

        with open(after, "a") as afterFile:
            writer = csv.DictWriter(afterFile, fieldnames=["first", "last", "house"])
            writer.writeheader()
            for name in split:
                last, first = name["name"].split(",")
                writer.writerow(
                    {"first": first.lstrip(), "last": last, "house": name["house"]}
                )

    except:
        return f"file doesnt exist"


arg()
