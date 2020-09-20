import csv
def log(username, filename, link, time):
    print("Logging: ", username, filename, time)
    with open("userlist.csv", 'a+', newline='',) as f:
        writeclass = csv.writer(f, delimiter=',')
        writeclass.writerow([time, username, filename, link])
