import psycopg2
from psycopg2.extras import RealDictCursor
from config import Config

# Create and return a database connection
def get_db_connection():
    conn = psycopg2.connect(Config.DATABASE_URL)
    return conn

# (User Model) 
class User:
    @staticmethod
    def find_by_email(email):
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute('SELECT * FROM users WHERE email = %s', (email,))
        user = cur.fetchone()
        cur.close()
        conn.close()
        return user

    @staticmethod
    def find_by_id(user_id):
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute('SELECT * FROM users WHERE id = %s', (user_id,))
        user = cur.fetchone()
        cur.close()
        conn.close()
        return user

# (Ticket Model) 
class Ticket:
    @staticmethod
    def create(title, description, user_id):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            'INSERT INTO tickets (title, description, user_id) VALUES (%s, %s, %s)',
            (title, description, user_id)
        )
        conn.commit()
        cur.close()
        conn.close()

    @staticmethod
    def get_all():
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute('''
            SELECT t.*, u.name as user_name 
            FROM tickets t 
            JOIN users u ON t.user_id = u.id 
            ORDER BY t.created_at DESC
        ''')
        tickets = cur.fetchall()
        cur.close()
        conn.close()
        return tickets

    @staticmethod
    def get_by_user(user_id):
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute(
            'SELECT * FROM tickets WHERE user_id = %s ORDER BY created_at DESC',
            (user_id,)
        )
        tickets = cur.fetchall()
        cur.close()
        conn.close()
        return tickets

    @staticmethod
    def find_by_id(ticket_id):
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute('''
            SELECT t.*, u.name as user_name 
            FROM tickets t 
            JOIN users u ON t.user_id = u.id 
            WHERE t.id = %s
        ''', (ticket_id,))
        ticket = cur.fetchone()
        cur.close()
        conn.close()
        return ticket

    @staticmethod
    def close(ticket_id):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            "UPDATE tickets SET status = 'Closed' WHERE id = %s",
            (ticket_id,)
        )
        conn.commit()
        cur.close()
        conn.close()

#  (Reply Model) 
class Reply:
    @staticmethod
    def create(content, ticket_id, user_id):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            'INSERT INTO replies (content, ticket_id, user_id) VALUES (%s, %s, %s)',
            (content, ticket_id, user_id)
        )
        conn.commit()
        cur.close()
        conn.close()

    @staticmethod
    def get_by_ticket(ticket_id):
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute('''
            SELECT r.*, u.name as user_name 
            FROM replies r 
            JOIN users u ON r.user_id = u.id 
            WHERE r.ticket_id = %s 
            ORDER BY r.created_at ASC
        ''', (ticket_id,))
        replies = cur.fetchall()
        cur.close()
        conn.close()
        return replies
