import csv
print '['
count = 0
with open('state_table.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in spamreader:
        if count > 0:
            print """
{
  "model": "company_directory.state",
  "pk" : %s,
  "fields": {
    "code": "%s",
    "name": "%s"
  }
},"""[1:] % (count, row[2], row[1])
        count = count + 1
print ']'
