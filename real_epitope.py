import argparse

def parse_args():

    parser = argparse.ArgumentParser()
    parser.add_argument("--file", "-F", dest="infile", type=str, required=True,
                        help="CPL output")
    parser.add_argument("--iedbfile", "-I", dest="iedb", type=str, required=False,
                        help="IEDB file", default="epitope_table_export_1606168510.csv")


out = open("outfile.txt")

with open(args.infile) as f:
    for line1 in f:
        peptide = line1.split("\t")[2]
        with open("epitope_table_export_1606168510.csv") as f:
            for line2 in f:
                if peptide == line2.split("\t")[2]:
                    out.write(line1 + line.replace('"', "").replace.(",", "\t") + "\n")
