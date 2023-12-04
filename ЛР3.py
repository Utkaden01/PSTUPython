import random
import sys


class DNACCompressed:
    def __init__(self, dna_sequence):
        self.dna_sequence = dna_sequence
        self.compressed_sequence = self.__compress()

    def __compress(self):
        compressed = 0b00
        for nucleotide in self.dna_sequence:
            if nucleotide == 'A':
                compressed <<= 2
                compressed |= 0b00
            elif nucleotide == 'C':
                compressed <<= 2
                compressed |= 0b01
            elif nucleotide == 'G':
                compressed <<= 2
                compressed |= 0b10
            elif nucleotide == 'T':
                compressed <<= 2
                compressed |= 0b11
        return compressed

    def decompress(self):
        decompressed = ''
        compressed = self.compressed_sequence
        while compressed:
            nucleotide = compressed & 0b11
            if nucleotide == 0b00:
                decompressed += 'A'
            elif nucleotide == 0b01:
                decompressed += 'C'
            elif nucleotide == 0b10:
                decompressed += 'G'
            elif nucleotide == 0b11:
                decompressed += 'T'
            compressed >>= 2
        return decompressed[::-1]

    def __str__(self):
        return self.decompress()


dna_sequence = ''.join(random.choice(
    ['A', 'C', 'G', 'T']) for _ in range(1000))

compressor = DNACCompressed(dna_sequence)

original_size = sys.getsizeof(dna_sequence)
compressed_size = sys.getsizeof(compressor.compressed_sequence)
print(f'Оригинальный размер: {original_size} байт')
print(f'Сжатый размер: {compressed_size} байт')

decompressed_sequence = compressor.decompress()
print('Распакованная последовательность:', decompressed_sequence)
