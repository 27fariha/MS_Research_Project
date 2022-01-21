import csv, os
from dotenv import load_dotenv

load_dotenv()

f = open(os.getenv("CSV_PATH"))
csv_f = csv.reader(f)
for row in csv_f:
    print('{:<25} {:<40} {:<20} {:<20} {:<20} {:<10}'.format(*row))
