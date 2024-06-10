class RankValues():
    ADMIN = (1 << 15)
    QUEST = (1 << 14)
    MOD = (1 << 13)

    ranks = {
        "ADMIN": ADMIN,
        "QUEST": QUEST,
        "MOD": MOD
    }

class Rank: 
    def getRanks(value: int):
        ranks: str = []

        for key, _value in RankValues.ranks.items(): 
            if value & _value: 
                ranks.append(key) 
        
        return ranks
        
    def isRank(value: int, rank: RankValues):
        return True if (value & rank) else False

    def makeRank(ranks: list[RankValues] | RankValues): 
        newRank = 0

        if not isinstance(ranks, list):
            ranks = [ranks] 

        if isinstance(ranks[0], str): 
            for x in ranks: 
                if (rankValue := RankValues.ranks.get(x)): 
                    newRank |= rankValue
                else: 
                    print(f"{x} is invald rank..")
        
            return newRank

        for x in ranks: 
            newRank |= x
        return newRank
    
    def addrank(value: int, rank: RankValues):
        return (value | rank)


rank = 0 | RankValues.QUEST
rank |= RankValues.MOD

r = Rank.makeRank(RankValues.ADMIN)
r = Rank.addrank(r, RankValues.MOD)
print(Rank.getRanks(r))

r = Rank.makeRank(RankValues.ADMIN)
print(Rank.getRanks(r))

# highPins = [0,1,2,3, 8,9,10, 15]
# pinStatus = 0

# for x in range(0, len(highPins)):
#     pinStatus |= (1 << highPins[x])

# # for x in range(0, 16):
# #     print((pinStatus & (1 << x)))
# #     # print(f"Pin: {x}:{"HIGH" if (pinStatus & (1 << x)) else "LOW"}")

# for x in range(0, 16):
#     # print((rank & (1 << x)))
#     print(f"Pin: {x}:{"HIGH" if (rank & (1 << x)) else "LOW"}")
