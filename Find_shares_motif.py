from Bio import SeqIO
#find the longest common substring of all sequences

sequence_dict={} #erstelle leeren dict
handle = open('sequence.txt','r') #öffne txt file zum lesen
for record in SeqIO.parse(handle,'fasta'): #für jede sequenz in dem dict
    sequence_dict[record.id] = str(record.seq)
handle.close()


# first sort sequences by length then find the shortest
def find_lcm(directory_of_sequences):
    sorted_seqs = sorted(directory_of_sequences, key=len)
    shortest_seq = sorted_seqs[0]
    other_seq = sorted_seqs[1:]

    def check_if_match(substring):
        for seq in other_seq:
            if substring not in seq:
                return False
        return True

    motif = ""
    shortest_seq_len = len(shortest_seq)

    for i in range(shortest_seq_len):
        for j in range(i+1, shortest_seq_len + 1):
            candidate_motif = shortest_seq[i:j]
            if len(candidate_motif) > len(motif) and check_if_match(candidate_motif):
                motif=candidate_motif

    return motif

sequences = list(sequence_dict.values())

longest_motif=find_lcm(sequences)
print (longest_motif)