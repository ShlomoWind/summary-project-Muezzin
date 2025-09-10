class AttachLevel:
    def __init__(self,percent):
        self.percent = percent
        self.level = None

    def attach_by_percent(self):
        if self.percent > 1:
            self.level = "high"
        elif self.percent > 0:
            self.level = "medium"
        else:
            self.level = "none"
        return self.level