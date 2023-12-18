
#fetch a genbank file and sequence from there

#import Bio
from Bio import Entrez, SeqIO
def fetch_genbank_file(accession):
    # Provide your email address for identification
    Entrez.email = "rbhattac@jcvi.org"

    # Fetch the GenBank record using the accession number
    handle = Entrez.efetch(db="nucleotide", id=accession, rettype="gb", retmode="text")

    # Parse the GenBank record
    record = SeqIO.read(handle, "genbank")

    # Close the handle
    handle.close()

    return record

def main():
# Example: Replace 'your_accession_number' with the actual accession number you want to fetch
    accession_number = 'JF714155'
    genbank_record = fetch_genbank_file(accession_number)
    print(len(genbank_record.seq))
    print(genbank_record.seq)

if __name__ == "__main__":
    main()

# Save the GenBank record to a file
#output_filename = f"{accession_number}.gb"
#with open(output_filename, "w") as output_file:
    #SeqIO.write(genbank_record, output_file, "genbank")

#print(f"GenBank record saved to {output_filename}")