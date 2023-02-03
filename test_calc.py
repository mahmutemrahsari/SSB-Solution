# Mahmut Emrah Sari 
# 03/02/2023

import unittest
from Solution import Solution
from timeit import default_timer as timer
start = timer()

class TestSolution(unittest.TestCase):

    def test_empty_list(self):
        actual = Solution.find_anagrams(word_list=[])
        expected = []
        self.assertEqual(actual, expected)
    
    def test_one_word(self):
        actual = Solution.find_anagrams(word_list=["One"])
        expected = []
        self.assertEqual(actual, expected)
    
    def test_two_words(self):
        actual = Solution.find_anagrams(word_list=["One", "Two"])
        expected = []
        self.assertEqual(actual, expected)

    def test_more_than_one_word(self):
        actual = Solution.find_anagrams(word_list=["Erik", "Knut" , "Kire", "Irek" ,"Lars", "Lasr"])
        expected = [['Erik', 'Kire', 'Irek'], ['Lars', 'Lasr']]    
        self.assertEqual(actual, expected)

    #Tester hastigheten
    def test_speed(self):
        #Encoding UTF-8 gjør mulig å lese norske bokstaver korrekt 
        file_read = open('population.txt', 'r', encoding='UTF-8' )
        Solution.find_anagrams(word_list=list(set(file_read.read().split())))
        file_read.close()
        end = timer()
        sec = end - start
        if(sec < 0.09):
            print("EFFEKTIV NOK", sec)
        else:
            print("IKKE EFFEKTIV NOK", sec)
        

#Gjør kjøring av test direkte i editoren
if __name__ == '__main__':
    unittest.main()