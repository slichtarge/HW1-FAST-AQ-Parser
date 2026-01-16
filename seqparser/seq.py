# DNA -> RNA Transcription
from typing import Union

TRANSCRIPTION_MAPPING = {"A": "U", "C": "G", "T": "A", "G": "C"}
ALLOWED_NUC = TRANSCRIPTION_MAPPING.keys()


def transcribe(seq: str, reverse: bool = False) -> str:
    """
    Write a function that will transcribe (replace DNA sequence to RNA
    by replacing all 'T' to 'U') in an input sequence
    """
    transcription = []
    if seq == "":
        raise ValueError(f"Empty string found: {len(seq)}")
    for nuc in seq:
        if nuc not in ALLOWED_NUC:
            raise ValueError(f"Invalid nucleotide found: {nuc}")
        else:
            transcription.append(TRANSCRIPTION_MAPPING[nuc])
    final_transcription = "".join(transcription)
    return final_transcription

def reverse_transcribe(seq: str) -> str:
    """
    Write a function that will transcribe an input sequence and reverse
    the sequence
    """
    trxn = transcribe(seq)
    rev_trxn = trxn[::-1]
    return rev_trxn