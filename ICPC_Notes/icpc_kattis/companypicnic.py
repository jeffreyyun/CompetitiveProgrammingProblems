# BFS, recursion, DP
# Time: O(N) = (# nodes) * (# avg children)
# Space: O(N)

# global dicts
memo = {}
teams = {}
speed = {}
children = {}
# if name has no children, base case is 0,0
def getStats(name):
    # memo[name] stores total speeds w/ and w/o name on a team
    # teams[name] stores total pairings w/ and w/o name on a team
    memo.setdefault(name, [0,0])
    teams.setdefault(name, [0,0])
    # find # pairings and max total speed w/o name on a team
    for child in children[name]:
        getStats(child)
        memo[name][1] += max(memo[child][0], memo[child][1])
        teams[name][1] += max(teams[child][0], teams[child][1])
    # find # pairings and max total speed w/ name on a team
    for child in children[name]:
        # teams if we have name pair with that child
        m_teams = teams[name][1] - max(teams[child][0], teams[child][1]) + teams[child][1] + 1
        m_tot_speed = memo[name][1] - max(memo[child][0], memo[child][1]) + memo[child][1] + min(speed[child], speed[name])
        # update total speed as needed
        if m_teams > teams[name][0]:
            teams[name][0] = m_teams
            memo[name][0] = m_tot_speed
        elif m_teams == teams[name][0]:
            memo[name][0] = max(m_tot_speed, memo[name][0])
    return

if __name__ == '__main__':
    N = int(input())

    # process input
    for _ in range(N):
        name, m_speed, boss = input().split()
        speed[name] = float(m_speed)
        children.setdefault(name, [])
        if boss == "CEO":
            m_CEO = name
        else:
            children.setdefault(boss, [])
            children[boss].append(name)

    # get stats from root, recursively up from the children
    getStats(m_CEO)

    # evaluate for the most teams, and the highest total speeds
    if teams[m_CEO][0] > teams[m_CEO][1]:
        tot_speed = memo[m_CEO][0]
    elif teams[m_CEO][0] < teams[m_CEO][1]:
        tot_speed = memo[m_CEO][1]
    else:
        tot_speed = max(memo[m_CEO][0], memo[m_CEO][1])

    tot_teams = max(teams[m_CEO][0], teams[m_CEO][1])

    print(tot_teams, tot_speed/tot_teams if tot_teams > 0 else 0)
