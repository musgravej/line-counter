import os


def write_report(line_counts, longest_filename, most_lines):
    fld2w = max(len("Count"), len("{:,}".format(most_lines)))
    with open("line_count_report.txt", 'w', newline="") as r:
        r.writelines("{fld1:<{fld1w}}{fld2:>{fld2w}}\n".format(fld1="File Name", fld2="Count", 
                                                               fld1w=longest_filename + 2,
                                                               fld2w=fld2w,))
        
        r.writelines("{fld1:<{fld1w}}{fld2:>{fld2w}}\n".format(fld1="-" * longest_filename, 
                                                               fld2="-" * fld2w, 
                                                               fld1w=longest_filename,
                                                               fld2w=(fld2w + 2),))
        for file, count in line_counts.items():
            if isinstance(count, (int,)):
                print(file, "|", "{:,}".format(count))
                r.writelines("{fld1:<{fld1w}}{fld2:>{fld2w},}\n".format(fld1=file, fld2=count, 
                                                                        fld1w=longest_filename + 2,
                                                                        fld2w=fld2w,))
            else:
                print(file, "|", "{:}".format(count))
                r.writelines("{fld1:<{fld1w}}{fld2:>{fld2w}}\n".format(fld1=file, fld2=count, 
                                                                       fld1w=longest_filename + 2,
                                                                       fld2w=fld2w,))


def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


def main():
    longest_filename = 0
    most_lines = 0
    line_counts = dict()

    files = [f for f in os.listdir(os.path.curdir) 
             if f != "line_count_report.txt" and f != os.path.basename(__file__)]

    if files:
        for f in files:
            try:
                lines = file_len(f)
                most_lines = max(most_lines, lines)
            except Exception as e:
                lines = "n/a"

            line_counts[f] = lines
            longest_filename = max(longest_filename, len(f))

        write_report(line_counts, longest_filename, most_lines)


if __name__ == '__main__':
    main()
