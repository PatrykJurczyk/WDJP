from random import randint

def play_cards() -> list:
    colors = ["Pik", "Karo", "Czerwo", "Trefl"]
    figure = ["As", "Król", "Dama", "Jopek"] + [str(x) for x in range(10,1,-1)]
    cards = [ y+' '+x for x in colors for y in figure]
    players = []
    for i in range(4):
        hand = []
        for j in range(5):
            card = cards[randint(0, len(cards)-1)]
            hand.append(card)
            cards.remove(card)
        players.append(hand)
    return f'Patryk: {players[0]}\Bartek: {players[1]}\Olek: {players[2]}\Marcin: {players[3]}\n'