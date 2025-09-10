from utils.class_logger import Logger

class AttachLevel:
    def __init__(self,percent):
        self.percent = percent
        self.level = None
        self.logger = Logger.get_logger()

    def attach_by_percent(self):
        if self.percent > 1:
            self.level = "high"
        elif self.percent > 0:
            self.level = "medium"
        else:
            self.level = "none"
        self.logger.info("created a level")
        return self.level