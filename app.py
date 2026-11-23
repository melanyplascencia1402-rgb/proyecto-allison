from flask import Flask, request, flash, redirect, url_for, send_from_directory, render_template_string

app = Flask(__name__)
app.secret_key = "cecytej-30-aniversario"

# =========================================================
# CSS
# =========================================================
CSS = """
:root {
    --verde: #0b5d3b;
    --verde-oscuro: #14532d;
    --dorado: #c9a227;
    --fondo: #f7f7f7;
    --texto: #222;
}
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
    font-family: 'Segoe UI', Arial, sans-serif;
    background: var(--fondo);
    color: var(--texto);
    line-height: 1.6;
}
.topbar {
    background: var(--verde);
    color: #fff;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 12px 24px;
    border-bottom: 4px solid var(--dorado);
    flex-wrap: wrap;
}
.brand { display: flex; align-items: center; gap: 15px; }
.logo-img {
    height: 55px;
    width: auto;
    background: #fff;
    padding: 5px;
    border-radius: 6px;
    border: 2px solid var(--dorado);
}
.aniversario {
    border: 2px solid var(--dorado);
    color: var(--dorado);
    padding: 4px 10px;
    border-radius: 50px;
    font-weight: bold;
    font-size: .9rem;
}
nav a {
    color: #fff;
    text-decoration: none;
    margin-left: 18px;
    font-weight: 500;
    transition: color .2s;
}
nav a:hover { color: var(--dorado); }
main { max-width: 1100px; margin: 30px auto; padding: 0 20px; }
.card {
    background: #fff;
    padding: 30px;
    border-radius: 12px;
    box-shadow: 0 4px 14px rgba(0,0,0,.08);
    border-top: 5px solid var(--dorado);
}
.card h2 {
    color: var(--verde);
    margin-bottom: 12px;
    border-bottom: 2px solid var(--dorado);
    padding-bottom: 6px;
}
.card h3 { color: var(--verde); margin: 22px 0 10px; }
.hero {
    background: linear-gradient(135deg, var(--verde), #1f7a5c);
    color: #fff;
    text-align: center;
    padding: 50px 30px;
    border-radius: 14px;
    border: 3px solid var(--dorado);
}
.hero h1 { font-size: 1.8rem; margin: 15px 0; color: var(--dorado); }
.subt { margin-bottom: 20px; }
.foto-portada {
    width: 100%;
    max-width: 550px;
    border-radius: 12px;
    border: 3px solid var(--dorado);
    margin: 15px auto;
    display: block;
}
.emblema30 {
    height: 70px;
    width: auto;
    display: block;
    margin: 10px auto;
}
.menu-botones {
    display: flex; flex-wrap: wrap; gap: 12px;
    justify-content: center; margin-top: 25px;
}
.btn {
    background: var(--dorado);
    color: var(--verde);
    padding: 12px 22px;
    border-radius: 8px;
    text-decoration: none;
    font-weight: bold;
    border: none;
    cursor: pointer;
    transition: transform .2s, background .2s;
}
.btn:hover { background: #e0b730; transform: scale(1.05); }
.timeline { position: relative; margin: 20px 0; padding-left: 25px; border-left: 3px solid var(--dorado); }
.tl-item { margin-bottom: 25px; position: relative; }
.tl-item::before {
    content: "";
    position: absolute;
    left: -34px; top: 4px;
    width: 15px; height: 15px;
    background: var(--dorado);
    border-radius: 50%;
    border: 3px solid var(--verde);
}
.tl-item img {
    width: 100%;
    max-width: 250px;
    border-radius: 8px;
    border: 2px solid var(--dorado);
    margin-top: 8px;
}
.fecha { font-weight: bold; color: var(--verde); font-size: 1.1rem; }
.grid2 { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 18px; margin: 15px 0; }
.grid3 { display: grid; grid-template-columns: repeat(auto-fit, minmax(230px, 1fr)); gap: 18px; margin: 15px 0; }
.grid-categorias { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px; }
.bloque {
    background: #fafafa;
    border-left: 5px solid var(--dorado);
    padding: 18px;
    border-radius: 10px;
}
.bloque h4 { color: var(--verde); margin-bottom: 6px; }
.bloque img {
    width: 100%;
    border-radius: 10px;
    border: 2px solid var(--dorado);
    margin-bottom: 8px;
}
.testimonio {
    background: #fafafa;
    border-left: 5px solid var(--dorado);
    border-radius: 10px;
    padding: 15px;
    text-align: center;
    box-shadow: 0 2px 8px rgba(0,0,0,.06);
}
.testimonio img {
    width: 80px; height: 80px;
    border-radius: 50%;
    object-fit: cover;
    border: 3px solid var(--dorado);
    margin-bottom: 8px;
}
.testimonio h4 { color: var(--verde); }
.testimonio span { font-size: .85rem; color: #666; display: block; margin-bottom: 8px; }
.cat {
    background: var(--verde);
    color: #fff;
    padding: 18px;
    border-radius: 10px;
    border-bottom: 4px solid var(--dorado);
    text-align: center;
}
.cat img {
    width: 100%;
    height: 120px;
    object-fit: cover;
    border-radius: 8px;
    border: 2px solid var(--dorado);
    margin-bottom: 8px;
}
.cat h4 { color: var(--dorado); margin-bottom: 6px; }
.evento {
    background: #fafafa;
    border-radius: 10px;
    padding: 15px;
    border-top: 4px solid var(--dorado);
    box-shadow: 0 2px 8px rgba(0,0,0,.06);
}
.evento img {
    width: 100%;
    height: 140px;
    object-fit: cover;
    border-radius: 8px;
    border: 2px solid var(--dorado);
    margin-bottom: 10px;
}
.evento h4 { color: var(--verde); margin-bottom: 6px; }
.form-futuro { display: flex; flex-direction: column; gap: 12px; max-width: 500px; margin-top: 15px; }
.form-futuro input, .form-futuro textarea {
    padding: 12px;
    border: 2px solid #ddd;
    border-radius: 8px;
    font-family: inherit;
    font-size: 1rem;
}
.form-futuro input:focus, .form-futuro textarea:focus {
    border-color: var(--dorado);
    outline: none;
}
.form-futuro textarea { min-height: 100px; resize: vertical; }
.frase-final {
    margin-top: 30px;
    font-style: italic;
    text-align: center;
    color: var(--verde);
    font-size: 1.15rem;
    padding: 15px;
    border-top: 2px dashed var(--dorado);
    border-bottom: 2px dashed var(--dorado);
}
.entrevista {
    background: #fafafa;
    border-left: 5px solid var(--dorado);
    border-radius: 10px;
    padding: 20px;
    margin: 15px 0;
    box-shadow: 0 2px 8px rgba(0,0,0,.06);
}
.entrevista h3 {
    color: var(--verde);
    margin-bottom: 10px;
    border-bottom: 1px solid var(--dorado);
    padding-bottom: 5px;
}
.entrevista .pregunta {
    font-weight: bold;
    color: var(--verde);
    margin-top: 12px;
}
.entrevista .respuesta {
    margin-left: 20px;
    margin-bottom: 10px;
}
.flash {
    background: #fff8e1;
    border-left: 5px solid var(--dorado);
    padding: 12px 18px;
    margin-bottom: 15px;
    border-radius: 8px;
    color: var(--verde);
    font-weight: 600;
}
footer {
    background: var(--verde);
    color: #fff;
    text-align: center;
    padding: 18px;
    margin-top: 40px;
    border-top: 4px solid var(--dorado);
    font-size: .9rem;
}
@media (max-width: 700px) {
    .topbar { flex-direction: column; gap: 10px; }
    nav a { margin: 0 8px; }
    .hero h1 { font-size: 1.3rem; }
}
"""

