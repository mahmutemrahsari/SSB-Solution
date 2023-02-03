class Solution:
    def find_anagrams(word_list):

        #Holder anagramene som skal returneres
        anagrams = []

        #Returnerer tom liste hvis ordlist har mindre enn 2 ord -> ( tom eller 1 ord )
        #O(1)
        if len(word_list) < 2: 
            return []
              
        #Sorterer per ord gjennom bokstaver e.g. "Erik" -> "eikr"
        #O(N)
        list_of_sorted_words = [''.join(sorted(word.lower())) for word in word_list] 
      
        #legg til alle ord dukket opp mer enn 1 som key(ordet) :value ([utseendeindeksene])
        dict_of_presence = {} 

        #Lager [key, value] array
        #O(N)
        for index, key in enumerate(list_of_sorted_words):
            #append legger indeks per ord inn i array
            #setdefault oppdaterer ordboket hvis nøkkelen finnes ikke i 
            dict_of_presence.setdefault(key, []).append(index)

        #O(N*N) -> O (n square)
        for index in dict_of_presence.values(): # O(N)
            if len(index) > 1: #O(1)
                #Lager en midlertidig list for per anagrammet
                tmp = list( word_list[k] for k in index ) # O(N)
                print(*tmp)
                anagrams.append(tmp)
        if(len(anagrams) > 1): #O(1)
            return anagrams
        else:
            return []

    if __name__ == '__main__':
        find_anagrams(["Erik", "Knut" , "Kire", "Irek" ,"Lars", "Lasr"])

"""
Tidkompleksiteten til koden er O(n^2), hvor n er antall ord i ordlisten.

Første if-setning har en tidkompleksitet på O(1).
list_of_sorted_words liste forståelse har en tidkompleksitet på O(n).
for-løkken for å opprette dict_of_presence ordbok har en tidkompleksitet på O(n).
Den andre for-løkken for å finne anagrammene har en tidkompleksitet 
på O(n^2), da den går gjennom verdiene i dict_of_presence ordboken 
og utfører en annen iterasjon over indeksene til hver gruppe av ord.
Plasskompleksiteten til koden er O(n), da vi må lagre list_of_sorted_words 
og dict_of_presence ordbok, som begge har en størrelse proporsjonal med antall ord i ordlisten.

"""