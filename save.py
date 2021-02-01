import csv


def save_to_file(jobs):
    # open file, if not exist, create
    #     "filenamve.csv" mode=write Only
    file = open("jobs.csv", mode="w", encoding='UTF-8')
    writer = csv.writer(file)
    writer.writerow(["title", "company", "location", "link"])
    print(jobs)
    for job in jobs:
        writer.writerow(list(job.values()))
    return