BASE = """
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>CECyTEJ Plantel 08 - 30 Aniversario</title>
<link rel="stylesheet" href="/static/style.css">
</head>
<body>

<header class="topbar">
    <div class="brand">
        <img src="https://tse2.mm.bing.net/th/id/OIP.-SZ2OwP3GNIBEANAq2Pi0QHaHa?r=0&rs=1&pid=ImgDetMain&o=7&rm=3" alt="Logo CECyTEJ" class="logo-img">
        <div class="aniversario">30 Años</div>
    </div>
    <nav>
        <a href="/">Inicio</a>
        <a href="/historia">Historia</a>
        <a href="/testimonios">Testimonios</a>
        <a href="/orgullo">Orgullo</a>
        <a href="/celebremos">Celebremos</a>
        <a href="/futuro">Futuro</a>
        <a href="/entrevista">Entrevista</a>
    </nav>
</header>

<main>
    {% with msgs = get_flashed_messages() %}
        {% if msgs %}
            {% for m in msgs %}
                <div class="flash">{{ m }}</div>
            {% endfor %}
        {% endif %}
    {% endwith %}
    {% block content %}{% endblock %}
</main>

<footer>
    <p>© 2026 CECyTEJ Plantel 08 Ixtlahuacán del Río · 30 años formando generaciones, construyendo oportunidades</p>
</footer>

</body>
</html>
"""

