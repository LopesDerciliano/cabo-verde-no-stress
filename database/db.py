import sqlite3, os

os.makedirs("comprovativos", exist_ok=True)
conn = sqlite3.connect("dados.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS utilizadores (
    id INTEGER PRIMARY KEY,
    status TEXT DEFAULT 'pendente',
    idioma TEXT DEFAULT 'pt'
)''')
conn.commit()

def criar_utilizador(user_id):
    cursor.execute("INSERT OR IGNORE INTO utilizadores (id) VALUES (?)", (user_id,))
    conn.commit()

def definir_idioma(user_id, idioma):
    cursor.execute("UPDATE utilizadores SET idioma=? WHERE id=?", (idioma, user_id))
    conn.commit()

def salvar_comprovativo(user_id):
    cursor.execute("UPDATE utilizadores SET status='pendente' WHERE id=?", (user_id,))
    conn.commit()

def aprovar_user(user_id):
    cursor.execute("UPDATE utilizadores SET status='ativo' WHERE id=?", (user_id,))
    conn.commit()

def rejeitar_user(user_id):
    cursor.execute("UPDATE utilizadores SET status='rejeitado' WHERE id=?", (user_id,))
    conn.commit()

def tem_acesso(user_id):
    r = cursor.execute("SELECT status FROM utilizadores WHERE id=?", (user_id,)).fetchone()
    return r and r[0] == "ativo"

def listar_utilizadores():
    return cursor.execute("SELECT id, status FROM utilizadores").fetchall()

def listar_ids_ativos():
    return [r[0] for r in cursor.execute("SELECT id FROM utilizadores WHERE status='ativo'")]
