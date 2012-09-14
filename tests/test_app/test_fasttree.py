#!/usr/bin/env python
"""Tests for FastTree v1.1 application controller.  
Also functions on v2.0.1, v2.1.0 and v2.1.3"""

from shutil import rmtree
from os import getcwd
from cogent.util.unit_test import TestCase, main
from cogent.app.fasttree import FastTree, build_tree_from_alignment
from cogent.core.alignment import Alignment
from cogent.parse.fasta import MinimalFastaParser
from cogent.parse.tree import DndParser
from cogent.core.moltype import DNA

__author__ = "Daniel McDonald"
__copyright__ = "Copyright 2007-2012, The Cogent Project"
__credits__ = ["Daniel McDonald", "Justin Kuczynski"]
__license__ = "GPL"
__version__ = "1.5.3-dev"
__maintainer__ = "Daniel McDonald"
__email__ = "mcdonadt@colorado.edu"
__status__ = "Development"

class FastTreeTests(TestCase):
    def setUp(self):
        self.seqs = Alignment(dict(MinimalFastaParser(test_seqs.split())))
    
    def test_base_command(self):
        app = FastTree()
        self.assertEqual(app.BaseCommand, \
                         ''.join(['cd "',getcwd(),'/"; ','FastTree']))
        app.Parameters['-nt'].on()
        self.assertEqual(app.BaseCommand, \
                         ''.join(['cd "',getcwd(),'/"; ','FastTree -nt']))

    def test_change_working_dir(self):
        app = FastTree(WorkingDir='/tmp/FastTreeTest')
        self.assertEqual(app.BaseCommand, \
                       ''.join(['cd "','/tmp/FastTreeTest','/"; ','FastTree']))
        rmtree('/tmp/FastTreeTest')

    def test_build_tree_from_alignment(self):
        tree = build_tree_from_alignment(self.seqs, DNA)
        # test expected output for fasttree 1.1 and 2.0.1
        try:
            for o,e in zip(tree.traverse(), DndParser(exp_tree).traverse()):
                self.assertEqual(o.Name,e.Name)
                self.assertFloatEqual(o.Length,e.Length)
        except AssertionError:
            for o,e in zip(tree.traverse(), DndParser(exp_tree_201).traverse()):
                self.assertEqual(o.Name,e.Name)
                self.assertFloatEqual(o.Length,e.Length)
