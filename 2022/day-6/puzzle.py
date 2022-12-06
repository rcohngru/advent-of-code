from typing import List, Tuple

def main():
    """Driver code to orchestrate the puzzle solution."""

    fname = "puzzle_data.txt"

    lines = ingest_file(fname)
    start_of_packet_marker = 4

    print("-------- Part 1 --------")
    for datastream in lines:
        sequence, sequence_start, sequence_end = detect_sequence_start(datastream, start_of_packet_marker)
        print(f"Packet starts after sequence `{sequence}` is detected at the {sequence_end} place in the datastream.")

    print("-------- Part 2 --------")
    start_of_message_marker = 14
    for datastream in lines:
        sequence, sequence_start, sequence_end = detect_sequence_start(datastream, start_of_message_marker)
        print(f"Message starts after sequence `{sequence}` is detected at the {sequence_end} place in the datastream.")

def ingest_file(fname: str) -> List[str]:
    """Returns a list of the lines in a file."""

    with open(fname, "r") as f:
        lines = f.readlines()

    lines = [l.strip("\n") for l in lines]

    return lines

def detect_sequence_start(datastream: str, N: int) -> Tuple[str, int, int]:
    """
        Parses a datastream to find the unique sequence marker.

        Using the Elven protocol, a sequence marker is defined as being
        N unique characters in a sequence of the datastream that is N
        characters long. The Elves use at least 2 separate sequence markers, 
        explained below:

        Start-of-Packet: a 4 unique character long marker that occurs in a 
                sequence of 4 characters used to indicate the beginning of a packet.

        Start-of-Message: a 14 unique character long marker that occurs in a 
                sequence of 14 characters used to indicate the beginning of a packet.

        Parameters:
        datastream (str): a string of data containing various sequences used by the Elves.
        N (int): the number of charaters to look for in a sequence of the same length.

        Returns:
        sequence (str): the N character sequence that has been identified.
        scan_start (int): the start position in the datastream of the N-character long sequence.
        scan_end (int) the end position in the datastream of the N-character long sequence
    """

    for scan_start in range(0, len(datastream) - N):
        scan_end = scan_start + N
        
        sequence = datastream[scan_start: scan_end]

        if len(set(sequence)) == N:
            return sequence, scan_start + 1, scan_end

    return "", -1, -1

if __name__ == "__main__":
    main()