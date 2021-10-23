
class Solution:
    def Longest_Substring_Without_Repeating_Characters(self,stringg: str) -> dict:
        how_long=0
        array_of_substring=[]
        dict={}
        for index,character in enumerate(stringg):
            if character not in array_of_substring:
                array_of_substring.append(character)
            else:
                dict[''.join(array_of_substring)]=len(array_of_substring)
                index_in_aray_of_character=array_of_substring.index(character)
                if index_in_aray_of_character!=0:
                    array_of_substring = array_of_substring[index_in_aray_of_character+1:]
                    array_of_substring.append(character)
                else:
                    array_of_substring = array_of_substring[1:]
                    array_of_substring.append(character)

        dict[''.join(array_of_substring)] = len(array_of_substring)


        return dict
if __name__ == '__main__':
    s=Solution()
    print(max(s.Longest_Substring_Without_Repeating_Characters("abcabcbb").values()))
    # print(Solution.Longest_Substring_Without_Repeating_Characters("abcabcbb"))
