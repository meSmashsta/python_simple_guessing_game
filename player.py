from dataclasses import dataclass

from rx.subject import BehaviorSubject

@dataclass
class Player:
    score: int = 0
    scoreSubject = BehaviorSubject(0)
    
    def addScore(self, score):
        self.score += score
        self.scoreSubject.on_next(self.score)