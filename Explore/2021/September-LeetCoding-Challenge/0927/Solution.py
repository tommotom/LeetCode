class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        def parseEmail(email):
            i = 0
            while i < len(email):
                if email[i] == "@": break
                i += 1
            return email[:i], email[i+1:]

        def processLocal(local):
            sb = []
            for l in local:
                if l == ".": continue
                if l == "+": break
                sb.append(l)
            return "".join(sb)

        unique_emails = defaultdict(set)
        for email in emails:
            local, domain = parseEmail(email)
            local = processLocal(local)
            unique_emails[domain].add(local)
        return sum(len(l) for l in unique_emails.values())
