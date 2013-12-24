__author__ = 'iury'
import unittest

'''

A questao :

A string is simply an ordered collection of symbols selected from some alphabet and formed into a word; the length of a string is the number of symbols that it contains.

An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."

Given: A DNA string s of length at most 1000 nt.

Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.

'''

''' A funcao percorrre uma string e para cada letra na string se essa letra pertence aos simbolos
 ele eh adicionado em uma estrutura de dicionario'''


def countingDNA(dnaString):
    counts = {"A": 0, "C": 0, "G": 0, "T": 0}

    for symbol in dnaString:
        if symbol in counts.keys():
            counts[symbol] += 1

    return counts["A"], counts["C"], counts["G"], counts["T"]


class Test(unittest.TestCase):
    def test_count1(self):
        self.assertEqual((20, 12, 17, 21),
                         countingDNA("AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"))

    def test_count2(self):
        self.assertEqual((10, 5, 5, 5), countingDNA("AAAAAAAAAAGGGGGTTTTTCCCCC"))

    def test_count3(self):
        self.assertEqual((238, 237, 222, 229), countingDNA(
            "CTTTTTCGGTACATTCCTGTATGTCGTTGGTCCTAGTCAAAGATGACCGGTATTCAATGGTTGAATATATTCTCGTACCCCATGGTTGCCCCGGTCCGGCCGGATACTTGAAGGTAGTTTACCCGCCTAAACTATACCTCTAAGTCGGTTACGATGCACAAGTAGGTACGAGCTCTACTGGGTAGGCAGCTAGACCCGCAGATAGCATGGGAGATTAGCCACCATTTGAGACGTACGGCTTCTTGTACTAACTGGGACCGTTTCTCTAAACTGCCCCATCCCATCCCGACGTTCCCGGGGTCATAACGTAGAATTAGAAAATTAGTTTCATGGCGCGCCGTCACGAAGTGAGGAGACAAGTAACGCCCTGTTACTATGTTTACGTACATATCGCACTCTGTAACTCTCATACGATCTTCCGCCATCAGAACCCTAAGATAAAACGGATACGTGAACTCAGCTTCGGGCAATTAAAGTTGTGGGCCAATGTCGCCTGCTCTGGGACTTACATCTCAAAGTAATGCTACTTCCACCGATCGGGCAAGTCAATACCGGCATCAAACCGAGGCATGCTCCGTTGCGAAATGCGGACAGGCGGCTTAGCCAAATAGACCAACCAGGGCCTATATCAAGTGATCAGCAGGTACTGACTTTCCCACGACCCTGGGCCGAGCGAGAGCACTAATGCCAGTCCCCGCTTACTGGATAGAGATATGGATGGCCAGACGAACTAATTAAGGTCTATACACGGCGCCACATCTGATACTGTTAAGGTTGAACAACATGACTCTCGCATAGACATACTAGTGTACGATACGGGCTATTAATTTTCATCTGCTGAGGTCATGTAGCCGGGGCCCATTCCCTTACGGCGCTGTTTTTTGCGGAGTCTGAGTATGCGAGCATGCAAGGGCAAAGCCAGTCAG"))


if __name__ == '__main__':
    unittest.main()

