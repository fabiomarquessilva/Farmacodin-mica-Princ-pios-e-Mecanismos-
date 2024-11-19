
import streamlit as st
import csv
from datetime import datetime

# Configuração inicial do aplicativo
st.set_page_config(page_title="Farmacodinâmica: Princípios e Mecanismos", layout="wide")

# Senha para acessar o quiz
PASSWORD = "farmacodinamica2024"
CSV_FILE = "pharmacodynamics_responses.csv"

# Função para verificar a senha
def check_password():
    st.markdown("<h1 style='text-align: center; color: #4CAF50;'>Farmacodinâmica: Princípios e Mecanismos</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: #FF5722;'>Digite a senha para acessar o quiz</h3>", unsafe_allow_html=True)

    password = st.text_input("Senha", type="password")
    if st.button("Entrar"):
        if password == PASSWORD:
            st.session_state["access_granted"] = True
            st.experimental_rerun()
        else:
            st.error("Senha incorreta. Tente novamente.")

# Função para salvar respostas no CSV
def save_responses_to_csv(responses, score, correct_answers, wrong_answers):
    with open(CSV_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        if file.tell() == 0:  # Verifica se o arquivo está vazio para adicionar cabeçalho
            writer.writerow(["Data/Hora", "Pergunta", "Resposta Escolhida", "Resposta Correta", "Pontuação", "Corretas", "Erradas"])
        for response in responses:
            writer.writerow([
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                response["question"],
                response["selected"],
                response["correct"],
                score,
                correct_answers,
                wrong_answers
            ])

# Verificar se o acesso foi concedido
if "access_granted" not in st.session_state or not st.session_state["access_granted"]:
    check_password()
else:
    # Título do jogo
    st.markdown("<h1 style='text-align: center; color: #4CAF50;'>Farmacodinâmica: Princípios e Mecanismos</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: #FF5722;'>Teste seus conhecimentos sobre princípios e mecanismos de ação de fármacos!</h3>", unsafe_allow_html=True)

    # Introdução
    st.write("Bem-vindo ao Quiz de Farmacodinâmica! Escolha a alternativa correta para cada pergunta e clique em **Finalizar** ao final para ver seu desempenho.")

    # Lista de perguntas sobre farmacodinâmica
    questions = [
        {"question": "Qual é a principal característica de um agonista total?",
         "options": ["a) Ocupa o receptor, mas não ativa a sinalização celular", 
                     "b) Ativa o receptor para gerar uma resposta máxima", 
                     "c) Compete pelo receptor, mas não gera resposta", 
                     "d) Inativa o receptor completamente", 
                     "e) Diminui a afinidade do receptor pelo ligante"],
         "answer": "b) Ativa o receptor para gerar uma resposta máxima"},
        {"question": "O que indica o índice terapêutico de um fármaco?",
         "options": ["a) A quantidade máxima de fármaco administrada sem toxicidade", 
                     "b) A relação entre a dose eficaz e a dose tóxica", 
                     "c) A potência relativa entre dois fármacos", 
                     "d) A capacidade do fármaco em atingir o receptor-alvo", 
                     "e) A dose mínima necessária para gerar resposta terapêutica"],
         "answer": "b) A relação entre a dose eficaz e a dose tóxica"},
        {"question": "Qual tipo de receptor está envolvido em canais iônicos rápidos?",
         "options": ["a) Receptores Metabotrópicos", 
                     "b) Receptores Ionotrópicos", 
                     "c) Receptores Tirosina Quinase", 
                     "d) Receptores Nucleares", 
                     "e) Receptores Acoplados à Proteína G"],
         "answer": "b) Receptores Ionotrópicos"},
        {"question": "O que caracteriza a taquifilaxia?",
         "options": ["a) Aumento progressivo da resposta ao longo do tempo", 
                     "b) Perda rápida da eficácia de um fármaco", 
                     "c) Necessidade de doses crescentes para obter o mesmo efeito", 
                     "d) Ativação excessiva dos receptores", 
                     "e) Redução na eliminação do fármaco"],
         "answer": "b) Perda rápida da eficácia de um fármaco"},
        {"question": "Qual é a função de um antagonista competitivo?",
         "options": ["a) Estimula a ativação do receptor", 
                     "b) Bloqueia o receptor irreversivelmente", 
                     "c) Compete pelo receptor sem ativá-lo", 
                     "d) Diminui a afinidade do receptor pelo ligante", 
                     "e) Inativa o receptor completamente"],
         "answer": "c) Compete pelo receptor sem ativá-lo"}
    ]

    # Variáveis para armazenar pontuação e respostas do usuário
    correct_answers = 0
    wrong_answers = 0
    user_answers = []
    score = 0

    # Exibição das perguntas
    for i, q in enumerate(questions):
        st.markdown(f"<h4 style='color: #2196F3;'>Pergunta {i+1}: {q['question']}</h4>", unsafe_allow_html=True)
        selected = st.radio("", q["options"], key=i)
        user_answers.append({
            "question": q["question"],
            "selected": selected,
            "correct": q["answer"]
        })

    # Botão para finalizar o quiz
    if st.button("Finalizar Quiz"):
        # Verificar respostas
        for response in user_answers:
            if response["selected"] == response["correct"]:
                correct_answers += 1
            else:
                wrong_answers += 1
        score = correct_answers

        # Salvar as respostas no CSV
        save_responses_to_csv(user_answers, score, correct_answers, wrong_answers)

        # Exibir resultado final
        st.markdown("<hr>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center; color: #4CAF50;'>Resultado Final</h3>", unsafe_allow_html=True)
        st.markdown(f"<h4 style='text-align: center; color: #4CAF50;'>Respostas Corretas: {correct_answers}</h4>", unsafe_allow_html=True)
        st.markdown(f"<h4 style='text-align: center; color: #F44336;'>Respostas Erradas: {wrong_answers}</h4>", unsafe_allow_html=True)

        # Feedback com base no desempenho
        if correct_answers == len(questions):
            st.balloons()
            st.markdown("<h4 style='text-align: center; color: #4CAF50;'>Excelente! Você acertou todas as perguntas!</h4>", unsafe_allow_html=True)
        elif correct_answers > len(questions) // 2:
            st.markdown("<h4 style='text-align: center; color: #FFEB3B;'>Bom trabalho! Continue praticando para melhorar ainda mais.</h4>", unsafe_allow_html=True)
        else:
            st.markdown("<h4 style='text-align: center; color: #F44336;'>Não desista! Revise os conceitos e tente novamente.</h4>", unsafe_allow_html=True)
