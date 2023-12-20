import numpy as np
from collections import Counter

fh = open("input19-1.dat")
#fh = open("test.dat")

lines = fh.readlines()
lines = [x.strip("\n") for x in lines]

class Workflow:
    def __init__(self, name, rules):
        self.name = name
        self.rules = rules  

    def process_rule(self, rule):
        #print(self.name, rule)
        check = True
        tgt = rule 

        if ":" in rule:
            cond, tgt = rule.split(":")
            if ">" in cond:
                cat, val = cond.split(">")
                check = (int(part[cat])>int(val))
            elif "<" in cond:
                cat, val = cond.split("<")
                check = (int(part[cat])<int(val))

        return (check, tgt)

    
    def check_part(self, part):
        #print(part)
        for rule in self.rules:
            check, tgt = self.process_rule(rule)
            if check:
                break
        
        # tgt will either be a new node name or A/R
        return tgt
    
workflows = {}
parts = []
part1 = True
for line in lines:
    if line=="":
        part1 = False
        continue
    if part1:
        tmp = line.replace("}","").split("{")
        name = tmp[0]
        conditions = tmp[1].split(",")
        workflows[name] = Workflow(name, conditions)
    else:
        tmp = line.replace("}","").replace("{","").split(",")
        parts.append( dict(tuple(pair.split('=')) for pair in tmp) )

tgt = 'in'
accepted_parts = []
for i,part in enumerate(parts):
    print(f"Working {i}...")
    while tgt not in ["A","R"]:    
        tgt = workflows[tgt].check_part(part)
    if tgt=="A":
        accepted_parts.append(part)
    tgt = 'in'

total = 0
for part in accepted_parts: 
    total += sum( (int(v) for k,v in part.items()) )

print("Answer: ", total)