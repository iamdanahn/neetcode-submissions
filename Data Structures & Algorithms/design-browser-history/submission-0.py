class BrowserHistory:

    def __init__(self, homepage: str):
        # stack/list structure to keep track
        # each ele will be the url
        self.history = [homepage]
        self.curPos = 0

    def visit(self, url: str) -> None:
        # if in current position is not at the end
        # clear everything after the currPos
        # add url to the end 
        self.curPos += 1
        if self.curPos != len(self.history):
            self.history = self.history[:self.curPos]
        self.history.append(url)

    def back(self, steps: int) -> str:
        self.curPos -= steps
        self.curPos = max(0, self.curPos)
        return self.history[self.curPos]

    def forward(self, steps: int) -> str:
        self.curPos += steps
        self.curPos = min(len(self.history)-1, self.curPos)
        return self.history[self.curPos]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)