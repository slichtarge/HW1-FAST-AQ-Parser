from seqparser import (
        FastaParser,
        FastqParser,
        transcribe,
        reverse_transcribe)

import pytest


def main():
    """
    The main function
    """
    # Create instance of FastaParser
    fasta_parser = FastaParser("data/test.fa")

    # Create instance of FastqParser
    fastq_parser = FastqParser("data/test.fq")
        
    # For each record of FastaParser, Transcribe the sequence
    print("transcribing fasta")
    with open(fasta_parser.filename, "r") as f_obj: 
        records = fasta_parser.get_record(f_obj)
        for record in records:
            seq_name, seq = record
            transcribed = transcribe(seq)
            print("\n")
            print(seq_name, transcribed)    # and print it to console
       
    # For each record of FastqParser, Transcribe the sequence
    print("\ntranscribing fastq")
    with open(fastq_parser.filename, "r") as f_obj: 
        records = fastq_parser.get_record(f_obj)
        for record in records:
            seq_name, seq, __line = record
            transcribed = transcribe(seq)
            print("\n")
            print(seq_name, transcribed)    # and print it to console


    # For each record of FastaParser, Reverse Transcribe the sequence
    print("\nrev-transcribing fasta")
    with open(fasta_parser.filename, "r") as f_obj: 
        records = fasta_parser.get_record(f_obj)
        for record in records:
            seq_name, seq = record
            rev_transcribed = reverse_transcribe(seq)
            print("\n")
            print(seq_name, rev_transcribed)    # and print it to console
       
    # For each record of FastqParser, Reverse Transcribe the sequence
    # and print it to console
    print("\nrev-transcribing fasta")
    with open(fastq_parser.filename, "r") as f_obj: 
        records = fastq_parser.get_record(f_obj)
        for record in records:
            seq_name, seq, __line = record
            rev_transcribed = reverse_transcribe(seq)
            # and print it to console
            print("\n")
            print(seq_name, rev_transcribed)

        
"""
When executing a python script from the command line there will
always be a hidden variable `__name__` set to the value `__main__`.

Since this is guaranteed you can execute your `main` function with
the following if statement
"""
if __name__ == "__main__":
    main()