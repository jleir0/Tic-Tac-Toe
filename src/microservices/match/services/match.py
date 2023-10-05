from models import db, Match

m_winners = [[[1,1,1],[0,0,0],[0,0,0]],
             [[0,0,0],[1,1,1],[0,0,0]],
             [[0,0,0],[0,0,0],[1,1,1]],
             [[1,0,0],[1,0,0],[1,0,0]],
             [[0,1,0],[0,1,0],[0,1,0]],
             [[0,0,1],[0,0,1],[0,0,1]],
             [[1,0,0],[0,1,0],[0,0,1]],
             [[1,0,0],[0,1,0],[1,0,0]]]

matriz_cero = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

class MatchService:

    @staticmethod
    def ocupiedSquares(match):        
        matriz_suma = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        for i in range(3):
            for j in range(3):
                matriz_suma[i][j] = match["Xmoves"][i][j] + match["Omoves"][i][j]
                if matriz_suma[i][j] > 1:
                    return(400, "You have introduced an invalid move.")
                
        return matriz_suma

    @staticmethod
    def checkMove(match, user, x, y):          

        if match[user][x][y] == 1:
            return(400, "You have introduced an invalid move.")   
        
        m_available = MatchService.ocupiedSquares(match)
        
        if m_available[x][y] == 1:
            return(400, "You have introduced an invalid move.")   

        match[user][x][y] = 1
        try:
            db.session.commit()
        except Exception as e:
            return(500, f"An error occurred: {str(e)}")

        if match[user] in m_winners:
            return True
        
        return False
    
    @staticmethod
    def newIterator(occupiedSquares, x, y):
        if y > 0:
            if occupiedSquares[x][y-1] == 0:
                return x, y-1
        if y < 2:
            if occupiedSquares[x][y+1] == 0:
                return x, y+1
        if x > 0:
            if occupiedSquares[x-1][y] == 0:
                return x-1, y  
        if x < 2:     
            if occupiedSquares[x+1][y] == 0:
                return x+1, y
    
    @staticmethod
    def move(data):
        matchId = data['matchId']
        playerId = data['playerId']
        square_x = data['square']['x']
        square_y = data['square']['y']

        try:
            match = Match.query.filter_by(matchId=matchId)
        except Exception as e:
            return(500, f"An error occurred: {str(e)}")
        if match is None:
            return(404, f"Match {matchId} not found.")
        
        if match["status"] == "playing":

            if square_x > 3 or square_x < 1:
                return(400, "X just can be 1, 2 or 3.")
            if square_y > 3 or square_y < 1:
                return(400, "Y just can be 1, 2 or 3.")
            
            square_x =- 1
            square_y =- 1

            user = None
            pc = None

            if playerId == "X" or playerId == "x":
                user = "Xmoves"
                pc = "Omoves"
            elif playerId == "O" or playerId == "o":
                user = "Omoves"
                pc = "Xmoves"
            else:
                return(400, "You enter a wrong player_id, only X or O are valid.")

            if match["playerId"] != playerId:
                return(400,"You are playing this match as " + match["playerId"])

            m_available = MatchService.ocupiedSquares(match)
            if user == "Omoves" and m_available == matriz_cero:
                pcMove = MatchService.checkMove(match, pc, 2, 2)

            userMove = MatchService.checkMove(match, user, square_x, square_y)

            if userMove:
                match["status"] = "won"
                try:
                    db.session.commit()
                except Exception as e:
                    return(500, f"An error occurred: {str(e)}")
                return "Congratulations, you won", 200
            else:
                l_available = MatchService.ocupiedSquares(match)

                x, y = MatchService.newIterator(l_available, square_x, square_y)

                pcMove = MatchService.checkMove(match, pc, x, y)

                if pcMove:
                    match["status"] = "lost"
                    try:
                        db.session.commit()
                    except Exception as e:
                        return(500, f"An error occurred: {str(e)}")
                    return "Sorry but I won this match.", 200
                else:
                    return "I make my move, now its your turn again.", 200
        else:
            return(400, "This match is finished.")


    @staticmethod
    def status(matchId):
        try:
            match = Match.query.filter_by(matchId=matchId)
        except Exception as e:
            return(500, f"An error occurred: {str(e)}")

        if match is None:
            return(404, f"Match with id {matchId} not found")
        
        m_available = MatchService.ocupiedSquares(match)

        response_data = {
            "matchId": matchId,
            "status": "The match is " + match["status"],
            "next": "X" if match["playerId"] == "O" else "O",
            "overall": m_available,
        }

        return response_data, 200
    
    
    @staticmethod
    def create(matchId):
        response_data = {
            "matchId": matchId
        }

        new_match = Match(matchId=matchId)
        try:
            db.session.add(new_match)
            db.session.commit()
        except Exception as e:
            return(500, f"An error occurred: {str(e)}")

        return response_data, 200
    