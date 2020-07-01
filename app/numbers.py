from .database import DB

class Numbers():
    def __init__(self, id, number1, number2, string):
        self.id = id
        self.number1 = number1
        self.number2 = number2
        self.string = string

    
    def create(self):
        with DB() as db:
            values = (self.number1, self.number2, self.string)

            db.execute('INSERT INTO numbers(number1, number2, string) VALUES(?, ?, ?)', values)

            return self


    @staticmethod
    def get_last_record():
        with DB() as db:

            row = db.execute('SELECT * FROM numbers ORDER BY id DESC LIMIT 1').fetchone()

            return Numbers(*row)