test_seqs = """>test_set1_0
GGTAGATGGGACTACCTCATGACATGAAACTGCAGTCTGTTCTTTTATAGAAGCTTCATACTTGGAGATGTATACTATTA
CTTAGGACTATGGAGGTATA
>test_set1_1
GGTTGATGGGACTACGTAGTGACATGAAATTGCAGTCTGTGCTTTTATAGAAGTTTGATACTTGGAGCTCTCTACTATTA
CTTAGGACTATGGAGGTATA
>test_set1_2
GGTTGATGGGCCTACCTCATGACAATAAACTGAAGTCTGTGCTTTTATAGAGGCTTGATACTTGGAGCTCTATACTATTA
CTTAGGATTATGGAGGTCTA
>test_set1_3
GGTTGATGGGACTACCTCATGACATGAAACTGCAGTCTGTGCTTTTATAGAAGCTTGATACTTGGAGATCTATACTATTA
CTTAGGACTATGGAGGTCAC
>test_set1_4
GGTTGGTGGGACTACCTCATGACATGAAGATGCAGTCTGTGCTTGTATAGAAGCTTGAAACTTGGATATCTATACTATTA
CTTAAGACTATGGAGGTCTA
>test_set1_5
GGTTGATGCGACTACCTCATGACATGAGACTGCAGTCTGTGCTTTTACTGAAGCTTGATACTTGGAGATCTATACTATTA
CTTAGGACTATGGAGGTTTA
>test_set1_6
GGTTGATGGGACTACCTCATGACATGAAAATGCAGTCTGTCCTTTTATAGAAGCTTGATACTTGTAGATCTATACTGTTA
CTTAGGACTATGGAGGTCTA
>test_set1_7
GGTTGATGGGACTCCCTCATGACATAAAACTGCAGTCTGTGCTTTTACAGAAGCTTGATACTTGGAGATCTATACTATTA
CATAGGACTATGGAGGTCTA
>test_set1_8
GGTTGATGGCACTACCTCATGAGATGAAACTGCAGTCTGTGCTTTTATAGAAGCTTGATACTTGGATATCTATACTATAA
CTTAGTACTATGGAGGCCTA
>test_set1_9
GGTTTATGTTACTACCTCATGACATGAAACGGCAGCATGTGCTTTTATAGAAGCTTGATACTTGGAGATCTAAACTATTA
CTTAGGACTATGGAGGTCTA
>test_set2_0
AGCGAATCATACTCTGGAAAGAAAAGGACGACTCCTTTGCTCGCGGTCTAGCTGCTACAGCTTCACCGAGTACATCTGAA
TGATGGTTGAACCGGGTTCA
>test_set2_1
AGAGAATAGTACTCTGGAAAGACAAGGACGACTCCTTTGATCGCGGTCTAGCTGCTACAGCTTCACCGAGTACATCTGAA
TGATGGTTGAACCGGATTCA
>test_set2_2
AGAGTATAATACTCTGGAAAGAAAAGGACGACTCCTTTGATCGCGGTCTAGCTGCTACAGCTTCACCGAGTACATCTTAA
TGATGGTTGAACCGGGGTCA
>test_set2_3
AGAGAATCATACTCTGGAAAGAAATGGACGACTCCTTTGATCGCGGTCCAGCTGCTACAGCTTCACCGAGTACATCTGAA
TGATGGTTGGACCGGGTTCA
>test_set2_4
AGAGAATAATAGTCTGGAAAGAAAAGGACGACTCCTTTGTTCCCGGTCTAGCTGCTACAGCTTCCCCGAGTACATCTGAA
TGATGGTTGAACCGGGTTCA
>test_set2_5
ACAGAATACTACTCTGGAAAGAAAAGGCCGACTCCTTTGATCGCTGTCTAGCTGCGACAGCTGCACGGAGTCCATCCGAA
TGATGGTTGAACCGGGTTCA
>test_set2_6
AGAGAATAATACTCTGGACAGAAATGGACGACTCCTTTGATCGCGGTCTAGCTGCTACAGCTTCACCGAGTACATCTGAA
TGATGGCTGAACCGGGTTCA
>test_set2_7
AGAGAATATTACTCTGGAAAGAAAAGGACGACTCCTTGGATCGCGGTCTAGCTGCTACAGCTTCAGCGAGTACATCGGAA
TGATGGTTTAACCGGGTTCA
>test_set2_8
AGTGAATAATACTCTGGAAAGAAAAGGACGACTCCTTTGATCGCGGTCTAGCTGCTAGAGCTTCACCGAGTACATCTGAA
TGATGGTTGAACCGGGTTCA
>test_set2_9
AGAGATTAATACTCTGGATAGAAAATGACGACTCCTTTGATCGCGGTCTAGCTGCTACAGATTGACCTATTACATCTGAA
TGATGGTTGAACCGGGTTCA
>test_set3_0
TTGTCTCCATTGAGCACTCTAATCTTGCCGTGTATTCAGGAAAGGAGGATAGAACTCGGACAGTATTCTGAACATTACAG
AATCGCCGTATTTACGGTGT
>test_set3_1
TTGTCTCCATTGAGCACTCTAATCATGCCGTGTATTCAGGAACGGAGGAGAGGACTCGGTCAGTATTCGGAACATTACAG
AATGGCGTTATTTACGGTGT
>test_set3_2
TTGTCTCCATTGAGCACTCTAATCTTGCCGTGTATTCAGGAACGGAGGATAGAACTCGGACAGAATCCTGAATATTACAA
AATCGGGTTATTTACGGTGT
>test_set3_3
TTGTCTCCATTGAGCACTCTAATCTTGCCGTGTTTTCAGGAACGGAGGATAGAACTCGGACAGTAGCCTGAACATTACAG
AATCCCGTTATTTACGGTGT
>test_set3_4
TTGTCTCCATCGAGCACTCTAATCTTGCCGTGTATTCAGGAACGGAGGATTGAACTCGGACAGTATCCTGAACATTACAG
AATCGCGTTATTTACGGTGT
>test_set3_5
TTGTCTCCATTGAGCACGCTAAGCTTGCCGTGTATTCAGGAACGGAGGATAGAACTCGGACAGTATCCTGAACATTACAG
AATCGCGTTATTTACGGTGT
>test_set3_6
TTGTCGTCATTGAGCACTCTAATCTTGCCGTGTATTCAGGAACGAAGGATAGAACTCGGACAGTATCCTGAACTTTGCAA
AATCGCGTTATTTACGGTGT
>test_set3_7
TTGTCTCCATTGAGCACTCTAATCTAGCCGTGTAGTCAGGAACGGAGGATGGAACGCGCACAGTATCCTGAACATAACAG
AATCGCGTTATTTACGGTGT
>test_set3_8
TTGTCTCCATTGAGCACTCTAATCTTGCCGTATATTCCCGAACGGAGGATAGAACTCGGACAGTAGCCTGAACAGTACAG
AATCGCGTTATTTACGGTGT
>test_set3_9
TTGTCTCCCTTGAGCACTCTAATCTTGCCGTGTATTCAGGAACGGAGGATAGAACTCGGACAGTATCCTGAACATTACAG
AATCGCGTTATTTACGGTGT
>test_set4_0
CTTTTACCGGGCTGCCCGAGAGCACTATCTGCGTCGTGCCCTGCTTCGATGCCCACACTACCATCATACTATTCGTGAAT
TTGCGGCCGCTAAGATCCGA
>test_set4_1
CTTTTATCGGGGTGCCTGATAGCACCATCTGCGTCGTGCCCTGCTTCGATGCCTAAACCACCGTCATGCTATTTGTGAAT
TTGAGGTCGCTAAGAGCCCA
>test_set4_2
CTTTTATCGGGGTGCCCGAGAGCACCATCTGCGTCGTGCCCTGCTTCGATGCCCAGGCCACCATCATACTATTTGTGGCT
TAGGGGTCGCTAAGAGCCGA
>test_set4_3
CTTTTATCGGGGGGCCCGAGAGCACCACCTGCGTCGTGCCCTGCTTCGATGCCCAAACCACCATCATACTATTTGTGAAT
TTGGGGTCGCTAAGAGCCGA
>test_set4_4
CTTTTATAGGGGTGCCCGAGAGCACCATCTGCGTCGTGCCCAGCTTCGATTTCCAAACCACCATCATACTATTTGTGAAC
TTGGGGACGTTAAGAGCCGA
>test_set4_5
CTTTTCGCGGGGTGCCCGAGAGCACCATCTGCGTCGCGCCCTGCTTCGGTGCCCATACCACCATCATAATATTTGGGAAA
TTGGGATCGCTAAGAGTCGA
>test_set4_6
CTTTTCTCGGGGTGCCCGAGAGCCCCATCTGCGTTGTGCCCTGCTACTATGCCCAAACCACCATCATACTATTTGTGAAT
GTGGCGTCGCTCAGAGCCGA
>test_set4_7
CTTTTATCGGGGTGCCCGAGAGCACCATCTGCGTCGTGCCCTGCTTCGATGCCCACGTCACCATACTACTATTTGTGAAT
TTGGGGTCGCTAATAGCCGA
>test_set4_8
CTTTTATCGGGGGGCCCGAGAGCATCATCTGCGTCGTGCCCTGCTTCGATGCCCAAACTACCATCATACTATTTGTGAAT
TTGGGGTTTCTAAGAGCCGA
>test_set4_9
CTTTTACCGGGGTGACCGAGAGCACCATCTGCGCCGTGCCCTGCTTCGAGGCCCAAACCACCATCATACTGTTTGTGAAT
CAGGGGTTGCTAAGAGCCGA"""

