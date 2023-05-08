class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        out = 0
        for i in items:
            if ruleKey == "type":
                if i[0] == ruleValue:
                    out += 1
            elif ruleKey == "color":
                if i[1] == ruleValue:
                    out +=1
            elif ruleKey == "name":
                if i[2] == ruleValue:
                    out += 1
        return out    