import sys
import pyreadstat


# Convert a SAV file into a CSV file
def convert_sav_to_csv(filepath):
    df, meta = pyreadstat.read_sav(filepath)
    df.to_csv(generate_csv_filename(filepath))


# Extract the SAV file name and return it with the CSV file extension
def generate_csv_filename(filepath):
    sav_filename = filepath.split('/')[-1]
    csv_filename = sav_filename.split('.')[0] + '.csv'
    return csv_filename


if __name__ == "__main__":
	convert_sav_to_csv(sys.argv[1])
