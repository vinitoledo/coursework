class Solution:

    def encode(self, strs: List[str]) -> str:

        # if strs == [""]:
        #     return "empty"

        message = ''
        for word in strs:
            message = message + str(len(word)) + "&" + word
        return message

    def decode(self, s: str) -> List[str]:

        if s == "empty":
            return []
        
        lista = []

        word_size = ""
        head = 0

        while head < len(s):
            for word_end in range(head,len(s)):
                if s[word_end] == "&":
                    word_size = s[head:word_end]
                    break
            
            # print(head, word_end, word_size)
            size_num = len(word_size)

            head += size_num + 1
            next_word = s[head : head + int(word_size)]


            lista.append(next_word)
            head = head + len(next_word)

        return lista


