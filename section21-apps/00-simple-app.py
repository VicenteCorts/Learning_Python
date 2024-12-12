import justpy as jp

def app():
    wp = jp.QuasarPage()

    h1 = jp.QDiv(a=wp, text="Análisis de las Valoraciones de los Cursos", classes="text-h3 text-center q-pa-md")
    p1 = jp.QDiv(a=wp, text="Estos Gráficos representan un análisis de las Valoraciones de los Cursos")

    return wp

jp.justpy(app)