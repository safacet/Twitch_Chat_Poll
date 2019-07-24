import sqlite3

class ChatPoll():
    def connect(self):
        self.con = sqlite3.connect("Chat.db")
        self.cursor = self.con.cursor()
        query1 = "create table if not exists poll(idea TEXT, voters TEXT, votecount INT)"
        self.cursor.execute(query1)
        self.con.commit()
        query2 = "delete from poll"
        self.cursor.execute(query2)
        self.con.commit()
        
    
    def newIdea(self, idea, voter):
        query = "Insert into poll values(?, ?, 1)"
        self.cursor.execute(query, (idea, voter))
        self.con.commit()
    
    def VoteUp(self, result, voter):
        newVoter = result[1]
        newVoter = newVoter + " " + voter
        newVoteCount = result[2]
        newVoteCount += 1
        idea = result[0]
        query = "Update poll set voters = ?, votecount = ? where idea = ? "
        self.cursor.execute(query, (newVoter, newVoteCount, idea))
    
    def control(self, idea, voter):
        query = "Select * from poll where idea = ?"
        self.cursor.execute(query, (idea,))
        result = self.cursor.fetchone()
        if result is None:
            return self.newIdea(idea, voter)
        else:
            voters = result[1]
            voters = voters.split()
            if not voter in voters:
                return self.VoteUp(result, voter)
            else:
                return

    def select(self):
        query = "select * from poll order by votecount DESC"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result