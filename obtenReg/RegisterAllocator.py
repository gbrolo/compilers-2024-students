class RegisterAllocator:
    def __init__(self):
        self.registers = {'R1': None, 'R2': None, 'R3': None}
        self.memory = {}  # To store spilled values
        self.next_spill = 0  # Counter for spilled variables

    def get_register(self, variable):
        # Check if the variable is already in a register
        for reg, value in self.registers.items():
            if value == variable:
                return reg
        
        # If not in a register, assign it to a free one
        for reg in self.registers:
            if self.registers[reg] is None:
                self.registers[reg] = variable
                return reg
        
        # If no free registers, spill the first one
        return self.spill_and_assign(variable)

    def spill_and_assign(self, variable):
        # Spill the first register to memory
        spill_reg = list(self.registers.keys())[0]
        spilled_value = self.registers[spill_reg]
        self.memory[f'mem{self.next_spill}'] = spilled_value
        self.next_spill += 1
        
        # Assign the new variable to the now-free register
        self.registers[spill_reg] = variable
        return spill_reg

    def __str__(self):
        return f'Registers: {self.registers}\nMemory: {self.memory}'

# Example Usage
allocator = RegisterAllocator()

# Simulate allocation of variables
print(allocator.get_register('a'))  # R1
print(allocator.get_register('b'))  # R2
print(allocator.get_register('c'))  # R3
print(allocator)  # Shows the current state of registers and memory

# Now request a new variable, which causes spilling
print(allocator.get_register('d'))  # R1 (spills 'a')
print(allocator)  # Shows 'a' spilled to memory and 'd' assigned to R1
