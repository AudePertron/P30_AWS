import psycopg2

class DataAccess :

    @classmethod 
    def connexion(cls):
        cls.conn = psycopg2.connect(host = 'brief30.cnclzdom1btx.eu-west-3.rds.amazonaws.com', user = 'Copinette', password = 'coucou29', port = '5432', database = 'exercises')
        cls.db = cls.conn.cursor()

    @classmethod
    def deconnexion(cls):
        cls.conn.close()
        cls.db.close()

    #endpoint one
    @classmethod
    def get_facilities(cls):
        cls.connexion()
        cls.db.execute(f"select * from cd.facilities")
        result = cls.db.fetchall()
        cls.deconnexion()
        return list(result)
        
    
    @classmethod
    def get_cost(cls, cost):
        cls.connexion()
        cls.db.execute(f"select * from cd.facilities where membercost>{cost}")
        result = cls.db.fetchall()
        cls.deconnexion()
        return list(result)

    @classmethod
    def one_facility(cls, facility):
        cls.connexion()
        cls.db.execute(f"select * from cd.facilities where name like '%{facility}%'")
        result = cls.db.fetchall()
        cls.deconnexion()
        return list(result)