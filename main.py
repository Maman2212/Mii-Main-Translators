Char = int(input("What mii class would you like to check? 1= Brawler, 2 = Swordfighter, 3 = Gunner:  "))
if Char == 1:
    Brawl1 = int(input("Please enter the first(Neutral) move number:  "))
    Brawl2 = int(input("Please enter the second(Side) move number:  "))
    Brawl3 = int(input("Please enter the third(Up) move number:  "))
    Brawl4 = int(input("Please enter the fourth(Down) move number:  "))
    if Brawl1 == 1:
        print('Shot Put Neutral Special')
    elif Brawl1 == 2:
        print('Flashing Mach Punch Neutral Special')
    elif Brawl1 == 3:
        print('Exploding Side Kick Neutral Special')
    if Brawl2 == 1:
        print('Onslaught Side Special')
    elif Brawl2 == 2:
        print('Burning Dropkick Side Special')
    elif Brawl2 == 3:
        print('Suplex Side Special')
    if Brawl3 == 1:
        print('Soaring Axe Kick Up Special')
    elif Brawl3 == 2:
        print('Helicopter Kick Up Special')
    elif Brawl3 == 3:
        print('Thrust Uppercut Up Special')
    if Brawl4 == 1:
        print('Head-On Assault Down Special')
    elif Brawl4 == 2:
        print('Feint Jump Down Special')
    elif Brawl4 == 3:
        print('Counter Throw Down Special')
elif Char == 2:
    Sword1 = int(input("Please enter the first(Neutral) move number:  "))
    Sword2 = int(input("Please enter the second(Side) move number:  "))
    Sword3 = int(input("Please enter the third(Up) move number:  "))
    Sword4 = int(input("Please enter the fourth(Down) move number:  "))
    if Sword1 == 1:
        print('Gale Strike Neutral Special')
    elif Sword1 == 2:
        print('Shuriken of Light Neutral Special')
    elif Sword1 == 3:
        print('Blurring Blade Neutral Special')
    if Sword2 == 1:
        print('Airborne Assault Side Special')
    elif Sword2 == 2:
        print('Gale Stab Side Special')
    elif Sword2 == 3:
        print('Chakram Side Special')
    if Sword3 == 1:
        print('Stone Scabbard Up Special')
    elif Sword3 == 2:
        print('Skyward Slash Dash Up Special')
    elif Sword3 == 3:
        print("Hero's Spin Up Special")
    if Sword4 == 1:
        print('Blade Counter Down Special')
    elif Sword4 == 2:
        print('Reversal Slash Down Special')
    elif Sword4 == 3:
        print('Power Thrust Down Special')
elif Char == 3:
    Gun1 = int(input("Please enter the first(Neutral) move number:  "))
    Gun2 = int(input("Please enter the second(Side) move number:  "))
    Gun3 = int(input("Please enter the third(Up) move number:  "))
    Gun4 = int(input("Please enter the fourth(Down) move number:  "))
    if Gun1 == 1:
        print('Charge Blast Neutral Special')
    elif Gun1 == 2:
        print('Laser Blaze Neutral Special')
    elif Gun1 == 3:
        print('Grenade Launch Neutral Special')
    if Gun2 == 1:
        print('Flame Pillar Side Special')
    elif Gun2 == 2:
        print('Stealth Burst Side Special')
    elif Gun2 == 3:
        print('Gunner Missile Special')
    if Gun3 == 1:
        print('Lunar Launch Up Special')
    elif Gun3 == 2:
        print('Cannon Jump Kick Up Special')
    elif Gun3 == 3:
        print('Arm Rocket Up Special')
    if Gun4 == 1:
        print('Echo Reflector Down Special')
    elif Gun4 == 2:
        print('Bomb Drop Down Special')
    elif Gun4 == 3:
        print('Absorbing Vortex Down Special')
