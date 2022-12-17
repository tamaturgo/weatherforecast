import streamlit as st


def app():
    st.title("Sistema de previsão do tempo")
    st.subheader("Insira os dados abaixo para prever o tempo")

    form = st.form("input_values")
    umidade = form.text_input(
        "Umidade",
        value="",
        max_chars=3,
    )
    temperatura = form.text_input(
        "Temperatura",
        value="",
        max_chars=3,
    )
    ventos = form.text_input(
        "Ventos",
        value="",
        max_chars=3,
    )

    submit = form.form_submit_button("Enviar")

    if submit:
        values = app(umidade, temperatura, ventos)
        st.subheader("Descrição: " + values[0])
        st.subheader("Resultado: " + values[1])

