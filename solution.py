

class Solution:
    def __init__(self, effort, satisfaction):
        self.effort = effort
        self.satisfaction = satisfaction

    @property
    def productivity(self):
        """This is the productivity value of a Solution."""
        if self.effort:
            return (self.satisfaction//self.effort)
        return 0

    def __str__(self):
        return "Solution with satisfaction: %d" %self.satisfaction + ", effort: %d" %self.effort + ", and productivity: %d" %self.productivity
