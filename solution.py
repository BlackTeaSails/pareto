

class Solution:
    def __init__(self, satisfaction, effort):
        self.satisfaction = satisfaction
        self.effort = effort

    @property
    def productivity(self):
        """This is the productivity value of a Solution."""
        if self.effort:
            return (self.satisfaction//self.effort)
        return 0

    def __str__(self):
        return "Solution with satisfaction: %d" %self.satisfaction + ", effort: %d" %self.effort + ", and productivity: %d" %self.productivity

    def __cmp__( self, other ) :
        if self.productivity < other.productivity :
            return -1
        elif self.productivity > other.productivity :
            return 1
        else :
            return 0
