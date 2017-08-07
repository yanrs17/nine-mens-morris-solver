class Strategy:
    def __init__(self):
        pass
        
    def get_next_move(self, state):
        raise NotImplementedError('Must be implemented in subclass')