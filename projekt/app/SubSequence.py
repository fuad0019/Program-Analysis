def is_subsequence(subsequence, sequence):
    """
    Check if subsequence is present in the sequence.
    """
    #print(f"\n THIS IS SUBSEQUENCE {subsequence} ")
    #print(f"\n THIS IS SEQUENCE {sequence} ")

    sub_len = len(subsequence)
    seq_len = len(sequence)

    # If subsequence is longer than sequence, it can't be a subsequence
    if sub_len > seq_len:
        return False

    # Iterate through the sequence to find the subsequence
    for i in range(seq_len - sub_len + 1):
        if sequence[i:i + sub_len] == subsequence:
            return True

    # If no match is found
    return False

# Example usage:
