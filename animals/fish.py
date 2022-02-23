class Fish:
    def __init__(self):
        '''Constructor for Fish.'''
        # Create some member animals
        self.members = ['Cod', 'Salmon', 'Tuna']
        
    def printMembers(self):
        print('Printing members of the Fish class')
        for member in self.members:
            print('\t%s ' % member)
