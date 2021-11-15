# 3
# Your care set up, do not pluck my care down.
# My care is loss of care with old care done.
# Your care is gain of care when new care is won.
# 1
# care
from collections import Counter
import string
class Solution(object):
    def get_data(self,lines_number:int):
        all_text=[]
        while lines_number-1>=0:
            text = input().strip()
            all_text.append(text)
            lines_number-=1
        return all_text
    def get_words(self, word_number: int):
        word_to_check=[]
        while word_number-1>=0:
            word = input().strip()
            word_to_check.append(word)
            word_number-=1
        return word_to_check
    
    def Indexing_search(self,all_text,word_to_check):
        dictt= dict()
    
        all_text=enumerate(all_text)
        for nb,line in all_text:

            for i in string.punctuation:
                line = line.replace(i, " ")
            line = line.lower()
            line=line.split()

            for word,quantity in Counter(line).items():
                if word not in dictt:
                    dictt[word]=dict()
                if nb not in dictt[word]:
                     dictt[word][nb]=0
                dictt[word][nb] = quantity
    
        for looking_word in word_to_check:
            returned_order_lines = []
            try:
                for linee,wystapienia in sorted(dictt[looking_word].items(), reverse=True, key= lambda x:x[1]):
                    returned_order_lines.append(linee)
                print(returned_order_lines)
            except KeyError:
                print([])
if __name__=='__main__':
    s=Solution()
    lines_number = int(input().strip())
    all_text=s.get_data(lines_number)
    word_number = int(input().strip())
    word_number=s.get_words(word_number)
    s.Indexing_search(all_text,word_number)
