from dateutil.parser import parse
import read

df = read.load_data()

def find_hour(row):
    return parse(row).hour

df["sub_hour"] = df["submission_time"].apply(find_hour)

sub_hour_count = df["sub_hour"].value_counts()

print(sub_hour_count)