"""Copies the records of KSP Diag - Scatter a run kept out of KSP.log, one file per loading.

    python extract-scatter-records.py --log KSP.log --lines out/lines.json --out <folder> --name kerbin-fix

For each line of lines.json (written by run-scatter-loading.py or run-scatter-driving.py), it writes
<name>-load<n>.log, or <name>-load<n>-<tag>.log when the line has a tag: the record whose number lines.json
gives, as KSP.log holds it, without the time stamp KSP puts before its first line.
"""
import argparse
import json
import os
import re

# The time stamp KSP puts before an entry of its log.
STAMP = re.compile(r"^\[(LOG|WRN|ERR|EXC)\s+[\d:.]+\]\s")


def records(path):
    """The records of the rocks in a KSP.log, by number: each a list of lines."""
    found = {}
    current = None
    number = None
    with open(path, encoding="utf-8", errors="replace") as f:
        for raw in f:
            line = STAMP.sub("", raw.rstrip("\r\n"))
            start = re.match(r"\[KSPDiagScatter\] Record (\d+) on ", line)
            if start:
                number = int(start.group(1))
                current = [line]
                continue
            if current is None:
                continue
            current.append(line)
            if re.match(r"\[KSPDiagScatter\] End of record %d:" % number, line):
                found[number] = current
                current = None
    return found


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--log", required=True, help="the KSP.log of the run")
    parser.add_argument("--lines", required=True, help="the lines.json of the run")
    parser.add_argument("--out", required=True, help="the folder the files go to")
    parser.add_argument("--name", required=True, help="the start of each file's name, such as kerbin-fix")
    options = parser.parse_args()
    found = records(options.log)
    with open(options.lines, encoding="utf-8") as f:
        rows = json.load(f)
    os.makedirs(options.out, exist_ok=True)
    for row in rows:
        if row["record"] not in found:
            raise SystemExit("no record %s in %s" % (row["record"], options.log))
        tag = "-" + row["tag"] if row.get("tag") else ""
        path = os.path.join(options.out, "%s-load%d%s.log" % (options.name, row["load"], tag))
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write("\n".join(found[row["record"]]) + "\n")
        print(path)


if __name__ == "__main__":
    main()
