class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        characterList = list(ransomNote)
        haveLetter = True
        i = 0
				
        while haveLetter and i < len(characterList):
                haveLetter = True if magazine.count(characterList[i]) is not 0 else False
                if haveLetter:
                    magazine = magazine.replace(characterList[i], '', 1)
                i = i+1
				
        return haveLetter