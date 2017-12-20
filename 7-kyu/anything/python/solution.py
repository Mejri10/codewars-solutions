class Anything:
    @classmethod
    def __lt__(cls, arg):
        return True
        
    @classmethod
    def __le__(cls, arg):
        return True
        
    @classmethod
    def __eq__(cls, arg):
        return True
        
    @classmethod        
    def __ne__(cls, arg):
        return True
        
    @classmethod        
    def __ge__(cls, arg):
        return True
        
    @classmethod        
    def __gt__(cls, arg):
        return True

def anything(thing):
    return Anything()