from utils.class_logger import Logger

class Percentage:
    def __init__(self,hostile_score,non_hostile_score,len_of_text):
        self.hostile_score = hostile_score
        self.non_hostile_score = non_hostile_score
        self.len_of_text = len_of_text
        self.risk_percent = 0
        self.logger = Logger.get_logger()


    def percentage_calculator(self):

        try:
            total_score = self.hostile_score + self.non_hostile_score
            result = (total_score / self.len_of_text) * 100
            self.risk_percent = result
            self.logger.info("calculated percent")
            return self.risk_percent
        except Exception as e:
            self.logger.info(f"calculate percent error: {e}")