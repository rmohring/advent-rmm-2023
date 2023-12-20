import numpy as np
from collections import Counter

fh = open("input20-1.dat")
#fh = open("test.dat")
#fh = open("test2.dat")

lines = fh.readlines()
lines = [x.strip("\n") for x in lines]

class FlipFlop:
    def __init__(self, name, outputs=None):
        self.unit_type = "FLIP"
        self.on = False
        self.name = name
        self.inputs = {}
        self.outval = None
        if outputs is not None:
            self.outputs = outputs
            #self.outputs = { x:0 for x in outputs }
        else:
            self.outputs = []
            #self.outputs = {}            

    def add_input(self, name):
        self.inputs[name] = None

    def add_output(self, name):
        self.outputs.append(name)
        #self.outputs[name] = 1

    def update(self, name, pulse):
        self.outval = None
        self.set_input(name, pulse)
        return self.transmit()
            
    def set_input(self, name, pulse):
        self.inputs[name] = pulse
        if pulse == 0:
            self.on = not self.on
            self.outval = int(self.on)
        
    def transmit(self):
        # Return a set of ordered instruction tuples (send_to, high/low)
        # or nothing if no further output
        transmissions = []
        if self.outval is not None:
            for o in self.outputs:
                transmissions.append( (o, self.name, self.outval) )
        
        return transmissions

    def __str__(self):
        onstr = "ON" if self.on else "OFF"
        return f"[{self.name:4s}] {self.unit_type}-{onstr:3s}; I: {self.inputs}; O: {self.outputs}; V: {self.outval}"

class Conjuction:
    def __init__(self, name, outputs=None):
        self.unit_type = "CONJ"
        self.name = name
        self.inputs = {}
        self.outval = None
        if outputs is not None:
            self.outputs = outputs
            #self.outputs = { x:0 for x in outputs }
        else:
            self.outputs = []
            #self.outputs = {}  

    def add_input(self, name):
        self.inputs[name] = 0

    def add_output(self, name):
        self.outputs.append(name)
        #self.outputs[name] = 1

    def update(self, input_name, pulse):
        self.set_input(input_name, pulse)
        return self.transmit()

    def set_input(self, input_name, pulse):
        self.inputs[input_name] = pulse

        if np.all( [v==1 for v in self.inputs.values() ] ):
            self.outval = 0
        else:
            self.outval = 1

    def transmit(self):
        # Return a set of ordered instruction tuples (send_to, high/low)
        # or nothing if no further output
        transmissions = []
        if self.outval is not None:
            for o in self.outputs:
                transmissions.append( (o, self.name, self.outval) )
        
        return transmissions
    
    def __str__(self):
        return f"[{self.name:4s}] {self.unit_type}; I: {self.inputs}; O: {self.outputs}; V: {self.outval}"

class Endpoint:
    def __init__(self, name):
        self.unit_type = "ENDP"
        self.name = name
        self.inputs = {}
        self.outval = None
        self.touches = 0

    def add_input(self, name):
        self.inputs[name] = 0

    def update(self, input_name, pulse):
        self.set_input(input_name, pulse)
        return self.transmit()

    def set_input(self, input_name, pulse):
        self.inputs[input_name] = pulse

    def transmit(self):
        # Return a set of ordered instruction tuples (send_to, high/low)
        # or nothing if no further output
        transmissions = []       
        return transmissions
    
    def __str__(self):
        return f"[{self.name:4s}] {self.unit_type}; I: {self.inputs}"
    
# -------------------------------------
units = {}
inputs_to_add = []
broadcaster = []

for line in lines:
    instr, outstr = line.split(" -> ")
    outputs = outstr.replace(" ","").split(",")
    
    if instr=="broadcaster":
        name = instr
        broadcaster = outputs
    else:
        t = instr[0]
        name = instr[1:]
        if t=="%":
            units[name] = FlipFlop(name, outputs)
        elif t=="&":
            units[name] = Conjuction(name, outputs)
    
    for o in outputs:
        inputs_to_add.append( (name, o) )

# for each output, create an input on the devices (all conjs):
for input_name, unit_name in inputs_to_add:
    if unit_name not in units:
        units[unit_name] = Endpoint(unit_name)        

    units[unit_name].add_input(input_name)
        

def print_state():
    for u in units.values():
        print(u)

pulse_ctr = Counter()
for loop_ctr in range(1000):
    # Push the button
    #pulse_ctr['P'] += 1
    pulse_ctr[0] += 1
    
    queue = []
    for o in broadcaster:
        queue.append( (o, 'broadcaster', 0))

    while queue:
        (target_unit_name, input_name, value) = queue.pop(0)
        pulse_ctr[value] += 1
        #print(f"{input_name} -{value}-> {target_unit_name}")
        #print("====================")
        #print_state()
        new = units[target_unit_name].update(input_name, value)
        #print("=====", target_unit_name, "sends", new)
        #print_state()
        queue.extend(new)
        #print("QUEUE:", queue)
        

print_state()
answer = 1
for k,v in pulse_ctr.items():
    answer *= v
print("Answer: ", answer, pulse_ctr)