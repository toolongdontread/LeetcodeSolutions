class Solution:
    def intToRoman(self, num: int) -> str:
        s = ""
        s2 = str(num)
        
        if len(s2) == 4:
            if s2[0] == "1":
                s+="M"
                s2=s2.replace(s2[0], "", 1)
            elif s2[0] == "2":
                s+="MM"
                s2=s2.replace(s2[0], "", 1)
            elif s2[0] == "3":
                s+="MMM"
                s2=s2.replace(s2[0], "", 1)
            else:
                s+=""
                s2=s2.replace(s2[0], "", 1)
            
        if len(s2) == 3:
            if s2[0] == "1":
                s+="C"
                s2=s2.replace(s2[0], "", 1)
            elif s2[0] == "2":
                s+="CC"
                s2=s2.replace(s2[0], "", 1)
            elif s2[0] == "3":
                s+="CCC"
                s2=s2.replace(s2[0], "", 1)
            elif s2[0] == "4":
                s+="CD"
                s2=s2.replace(s2[0], "", 1)
            elif s2[0] == "5":
                s+="D"
                s2=s2.replace(s2[0], "", 1)
            elif s2[0] == "6":
                s+="DC"
                s2=s2.replace(s2[0], "", 1)
            elif s2[0] == "7":
                s+="DCC"
                s2=s2.replace(s2[0], "", 1)
            elif s2[0] == "8":
                s+="DCCC"
                s2=s2.replace(s2[0], "", 1)
            elif s2[0] == "9":
                s+="CM"
                s2=s2.replace(s2[0], "", 1)
            else:
                s2+=""
                s2=s2.replace(s2[0], "", 1)

        if len(s2) == 2:
            if s2[0] == "1":
                s+="X"
                s2=s2.replace(s2[0], "", 1)
            elif s2[0] == "2":
                s+="XX"
                s2=s2.replace(s2[0], "", 1)
            elif s2[0] == "3":
                s+="XXX"
                s2=s2.replace(s2[0], "", 1)
            elif s2[0] == "4":
                s+="XL"
                s2=s2.replace(s2[0], "", 1)
            elif s2[0] == "5":
                s+="L"
                s2=s2.replace(s2[0], "", 1)
            elif s2[0] == "6":
                s+="LX"
                s2=s2.replace(s2[0], "", 1)
            elif s2[0] == "7":
                s+="LXX"
                s2=s2.replace(s2[0], "", 1)
            elif s2[0] == "8":
                s+="LXXX"
                s2=s2.replace(s2[0], "", 1)
            elif s2[0] == "9":
                s+="XC"
                s2=s2.replace(s2[0], "", 1)
            else:
                s2+=""
                s2=s2.replace(s2[0], "", 1)

        if len(s2) == 1:
            if s2[0] == "1":
                s+="I"
                s2=s2.replace(s2[0], "", 1)
            elif s2[0] == "2":
                s+="II"
                s2=s2.replace(s2[0], "", 1)
            elif s2[0] == "3":
                s+="III"
                s2=s2.replace(s2[0], "", 1)
            elif s2[0] == "4":
                s+="IV"
                s2=s2.replace(s2[0], "", 1)
            elif s2[0] == "5":
                s+="V"
                s2=s2.replace(s2[0], "", 1)
            elif s2[0] == "6":
                s+="VI"
                s2=s2.replace(s2[0], "", 1)
            elif s2[0] == "7":
                s+="VII"
                s2=s2.replace(s2[0], "", 1)
            elif s2[0] == "8":
                s+="VIII"
                s2=s2.replace(s2[0], "", 1)
            elif s2[0] == "9":
                s+="IX"
                s2=s2.replace(s2[0], "", 1)
            else:
                s2+=""
                s2=s2.replace(s2[0], "", 1)

        return s
            