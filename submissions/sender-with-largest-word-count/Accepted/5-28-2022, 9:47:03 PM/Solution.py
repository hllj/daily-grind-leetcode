// https://leetcode.com/problems/sender-with-largest-word-count

class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        n = len(messages)
        s = {}
        for idx, mess in enumerate(messages):
            word_cnt = len(mess.split(' '))
            sender = senders[idx]
            if sender not in s:
                s[sender] = word_cnt
            else:
                s[sender] += word_cnt
        li = []
        for key, value in s.items():
            print(key, value)
            li.append({
                'sender': key, 
                'word': value
            })
        li = sorted(li, key=lambda x: (x['word'], x['sender']), reverse=True)
        return li[0]['sender']