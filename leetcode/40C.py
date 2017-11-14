class Solution:
    def __init__(self):
        self.best_cost = 9999999999

    def shoppingOffers(self, price, special, needs, cost=0):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        #print(price, special, needs, cost)
        m_needs = needs.copy()
        if min(m_needs) < 0:
            return 999999999999999
        elif max(m_needs) == 0:
            self.best_cost = min(self.best_cost, cost)
            return cost

        for i in range(len(special)):
            #print(price, m_needs)
            new_cost = self.shoppingOffers(price, special, [m_needs[j]-special[i][j] for j in range(len(m_needs))], cost + special[i][-1])
            individ_buy = sum([price[i]*m_needs[i] for i in range(len(price))])
            this_buy = min(new_cost, cost+individ_buy)
            self.best_cost = min(self.best_cost, this_buy)
            #print(new_cost, cost+individ_buy)

        return self.best_cost
