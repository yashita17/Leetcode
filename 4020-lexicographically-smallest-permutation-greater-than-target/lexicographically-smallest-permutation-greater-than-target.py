class Solution(object):
    def lexGreaterPermutation(self, s, target):
        count = [0] * 26

        for ch in s:
            count[ord(ch) - 97] += 1

        n = len(target)
        i = 0

        while i < n:
            x = ord(target[i]) - 97

            if count[x] == 0:
                break

            count[x] -= 1
            i += 1

        if i == n:
            i = n - 1
            count[ord(target[i]) - 97] += 1

        while i >= 0:
            x = ord(target[i]) - 97

            for j in range(x + 1, 26):
                if count[j] > 0:
                    count[j] -= 1

                    ans = list(target[:i])
                    ans.append(chr(j + 97))

                    for k in range(26):
                        ans.extend([chr(k + 97)] * count[k])

                    return ''.join(ans)

            i -= 1
            count[ord(target[i]) - 97] += 1

        return ""
        