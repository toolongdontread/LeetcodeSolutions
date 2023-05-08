class Solution:
    def romanToInt(self, s: str) -> int:
        
        cm = s.count("CM")*900
        s=s.replace("CM", "")
        cd = s.count("CD")*400
        s=s.replace("CD", "")
        xc = s.count("XC")*90
        s=s.replace("XC", "")
        xl = s.count("XL")*40
        s=s.replace("XL", "")
        ix = s.count("IX")*9
        s=s.replace("IX", "")
        iv = s.count("IV")*4
        s=s.replace("IV", "")
        m = s.count("M")*1000
        s=s.replace("M", "")
        d = s.count("D")*500
        s=s.replace("D", "")
        c = s.count("C")*100
        s=s.replace("C", "")
        l = s.count("L")*50
        s=s.replace("L", "")
        x = s.count("X")*10
        s=s.replace("X", "")
        v = s.count("V")*5
        s=s.replace("V", "")
        i = s.count("I")
        s=s.replace("I", "")

        return cm+cd+xc+xl+ix+iv+m+d+c+l+x+v+i; 