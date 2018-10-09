# https://open.kattis.com/problems/yikes
# Wrong Answer on TC 2 - reason unknown as of contest end

TC = int(input())

for _ in range(TC):
    M,B,D,T = [float(i) for i in input().split()]

    maxL = T+ 4.5/M
    maxR = T+ 5.5/M

    #print(M,B,D,T, 'MAX!!', maxL,maxR)

    if maxR < D/B:
        print("Max beats the first bicycle")
        continue

    for bike in range(10):
        m_D = D + 4*bike
        mL = m_D/B
        mR = (m_D+2)/B
        #print(mL, mR)
        # if his crossing is not out of range with the bike
        if not (maxL > mR or maxR < mL):
            print("Collision with bicycle", bike+1)
            break
        # if he crosses
        elif maxL > mR:
            if bike == 9 or maxR < (m_D+4)/B:
                print("Max crosses safely after bicycle", bike+1)
                break