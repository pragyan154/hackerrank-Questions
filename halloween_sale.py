def howManyGames(p, d, m, s):
    count = 1
    ss = p

    if p>=s:
        count = 0

    else:

        while ss + m <= s:
            if p - d < m:

                p = m
                #print(count, p, ss, "a")

            if p == m:
                count += 1

                ss += p

                #print(count, p, ss, "b")


            elif p+(p-d)<=s:
                count += 1

                p = p - d
                ss += p

                #print(count, p, ss, "c")

            else:
                return count


    return count
