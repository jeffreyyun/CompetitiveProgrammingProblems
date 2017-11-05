class Solution:
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        adict = {}
        edict = {}

        for i, a in enumerate(accounts):
            m_id = i
            m_emails = set()

            for e in a[1:]:
                # switch all previous emails to this id
                if e in edict:
                    old_id = edict[e]
                    # transfers emails from other account
                    for oe in adict[old_id]:
                        m_emails.add(oe)
                    adict[old_id] = []
                m_emails.add(e)

            for e in m_emails:
                edict[e] = m_id

            adict[m_id] = m_emails    # store emails

        all_accounts = []

        for m_id in adict.keys():
            # if is current account
            emails = adict[m_id]
            if len(emails) > 0:
                all_accounts.append([accounts[m_id][0]] + sorted(list(emails)))

        return all_accounts