@app.route("/static/style.css")
def serve_css():
    return app.response_class(CSS, mimetype="text/css")


@app.route("/static/img/<path:filename>")
def serve_img(filename):
    return send_from_directory("static/img", filename)


@app.route("/")
def inicio():
    content = """
    <section class="hero">
        <img src="https://th.bing.com/th/id/OIP.ALVuYoNiMXR_6LqKFiImAQHaHa?w=177&h=180&c=7&r=0&o=7&pid=1.7&rm=3" alt="Emblema 30 años" class="emblema30">
        <h1>30 años formando generaciones, construyendo oportunidades</h1>
        <p class="subt">Bienvenido a la página conmemorativa del <strong>CECyTEJ Plantel 08 Ixtlahuacán del Río</strong>.</p>

        <img src="https://cdn.phototourl.com/member/2026-11-22-4f8d4be2-da1c-460f-aed9-84c27977f467.jpg" alt="Foto del Plantel 08" class="foto-portada">

        <div class="menu-botones">
            <a href="/historia" class="btn">Nuestra Historia</a>
            <a href="/testimonios" class="btn">Testimonios</a>
            <a href="/orgullo" class="btn">Orgullo</a>
            <a href="/celebremos" class="btn">Celebraciones</a>
            <a href="/futuro" class="btn">Futuro</a>
        </div>
    </section>
    """
    return render_template_string(BASE.replace("{% block content %}{% endblock %}", content))


@app.route("/historia")
def historia():
    content = """
    <section class="card">
        <h2>Nuestra Historia · Tres décadas de transformación</h2>
        <p>Desde el año 2000, el Plantel 08 ha formado a miles de jóvenes de Ixtlahuacán del Río. Tras su inauguración, el plantel ha demostrado una buena evolución a lo largo de los años, tanto en las instalaciones como en las carreras que ofrece.</p>

        <h3>Línea del tiempo</h3>
        <div class="timeline">
            <div class="tl-item">
                <span class="fecha">1995</span>
                <p>Fundación del plantel con la primera generación.</p>
                <img src="https://cdn.phototourl.com/member/2026-11-22-9d392f87-8f3b-4399-91ea-875c82ac31c1.jpg" alt="Fundación 1995">
            </div>
            <div class="tl-item">
                <span class="fecha">2005</span>
                <p>Logo del plantel.</p>
                <img src="https://1.bp.blogspot.com/-nJrOdHqawBE/TguA8gmpP9I/AAAAAAAAAe4/jwQVh2mo8aw/s320/Logo%2B300.bmp" alt="Logo del plantel">
            </div>
            <div class="tl-item">
                <span class="fecha">2005</span>
                <p>Ampliación de instalaciones y laboratorios.</p>
                <img src="https://cdn.phototourl.com/member/2026-11-22-7c6f642c-3863-4ac3-86bb-5cabb13713b0.jpg" alt="Ampliación 2005">
            </div>
            <div class="tl-item">
                <span class="fecha">2015</span>
                <p>Cambio en el color y logo del plantel.</p>
                <img src="https://cdn.phototourl.com/member/2026-11-22-5c0628f2-0003-499c-ad20-523c7b213c60.jpg" alt="Cambio de logo 2015">
            </div>
            <div class="tl-item">
                <span class="fecha">2026</span>
                <p>Mejoras en el plantel. Se incrementó una nueva escalera.</p>
                <img src="https://cdn.phototourl.com/member/2026-11-22-08310635-041e-42e1-b15f-8da56c84749e.jpg" alt="Mejoras 2026">
            </div>
            <div class="tl-item">
                <span class="fecha">2026</span>
                <p>30 años formando generaciones.</p>
                <img src="https://cdn.phototourl.com/member/2026-11-22-4fdb8454-d00e-4c94-a6f4-264bde768194.jpg" alt="30 Aniversario 2026">
            </div>
        </div>

        <h3>Antes y ahora</h3>
        <div class="grid2">
            <div class="bloque">
                <img src="https://cdn.phototourl.com/member/2026-11-22-0c7c3618-9bea-43e7-9f34-24c5d6df0a52.jpg" alt="Antes">
                <h4>Antes</h4>
                <p>El plantel contaba con otro logo y el color era azul, con dos carreras: Informática y Electromecánica.</p>
            </div>
            <div class="bloque">
                <img src="https://mexinternados.com/wp-content/uploads/cecytej-08-ixtlahuacan-del-rio-escuela-ixtlahuacan-del-rio.webp" alt="Ahora">
                <h4>Ahora</h4>
                <p>Cuenta con más áreas verdes, nuevos logos y la incorporación de la Programación.</p>
            </div>
        </div>

        <h3>Mejoras</h3>
        <ul>
            <li>Se plantaron árboles y se cuidan más las áreas verdes.</li>
            <li>Se proporcionó más maquinaria a los de Electromecánica y se añadieron salones y domos.</li>
            <li>Docentes certificados.</li>
        </ul>

        <h3>Eventos</h3>
        <p>Desfiles cívicos, torneos deportivos y graduaciones que marcaron cada generación.</p>
    </section>
    """
    return render_template_string(BASE.replace("{% block content %}{% endblock %}", content))


