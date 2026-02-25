from project_backend.db.db import get_connection

def get_interest_score(user_id: int, role_name: str):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT AVG(interest_score)
        FROM user_interests
        WHERE user_id = %s AND domain = %s
    """, (user_id, role_name))

    row = cur.fetchone()

    cur.close()
    conn.close()

    return row[0] if row and row[0] is not None else 0
