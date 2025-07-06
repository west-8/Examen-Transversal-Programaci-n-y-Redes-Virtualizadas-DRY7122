from flask import Flask, request, render_template_string
import sqlite3
import hashlib

app = Flask(__name__)
PORT = 5800

# Conexión y creación de base de datos
conn = sqlite3.connect('usuarios.db', check_same_thread=False)
c = conn.cursor()
c.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        usuario TEXT,
        hash_pass TEXT
    )
''')
conn.commit()

# Función para agregar usuarios si no existen
def agregar_usuario(usuario, password):
    hash_pass = hashlib.sha256(password.encode()).hexdigest()
    c.execute("SELECT * FROM usuarios WHERE usuario=?", (usuario,))
    if not c.fetchone():
        c.execute("INSERT INTO usuarios (usuario, hash_pass) VALUES (?, ?)", (usuario, hash_pass))
        conn.commit()

# Agregar los usuarios iniciales
agregar_usuario('Brian Arancibia', 'TuContraseña1')  # Cambia 'TuContraseña1' por la contraseña que elijas
agregar_usuario('Gabriel Ruminot', 'TuContraseña2')  # Cambia 'TuContraseña2' por la contraseña que elijas

# Sitio web
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        password = request.form['password']
        hash_input = hashlib.sha256(password.encode()).hexdigest()
        
        c.execute("SELECT * FROM usuarios WHERE usuario=? AND hash_pass=?", (usuario, hash_input))
        if c.fetchone():
            return "✅ Login exitoso"
        else:
            return "❌ Credenciales inválidas"
    
    return render_template_string('''
        <h2>Login DRY7122</h2>
        <form method="post">
            Usuario: <input name="usuario"><br>
            Contraseña: <input name="password" type="password"><br>
            <input type="submit" value="Ingresar">
        </form>
    ''')

if __name__ == '__main__':
    app.run(port=PORT, host='0.0.0.0')
