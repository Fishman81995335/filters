import csv
#
#
with open('alerts.csv', 'r') as alerts:
    with open('filtered_alerts_ULENS_only.csv', 'w') as to_be_written:
        reader = csv.reader(alerts)
        writer = csv.writer(to_be_written, delimiter=',')
        linNum = 0
        for line in reader:
            if linNum == 0:
                writer.writerow(line)
                linNum = linNum + 1
            elif (linNum != 0):
                if ((len(line) >= 7) and (line[7] == 'ULENS'))or ((len(line) >= 9) and ("microlens" in line[9])):
                    writer.writerow(line)
                    print(line)
                else:
                    print("fail")
            else:
                linNum = linNum + 1