@app.route("/testimonios")
def testimonios():
    content = """
    <section class="card">
        <h2>Testimonios</h2>
        <p>Testimonios de quienes han sido parte de nuestra historia.</p>

        <div class="grid3">
            <div class="testimonio">
                <img src="https://via.placeholder.com/80x80/0b5d3b/ffffff?text=M" alt="María López">
                <h4>María López</h4>
                <span>Exalumna · Generación 2024</span>
                <p>"El CECyTEJ me proporcionó una carrera técnica."</p>
            </div>
            <div class="testimonio">
                <img src="https://via.placeholder.com/80x80/0b5d3b/ffffff?text=J" alt="Juan Ramírez">
                <h4>Juan Ramírez</h4>
                <span>Exalumno · Generación 2023</span>
                <p>"Los conocimientos adquiridos en la escuela me han sido útiles en algunas situaciones de mi vida."</p>
            </div>
            <div class="testimonio">
                <img src="https://via.placeholder.com/80x80/0b5d3b/ffffff?text=V" alt="Valeria García">
                <h4>Valeria García</h4>
                <span>Alumna actual · 4° semestre</span>
                <p>"Aquí encontré mi vocación en programación."</p>
            </div>
            <div class="testimonio">
                <img src="https://via.placeholder.com/80x80/0b5d3b/ffffff?text=P" alt="Ing. Pedro Sánchez">
                <h4>Ing. Pedro Sánchez</h4>
                <span>Exalumno · Generación 2023</span>
                <p>"Fue muy agradable pasar mis años de preparatoria en CECyTEJ; pasé muy buenos momentos y agradezco todas las oportunidades que me dio el plantel."</p>
            </div>
        </div>

        <h3>Formación integral</h3>
        <p>Nuestros egresados destacan no solo en lo académico, sino en valores, deporte y cultura.</p>
    </section>
    """
    return render_template_string(BASE.replace("{% block content %}{% endblock %}", content))


