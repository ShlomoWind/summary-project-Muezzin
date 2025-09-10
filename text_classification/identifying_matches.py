from utils.class_logger import Logger

class MatchCount:
    def __init__(self,text,hostile_list,non_hostile_list):
        self.text = text.lower()
        self.hostile_list = hostile_list
        self.non_hostile_list = non_hostile_list
        self.hostile_score = 0
        self.non_hostile_score = 0
        self.logger = Logger.get_logger()


    def match_count(self):
        for word in self.hostile_list:
            word = word.lower()
            if word in self.text:
                self.hostile_score += self.text.count(word)
        self.hostile_score *= 2

        for word in self.non_hostile_list:
            word = word.lower()
            if word in self.text:
                self.non_hostile_score += self.text.count(word)
        self.logger.info("word count has ended")
        return self.hostile_score,self.non_hostile_score