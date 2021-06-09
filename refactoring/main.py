
class Homeowner:
    def __init__(self, name="Jan", address="Earth", needs=["electrician"]):
        self.name = name
        self.address = address
        self.needs = needs
        return



class Specialist(Homeowner):
    def __init__(self, name, proffesion):
        self.name = name
        self.proffesion = proffesion
        return 

    def contracts_list(self, Homeowner):
        specialists = []
        contracts_list = []
        homeowner_needs =  Homeowner.needs
        for need in homeowner_needs:
            specialists.append(need)
            current_need = need
            if self.proffesion == current_need:
                contracts_list.append(self.name)          
        return contracts_list

    def contracts_output(self):
        proffesion = self.proffesion
        return proffesion
        
alice = Specialist('Alice Aliceville', 'electrician')
bob = Specialist('Bob Bobsville', 'painter')
craig = Specialist('Craig Craigsville', 'plumber')


alfred = Homeowner('Alfred Alfredson', 'Alfredslane 123', ['painter', 'plumber'])
bert = Homeowner('Bert Bertson', 'Bertslane 231', ['plumber'])
candince = Homeowner('Candice Candicedottir', 'Candicelane 312', ['electrician', 'painter'])
print(Specialist.contracts_list(alice, candince))
#print(Specialist.contracts(candice))