exp_tree = """((test_set2_0:0.02121,(test_set2_8:-0.03148,(((test_set3_6:0.05123,(test_set3_5:0.01878,((test_set3_0:0.03155,test_set3_1:0.06432)0.664:0.01096,(((test_set3_3:0.02014,test_set3_8:0.04240)0.880:0.01129,(test_set3_7:0.05900,test_set3_4:0.01449)0.756:0.00571)0.514:0.00038,test_set3_9:0.00907)0.515:0.00020)0.834:0.00164)0.708:0.01349)0.754:0.19207,test_set3_2:-0.16026)0.999:1.34181,(test_set1_2:0.00324,((test_set1_0:0.04356,test_set1_1:0.07539)0.393:0.00223,((test_set1_3:0.01998,(test_set1_9:0.07362,((test_set1_4:0.06701,test_set1_8:0.05195)0.397:0.00350,(((test_set4_4:0.06931,(((test_set4_2:0.03637,test_set4_7:0.04823)0.726:0.01237,((test_set4_5:0.09845,test_set4_6:0.08151)0.593:0.00959,((test_set4_3:0.01520,test_set4_8:0.03654)0.590:0.00869,test_set4_9:0.07865)0.499:0.00229)0.479:0.00187)0.430:0.00179,test_set4_0:0.08643)0.651:0.00975)0.478:0.04249,test_set4_1:0.03754)1.000:1.66272,test_set1_6:-0.12006)0.803:0.15777)0.490:0.00569)0.562:0.00182)0.879:0.00579,(test_set1_7:0.03234,test_set1_5:0.04114)0.520:0.00487)0.567:0.00688)0.651:0.06887)0.923:0.48284)0.994:1.24321)0.517:0.05040)0.522:0.00306,test_set2_4:0.03835,((test_set2_9:0.07472,(test_set2_3:0.03380,test_set2_6:0.01794)0.540:0.00679)0.583:0.00234,(test_set2_2:0.03055,((test_set2_5:0.08864,test_set2_7:0.04212)0.724:0.00563,test_set2_1:0.02522)0.905:0.00645)0.566:0.00081)0.642:0.00394);"""
# for FastTree version 2.0.1
exp_tree_201 = """(((test_set2_8:0.00039,(((test_set3_6:0.05278,(test_set3_5:0.02030,(((test_set3_0:0.03166,test_set3_1:0.06412)0.783:0.00945,(test_set3_7:0.06330,test_set3_4:0.02026)0.896:0.00014)0.911:0.00014,((test_set3_3:0.02053,test_set3_8:0.04149)0.790:0.00995,test_set3_9:0.01011)0.927:0.00015)0.922:0.00015)0.780:0.00976)0.763:0.03112,test_set3_2:0.00014)0.881:1.40572,(((((test_set1_9:0.07378,(test_set1_7:0.03123,test_set1_5:0.04198)0.756:0.00995)0.883:0.00016,(test_set1_3:0.02027,((test_set1_0:0.04231,test_set1_1:0.07523)0.377:0.00928,test_set1_2:0.07433)0.868:0.00016)0.131:0.00015)0.872:0.00016,test_set1_8:0.06287)0.438:0.00975,(test_set1_6:0.00014,((((test_set4_4:0.07405,(test_set4_6:0.07814,test_set4_5:0.10163)0.688:0.00645)1.000:0.00015,((test_set4_2:0.03960,test_set4_7:0.05092)0.776:0.01382,(test_set4_9:0.07780,test_set4_0:0.08964)0.197:0.00703)0.862:0.00014)0.798:0.00014,(test_set4_3:0.01000,test_set4_8:0.04167)0.782:0.01024)1.000:0.07368,test_set4_1:0.00014)1.000:1.73333)0.598:0.03127)0.122:0.00091,test_set1_4:0.06300)0.634:0.46513)0.918:1.50492)0.600:0.01987,test_set2_0:0.03067)0.466:0.00015,test_set2_4:0.04129,((test_set2_2:0.03073,(test_set2_1:0.03068,(test_set2_5:0.09729,test_set2_7:0.05209)0.421:0.00015)0.851:0.00015)0.771:0.00015,(test_set2_9:0.07415,(test_set2_3:0.03110,test_set2_6:0.02061)0.776:0.00997)0.985:0.00016)0.879:0.00015);"""

if __name__ == '__main__':
    main()
