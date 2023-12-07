from collections import Counter
from functools import total_ordering

fh = open("input7-1.dat", "r")
#fh = open("test.dat", "r")

#@total_ordering
class Hand(object):
   def __init__(self, rawhand, bid):
      self.rawhand = rawhand
      self.bid = bid
      self.new_rawhand = self.evaluate_jokers()
      self.type_val = self.get_type_val(self.new_rawhand)

   def get_type_val(self, raw):
      freq = Counter(raw)
      self.signature = tuple(sorted( ( x[1] for x in freq.items() ) ))
      # Five of a kind
      if self.signature == (5,):
         val = 100
      # Four of a kind
      elif self.signature == (1, 4):
         val = 90
      # Full House
      elif self.signature == (2, 3):
         val = 80
      # Three of a kind
      elif self.signature == (1, 1, 3):
         val = 70
      # Two Pair
      elif self.signature == (1, 2, 2):
         val = 60
      # One Pair
      elif self.signature == (1, 1, 1, 2):
         val = 50
      # High Card
      elif self.signature == (1, 1, 1, 1, 1):
         val = 10
      else:
         val = -99
      
      return val
   
   def evaluate_jokers(self):
      # How many J's?
      tmp = self.rawhand.replace("J","")
      tmp_freq = Counter(tmp)
      if tmp!="":
         (char, val) = tmp_freq.most_common(1)[0]
      else:
         return self.rawhand
      return self.rawhand.replace("J", char)

   @property
   def for_sort(self):
      return ( self.rawhand
                   .replace("T","a")
                   .replace("J","0")  # J is a weak card now
                   .replace("Q","c")
                   .replace("K","d")
                   .replace("A","e")
      )
   
   def __str__(self):
      return f"{self.rawhand}, {self.new_rawhand}, Bid={self.bid:4d}, Sig: {str(self.signature):>15s}, Value={self.type_val:3d}"

lines = fh.readlines()
hands = []
for line in lines:
   (rawhand, bidstr) = line.strip("\n").split()
   h = Hand(rawhand, int(bidstr))
   hands.append( (h.type_val, h.for_sort, h.bid))

total = 0
for idx, (val, sort_str, bid) in enumerate(sorted(hands)):
   print( (bid, idx+1))
   total += (idx+1) * bid

print(total)



