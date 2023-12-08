puzzle_input = open("data.txt", "r").read().rstrip().splitlines()

cards_order = ('2','3','4','5','6','7','8','9','T','J','Q','K','A')
new_cards = 'abcdefghilmno'
res1 = 0
res2 = 0

class Hand:
    def __init__(self, cards: str, bid: str,new_order):
        self.bid = int(bid)        
        self.cards = cards
        self.newcards = ''.join(map(lambda x :str(new_cards[cards_order.index(x)]),self.cards))
        self.replaced_cards = ''
        if (new_order) :
            if 'a' in self.newcards and self.newcards != 'aaaaa': 
                card_counts = {card: self.newcards.count(card) for card in set(self.newcards) - {'a'}}
                self.replaced_cards = self.newcards.replace('a', sorted(card_counts, key=lambda card: card_counts[card])[-1])
            else :
                self.replaced_cards = self.newcards

    @property
    def hand_power(self) -> int:
        unique_cards = set(self.replaced_cards)
        counts = [self.replaced_cards.count(card) for card in unique_cards]
        if 5 in counts :
            return 6
        elif 4 in counts :
            return 5
        elif 3 in counts and 2 in counts :
            return 4
        elif 3 in counts :
            return 3
        elif counts.count(2) == 2 :
            return 2
        elif 2 in counts :
            return 1
        else :
            return 0

    def __lt__(self, other: "Hand") -> bool:
        if self.hand_power != other.hand_power :
            return self.hand_power < other.hand_power
        return self.newcards < other.newcards
    
    def __repr__(self):
        return self.cards +" "+str(self.bid)+" "+str(self.hand_power)+' '+self.newcards+' '+self.replaced_cards+'\n'
    

hands = [Hand(*line.split(),0) for line in puzzle_input]
hands = sorted(hands)
for index,hand in enumerate(hands) :
    res1 += hand.bid * (index+1)

cards_order = ('J','2','3','4','5','6','7','8','9','T','Q','K','A')

hands = [Hand(*line.split(),1) for line in puzzle_input]
hands = sorted(hands)
for index,hand in enumerate(hands) :
    res2 += hand.bid * (index+1)

print("part 1 : ",res1)
print("part 2 : ",res2)