@app.route("/orgullo")
def orgullo():
    content = """
    <section class="card">
        <h2>Orgullo CECyTEJ · Logros, talento y proyectos</h2>

        <h3>Galería por categorías</h3>
        <div class="grid-categorias">
            <div class="cat">
                <img src="data:image/webp;base64,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" alt="Tecnología">
                <h4>Tecnología</h4>
                <p>Los estudiantes de programación crean aplicaciones web.</p>
            </div>
        
            <div class="cat">
                <img src="https://th.bing.com/th/id/OIP.leZn7o7r9P4LKMX2K9TIygHaE7?w=216&h=180&c=7&r=0&o=7&pid=1.7&rm=3" alt="Deportes">
                <h4>Deportes</h4>
                <p>El plantel cuenta con varios trofeos ganados por sus estudiantes.</p>
            </div>
            <div class="cat">
                <img src="https://th.bing.com/th/id/OIP.C1UoB9_uAoFRA_5qfhoh_QHaFq?w=222&h=180&c=7&r=0&o=7&pid=1.7&rm=3" alt="Cultura">
                <h4>Cultura</h4>
                <p>Se ha implementado la danza folclórica en el CECyTEJ.</p>
            </div>
            <div class="cat">
                <img src="https://www.geocities.ws/cecytej08ixtlahuacan/estante_trofeos.jpg" alt="Logros académicos">
                <h4>Logros académicos</h4>
                <p>En 27 años, el plantel ha ganado innumerables trofeos.</p>
            </div>
        </div>

        <h3>Proyectos destacados</h3>
        <ul>
            <li>Aplicaciones web de Programación.</li>
            <li>Proyectos de los estudiantes de Electromecánica.</li>
            <li>Ferias de ciencia y torneos deportivos.</li>
        </ul>
    </section>
    """
    return render_template_string(BASE.replace("{% block content %}{% endblock %}", content))


@app.route("/celebremos")
def celebremos():
    content = """
    <section class="card">
        <h2>Celebremos juntos · 30 años de orgullo y tradición</h2>
        <p>Actividades conmemorativas.</p>

        <div class="grid2">
            <div class="evento">
                <img src="https://tse1.mm.bing.net/th/id/OIP.SfYkl_uLLn9z2U_mkwgU3QHaFj?r=0&rs=1&pid=ImgDetMain&o=7&rm=3" alt="Expo-ciencia">
                <h4>Expo-ciencia</h4>
                <p>Exhibición de proyectos estudiantiles.</p>
            </div>
            <div class="evento">
                <img src="https://th.bing.com/th/id/OIP.pppyl1R_cHrNaeTrk-VtTwHaE8?w=263&h=180&c=7&r=0&o=7&pid=1.7&rm=3" alt="Torneo Deportivo">
                <h4>Torneo Deportivo</h4>
                <p>Voleibol varonil y femenil, bastoneras, y futbol varonil y femenil.</p>
            </div>
            <div class="evento">
                <img src="https://th.bing.com/th/id/OIP.B-bwqvyRccYgnYyhEjY2mQHaEt?w=268&h=180&c=7&r=0&o=7&pid=1.7&rm=3" alt="Noche Cultural">
                <h4>Cultura</h4>
                <p>Danza folclórica, altar de muertos y desfiles.</p>
            </div>
        </div>
    </section>
    """
    return render_template_string(BASE.replace("{% block content %}{% endblock %}", content))


@app.route("/futuro", methods=["GET", "POST"])
def futuro():
    if request.method == "POST":
        nombre = request.form.get("nombre", "").strip()
        generacion = request.form.get("generacion", "").strip()
        mensaje = request.form.get("mensaje", "").strip()
        if nombre and generacion and mensaje:
            flash(f"¡Gracias {nombre} de la generación {generacion}! Tu mensaje para el futuro fue enviado.")
        else:
            flash("Por favor completa todos los campos.")
        return redirect(url_for("futuro"))

    content = """
    <section class="card">
        <h2>Nuestro futuro · Los próximos 30 años</h2>

        <h3>Metas y mejoras</h3>
        <ul>
            <li>Mejores computadoras en los laboratorios.</li>
            <li>Mejora de la maquinaria en Electromecánica.</li>
            <li>Uso de las habilidades aprendidas en carrera para crear un cambio social y ambiental.</li>
        </ul>

        <h3>Compromiso ambiental y comunitario</h3>
        <p>Reforestación, reciclaje y vinculación con la comunidad de Ixtlahuacán del Río.</p>

        <h3>Mi mensaje para el futuro</h3>
        <form method="POST" class="form-futuro">
            <input type="text" name="nombre" placeholder="Tu nombre" required>
            <input type="text" name="generacion" placeholder="Tu generación (ej. 2025)" required>
            <textarea name="mensaje" placeholder="Escribe tu mensaje para el futuro..." required></textarea>
            <button type="submit" class="btn">Enviar mi mensaje</button>
        </form>

        <p class="frase-final">«30 años formando generaciones, construyendo oportunidades»</p>
    </section>
    """
    return render_template_string(BASE.replace("{% block content %}{% endblock %}", content))


