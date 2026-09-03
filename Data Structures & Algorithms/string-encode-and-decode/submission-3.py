class Solution:

    def encode(self, strs: List[str]) -> str:
        """
        Loop through each word
        and count their characters
        (we probably dont want to create a new string every character maybe./.)
        String = delimiter + word
        repeat
        """
        # strings, work around using list and then joining them.
        res = ""
        temp = []
        for word in strs:
            count = len(word)
            newWord = f"{count}#{word}"
            temp.append(newWord)
        return res if not temp else "".join(temp)

    def decode(self, s: str) -> List[str]:
        """
        loop characters,
        count until delimiter #
        grab count of letters ==> words
        add to our list
        """
        res = []
        l = 0
        r = 1
        delimiter = '#'
        while r < len(s):
            if s[r] == delimiter:
                count = int(s[l:r])
                res.append(s[r+1:r+count+1])
                l = r+count+1
                r += count+1
            r += 1
        return res

