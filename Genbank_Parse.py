#import biopython
#import pip

#Output should be each row - accession, host field, lab host field and accessions are from the working set we made while working on  complex host name sheet
# Input is accession number


#pip install biopython




#setting up bio python
from Bio import Entrez, SeqIO
import csv

def fetch_genbank_record(accession_number):
    Entrez.email = "bvbrcacapria@gmail.com"
    try:
        handle = Entrez.efetch(db="nucleotide", id=accession_number, rettype="gb", retmode="text")
        record = SeqIO.read(handle, "genbank")
        handle.close()
        return record
    except Exception as e:
        print(f"Error fetching GenBank record: {e}")
        return None



def extract_host_info(record):
    host_info = ""
    lab_host_info = ""
    for feature in record.features:
        if feature.type == "source":
            qualifiers = feature.qualifiers
            if "host" in qualifiers:
                host_info = ', '.join(qualifiers["host"])
            if "lab_host" in qualifiers:
                lab_host_info = ', '.join(qualifiers["lab_host"])
    return host_info, lab_host_info

def main():
    accession_numbers = [
     "MH177014", "MN450761"
    ]
    with open("genbank_records_HOST_and_Lab_host.csv", "w", newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        # Write header
        csv_writer.writerow(["Accession", "Host", "Lab Host"])
        for accession_number in accession_numbers:
            record = fetch_genbank_record(accession_number)
            if record:
                accession = record.id
                # Extract host and lab host information
                host_info, lab_host_info = extract_host_info(record)
                # Write data to CSV
                csv_writer.writerow([accession, host_info, lab_host_info])

if __name__ == "__main__":
    main()





