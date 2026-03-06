good = r'''
                          ,dM
                         dMMP
                        dMMM'
                        \MM/
                        dMMm.           z
                       dMMP'_\---.       z
                      _| _  p ;88;`.   z
                    ,db; p >  ;8P|  `.
                   (``T8b,__,'dP |   |
                   |   `Y8b..dP  ;_  |     he's sleepy
                   |    |`T88P_ /  `\;
                   :_.-~|d8P'`Y/    /
                    \_   TP    ;   7`\
         ,,__        >   `._  /'  /   `\_
         `._ """"~~~~------|`\;' ;     ,'
            """~~~-----~~~'\__[|;' _.-'  `\
                    ;--..._     .-'-._     ;
                   /      /`~~"'   ,'`\_ ,/
                  ;_    /'        /    ,/
                  | `~-l         ;    /
                  `\    ;       /\.._|
                    \    \      \     \
                    /`---';      `----'
                   (     /            fsc
                    `---'
'''

bad = r"""
                                           HELP!
                           o           \o/
                          /|\           |        you vs. a very awake guard
                    ------/_\----------/->------
"""
guard_awake = False
if not guard_awake:
    outcome = "Shadow: It's your lucky day. Now if you keep quiet i'm sure you can sneak past."
    print(good)
else:
    outcome = "Doom: iiii... would start running the other way."
    print(bad)
print(outcome)