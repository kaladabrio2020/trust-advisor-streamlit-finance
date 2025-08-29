import streamlit as st
from streamlit_monaco import st_monaco
import io
import sys
import contextlib

st.set_page_config(page_title="Code Editor com Autocomplete", layout="wide")

st.title("💻 Editor de Código com Autocomplete + Execução")

# Editor Monaco
code = st_monaco(
    value="""# Exemplo inicial
def soma(a, b):
    return a + b

print("Resultado:", soma(2, 3))""",
    language="python",
    theme="vs-dark",
    height="400px",
)

# Botão para rodar código
if st.button("▶️ Executar Código"):
    output = io.StringIO()
    try:
        # Captura stdout e stderr
        with contextlib.redirect_stdout(output), contextlib.redirect_stderr(output):
            exec(code, globals())
    except Exception as e:
        st.error(f"Erro ao executar:\n{e}")
    finally:
        resultado = output.getvalue()
        if resultado.strip():
            st.success("### Saída do programa:")
            st.code(resultado)
        else:
            st.info("⚠️ Nenhuma saída gerada.")
