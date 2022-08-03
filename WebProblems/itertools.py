from itertools import groupby
payroll = [34000, 98000, 45000, 22000]
entry_level_group = groupby(payroll, key=lambda x:x<98000)
for key, value in entry_level_group:
    print(key, list(value))




def bitcoin_trades():
     yield 0.005
     yield 0.0016
     yield 0.3016
t= bitcoin_trades()
print(t)