'''Thi is a module docstr'''

value={1:'Ace',11:'Jack',12:'Queen',13:'King'}
for _ in range(2,11):
    value[_]=_
suit={0:'Spades',1:'Hearts',2:'Diamonds',3:'Clubs'}
def  the_name_of_your_card(v_0, s_0 = 0):
    """Name of card as a string."""
    if (v_0 < 1  or v_0 > 13 or s_0 not in (0,1,2,3)):
        raise ValueError


    return f'I have read your mind and  \
    predict your card is the {value[v_0]} of {suit[s_0]})'
print( the_name_of_your_card(2,  s_0= 3))
