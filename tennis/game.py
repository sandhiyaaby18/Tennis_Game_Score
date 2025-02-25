from setup_logger import logger

class Game:
    score_map = ["Love", "Fifteen", "Thirty", "Forty"]
    
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
    
    def calculate_score(self):
    
        try:
            score_diff = self.player1.score - self.player2.score

            if self.player1.score >= 3 and self.player2.score >= 3 and score_diff == 0:
                return "Deuce" 
            
            elif (self.player1.score >= 5 or self.player2.score >= 5) and abs(score_diff) > 2:
                logger.error("Invalid Score")
                raise ValueError("Invalid Score")
                        
            elif self.player1.score >= 4 or self.player2.score >= 4:
                if score_diff == 0:
                    return "Deuce"
                elif score_diff == 1:
                    return f"Advantage for {self.player1.name}"
                elif score_diff == -1:
                    return f"Advantage for {self.player2.name}"
                elif score_diff >= 2:
                    return f"Win for {self.player1.name}"
                elif score_diff <= -2:
                    return f"Win for {self.player2.name}"
                
            else:
                return f"{self.score_map[self.player1.score]}-{self.score_map[self.player2.score]}"
            
        except ValueError as e:
            logger.error(e)
            raise ValueError(e)

        except Exception as e:
            logger.error(e)
            raise Exception(f"Unexpected error: {e}")