@app.route("/entrevista")
def entrevista():
    content = """
    <section class="card">
        <h2>Entrevista</h2>
        <p>Entrevista realizada con el fin de conocer la experiencia de los exalumnos del CECyTEJ.</p>

        <div class="entrevista">
            <h3>Entrevista a Daniela Lynette</h3>
            <p class="pregunta">1. ¿Por qué elegiste el CECyTEJ?</p>
            <p class="respuesta">"Elegí el CECyTEJ por su nivel académico."</p>

            <p class="pregunta">2. ¿Consideras que los conocimientos adquiridos te ayudaron en la vida?</p>
            <p class="respuesta">"Creo que siempre puedes poner en práctica algún conocimiento; en mi caso, sí fue de ayuda."</p>

            <p class="pregunta">3. ¿Qué consejo le darías a los que están estudiando en el CECyTEJ?</p>
            <p class="respuesta">"Que disfruten sus 3 años, son los mejores 3 años que tendrán; aprovechen cada una de las actividades que se les ofrezcan y, sobre todo, expriman el conocimiento de sus maestros, siempre tienen buenos consejos o buenas enseñanzas que les servirían en un futuro."</p>

            <p class="pregunta">4. ¿Qué es lo que más te enorgullece de haber estudiado aquí?</p>
            <p class="respuesta">"Ver cómo, a pesar de mis pequeños momentos de estrés, no solo terminé mi prepa con buen promedio, sino que también logré terminar mi carrera técnica en programación."</p>
        </div>

        <div class="entrevista">
            <h3>Entrevista a Adriana Luna</h3>
            <p class="pregunta">1. ¿Por qué elegiste el CECyTEJ?</p>
            <p class="respuesta">"Elegí el CECyTEJ porque me pareció una buena escuela para continuar mis estudios, aprender cosas nuevas y prepararme para tener un buen futuro."</p>

            <p class="pregunta">2. ¿Consideras que los conocimientos adquiridos te ayudaron en la vida?</p>
            <p class="respuesta">"Sí, porque he aprendido muchas cosas que me sirven en mi vida diaria, tanto en la escuela como fuera de ella."</p>

            <p class="pregunta">3. ¿Qué consejo le darías a los que están estudiando en el CECyTEJ?</p>
            <p class="respuesta">"Les aconsejaría que le echen muchas ganas, que no se rindan, que aprovechen sus estudios y que siempre luchen por cumplir sus metas."</p>
        </div>

        <div class="entrevista">
            <h3>Entrevista a Sergio</h3>
            <p class="pregunta">1. ¿Por qué elegiste el CECyTEJ?</p>
            <p class="respuesta">"Elegí el CECyTEJ porque me gustó que, además de la prepa, sales con una carrera técnica, no solo con el certificado."</p>

            <p class="pregunta">2. ¿Consideras que los conocimientos adquiridos te ayudaron en la vida?</p>
            <p class="respuesta">"Sí, todo lo que aprendí me ha servido. En mi caso, lo de programación me ayudó a entender mejor las cosas de la escuela y también fuera de ella."</p>

            <p class="pregunta">3. ¿Qué consejo le darías a los que están estudiando en el CECyTEJ?</p>
            <p class="respuesta">"Que le echen muchas ganas, que no se rindan aunque a veces se sienta pesado, que disfruten sus 3 años y que aprovechen a sus maestros, porque sus consejos sí les van a servir en un futuro."</p>

            <p class="pregunta">4. ¿Qué es lo que más te enorgullece de haber estudiado aquí?</p>
            <p class="respuesta">"Ver cómo, a pesar de que hubo días de estrés y de querer dejar todo, sí pude terminar mi prepa con buen promedio y también terminar mi carrera técnica."</p>
        </div>
    </section>
    """
    return render_template_string(BASE.replace("{% block content %}{% endblock %}", content))


if __name__ == "__main__":
    app.run(debug=True)