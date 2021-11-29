class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        name_to_emails = defaultdict(list)
        for account in accounts:
            name = account[0]
            emails = set(account[1:])
            i = 0
            while i < len(name_to_emails[name]):
                if name_to_emails[name][i] & emails:
                    emails |= name_to_emails[name][i]
                    name_to_emails[name].pop(i)
                else:
                    i += 1
            name_to_emails[name].append(emails)

        ans = []
        for name in name_to_emails.keys():
            for emails in name_to_emails[name]:
                ans.append([name] + sorted(emails))
        return ans
