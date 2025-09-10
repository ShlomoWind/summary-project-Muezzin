from percentage_calculation import Percentage
from deciphering import Decoder
from identifying_matches import MatchCount
from level_attach import AttachLevel
from words_lists import hostile_list,non_hostile_list

class PercentManager:
    def __init__(self,text):
        self.decode = Decoder
        self.percentage = Percentage
        self.matcher = MatchCount
        self.level_attach = AttachLevel

        self.text = text
        self.host_list = self.decode(hostile_list).decoding_code()
        self.non_host_list = self.decode(non_hostile_list).decoding_code()
        self.percent = None
        self.level = None
        self.is_dangers = None

    def run(self):
        host_score,non_host_score = self.matcher(self.text,self.host_list,self.non_host_list).match_count()
        self.percent = self.percentage(host_score,non_host_score,len(self.text)).percentage_calculator()
        self.level = self.level_attach(self.percent).attach_by_percent()
        if self.percent > 0:
            self.is_dangers = True
        else:
            self.is_dangers = False
        return self