good = r"""
     8 8 8 8                     ,ooo.
     8a8 8a8                    oP   ?b   key:3
    d888a888zzzzzzzzzzzzzzzzzzzz8     8b
     `""^""'                    ?o___oP'
"""

bad = r'''
         .-"""-.
        /      c\
       |    c   0).-.  sad otter :( 
       |       .-;(_/     .-.      
        \     /  /)).---._|  `\   ,
         '.  '  /((       `'-./ _/|
           \  .'  )        .-.;`  / 
            '.             |  `\-'
              '._        -'    /
        jgs      ``""--`------`
'''

has_key = False
if has_key:
    outcome = "Click: wowie, would you look at that! well, what are you waiting for?"
    print(good)
else:
    outcome = "Doom: aww shucks.. guess you have to go another way..."
    print(bad)
print(outcome)