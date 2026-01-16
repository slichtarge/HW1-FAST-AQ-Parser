# write tests for parsers

from seqparser import (
        FastaParser,
        FastqParser)

import pytest


def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True # things after the assert are true statements


def test_freebie_parser_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_FastaParser():
    """
    Write your unit test for your FastaParser class here. You should generate
    an instance of your FastaParser class and assert that it properly reads in
    the example Fasta File.

    Some example of "good" test cases might be handling edge cases, like Fasta
    files that are blank or corrupted in some way. Two example Fasta files are
    provided in /tests/bad.fa and /tests/empty.fa
    """
    fasta_parser = FastaParser("data/test.fa")
    with open(fasta_parser.filename, "r") as f_obj: 
        records = fasta_parser.get_record(f_obj)
        for record in records:
            seq_name, seq = record
            assert isinstance(seq_name, str)
            assert isinstance(seq, str)
            assert not seq_name.startswith(">")
            assert all(base in "ATCG" for base in seq.upper())

    bad_parser = FastaParser("tests/bad.fa")
    with open(bad_parser.filename, "r") as f_obj: 
        records_list = list(bad_parser.get_record(f_obj))
        assert len(records_list) == 0


    blank_parser = FastaParser("tests/blank.fa")
    with open(blank_parser.filename, "r") as f_obj: 
        records_list = list(blank_parser.get_record(f_obj))
        assert len(records_list) == 0



def test_FastaFormat():
    """
    Test to make sure that a fasta file is being read in if a fastq file is
    read, the first item is None
    """
    fasta_parser = FastaParser("data/test.fq")
    with open(fasta_parser.filename, "r") as f_obj: 
        records = fasta_parser.get_record(f_obj)
        for idx, record in enumerate(records):
            if idx == 0:
                assert record[0] is None


def test_FastqParser():
    """
    Write your unit test for your FastqParser class here. You should generate
    an instance of your FastqParser class and assert that it properly reads 
    in the example Fastq File.
    """
    fastq_parser = FastqParser("data/test.fq")
    with open(fastq_parser.filename, "r") as f_obj: 
        records = fastq_parser.get_record(f_obj)
        for record in records:
            seq_name, seq, line = record
            assert isinstance(seq_name, str)
            assert isinstance(seq, str)
            assert isinstance(line, str)
            assert line != "+"
            assert not seq_name.startswith(">")
            assert all(base in "ATCG" for base in seq.upper())

def test_FastqFormat():
    """
    Test to make sure fastq file is being read in. If this is a fasta file, the
    first line is None
    """
    fastq_parser = FastqParser("data/test.fa")
    with open(fastq_parser.filename, "r") as f_obj: 
        records = fastq_parser.get_record(f_obj)
        for idx, record in enumerate(records):
            if idx == 0:
                assert record[0] is None