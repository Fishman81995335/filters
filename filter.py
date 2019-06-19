import csv
#
#
with open('alerts.csv','r') as alerts:
    with open('filtered_alerts_no_keys.csv', 'w') as to_be_written:
        reader = csv.reader(alerts)
        writer = csv.writer(to_be_written, delimiter=',')
        linNum = 0
        for line in reader:
            if linNum == 0:
                writer.writerow(line)
                linNum = linNum + 1
            elif (linNum != 0) and (len(line) > 1) and (line[5] != '' and line[4] != '') and (line[7] != 'AGN')\
                    and (line[7] != "QSO") and ("SN" not in line[7]) and ('slow' not in line[9]) \
                    and ("flare" not in line[9]):
                dif = float(line[5]) - float(line[4])
                if (dif >= .6) and (dif <= .9):
                    writer.writerow(line)
                    print(line)
                else:
                    print("fail")
            else:
                linNum = linNum + 1
