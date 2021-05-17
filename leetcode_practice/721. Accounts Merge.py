class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        uf = list(range(n))     #uf表示的数组是每个数的parent，一开始设置为跟节点一样
        def union(a, b):
            uf[find(a)] = find(b)
        def find(x):
            if uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]
        
        email_dict = {}
        for i in range(n):
            account = accounts[i]
            for j in range(1, len(account)):
                if account[j] not in email_dict:
                    email_dict[account[j]] = i
                else:
                    union(email_dict[account[j]], i)
        graphs = collections.defaultdict(list)
        for i in range(n):
            graphs[find(i)].append(i)
        res = []
        for idx, idx_list in graphs.items():
            cur = [accounts[idx][0]]
            emails = set()
            for i in idx_list:
                emails.update(accounts[i][1:])      #update the set by adding items from other
            emails = list(emails).sort()
            cur.extend(emails)
            res.append(cur)
        return res
