class Percentage:
    def __init__(self,hostile_score,non_hostile_score,len_of_text):
        self.hostile_score = hostile_score
        self.non_hostile_score = non_hostile_score
        self.len_of_text = len_of_text
        self.risk_percent = 0

    def percentage_calculator(self):
        total_score = self.hostile_score + self.non_hostile_score
        result = total_score / self.len_of_text
        self.risk_percent = result
        return self.risk_percent