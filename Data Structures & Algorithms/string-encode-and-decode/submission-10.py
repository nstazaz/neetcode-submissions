class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string=list()
        #print(strs)
        for x in strs:
            chrin=[]
            for y in x:
                y1=str(ord(y))
                chrin.append(y1)
            chrinde=str('/'.join(chrin))
            encoded_string.append(chrinde)
        if strs == []:
            encoded_string="#"
            return encoded_string
        encoded_string=','.join(encoded_string)      
        print(encoded_string)
        print("done 0",encoded_string)
        return encoded_string         

    def decode(self, s: str) -> List[str]:
        #print("done 1.0",s)
        encoded_word=s.split(",")
        print(encoded_word)
        decoded_strs=list()
        if s=="32":
            print("fff")
            return decoded_strs
        for x in encoded_word:
            if x =="#":
                decoded_strs=[]
                return decoded_strs
          #  print(f"x:{x}")
            chrout=[]
            chr1=0
            chro=[]
            x+="/"
            
            for y in x:
               # print(f"y{y}")
                if y !="/":
                    chro.append(y)
                  #  print(chro)
                elif y == "/":
                    if chro:
                        chr1=chr(int(''.join(chro)))
                       # print(chr1)
                        chrout.append(chr1)
                        chro=[]
            chroutde=str(''.join(chrout))
            decoded_strs.append(chroutde)
        print("done1.1")
        return decoded_strs    


