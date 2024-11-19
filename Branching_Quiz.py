
import streamlit as st

# Configuração inicial do aplicativo
st.set_page_config(page_title="Quiz Dinâmico: Farmacodinâmica", layout="wide")

# Variáveis de estado para acompanhar o progresso
if "current_question" not in st.session_state:
    st.session_state.current_question = 0
if "correct_answers" not in st.session_state:
    st.session_state.correct_answers = set()

# Função para processar a resposta e definir a próxima pergunta
def process_answer(question_id, selected_answer, correct_answer):
    if selected_answer == correct_answer:
        st.session_state.correct_answers.add(question_id)
        st.success("Resposta correta!")
        st.session_state.current_question += 1
    else:
        st.error("Resposta incorreta. Tente novamente.")

# Perguntas do quiz
questions = [
    {"id": 1,
     "question": "Qual é a principal característica de um agonista total?",
     "options": ["Ocupa o receptor, mas não ativa a sinalização celular",
                 "Ativa o receptor para gerar uma resposta máxima",
                 "Compete pelo receptor, mas não gera resposta",
                 "Inativa o receptor completamente",
                 "Diminui a afinidade do receptor pelo ligante"],
     "answer": "Ativa o receptor para gerar uma resposta máxima"},
    {"id": 2,
     "question": "Qual tipo de receptor está envolvido em canais iônicos rápidos?",
     "options": ["Receptores Metabotrópicos",
                 "Receptores Ionotrópicos",
                 "Receptores Tirosina Quinase",
                 "Receptores Nucleares",
                 "Receptores Acoplados à Proteína G"],
     "answer": "Receptores Ionotrópicos"},
    {"id": 3,
     "question": "O que caracteriza a taquifilaxia?",
     "options": ["Aumento progressivo da resposta ao longo do tempo",
                 "Perda rápida da eficácia de um fármaco",
                 "Necessidade de doses crescentes para obter o mesmo efeito",
                 "Ativação excessiva dos receptores",
                 "Redução na eliminação do fármaco"],
     "answer": "Perda rápida da eficácia de um fármaco"},
    {"id": 4,
     "question": "Qual é a função de um antagonista competitivo?",
     "options": ["Estimula a ativação do receptor",
                 "Bloqueia o receptor irreversivelmente",
                 "Compete pelo receptor sem ativá-lo",
                 "Diminui a afinidade do receptor pelo ligante",
                 "Inativa o receptor completamente"],
     "answer": "Compete pelo receptor sem ativá-lo"},
    {"id": 5,
     "question": "O que significa eficácia em farmacodinâmica?",
     "options": ["Capacidade do fármaco de alcançar a célula-alvo",
                 "Intensidade máxima de resposta que um fármaco pode produzir",
                 "Relação entre dose eficaz e dose tóxica",
                 "Quantidade mínima necessária para gerar resposta",
                 "Probabilidade de gerar efeitos adversos"],
     "answer": "Intensidade máxima de resposta que um fármaco pode produzir"}
]

# Exibição da pergunta atual
if st.session_state.current_question < len(questions):
    current_q = questions[st.session_state.current_question]
    st.markdown(f"### Pergunta {st.session_state.current_question + 1}: {current_q['question']}")
    selected = st.radio("Escolha uma opção:", current_q["options"], key=current_q["id"])

    if st.button("Responder", key=f"btn_{current_q['id']}"):
        process_answer(current_q["id"], selected, current_q["answer"])
else:
    st.success("Parabéns! Você concluiu o quiz com sucesso!")
    st.balloons()
    st.markdown(f"Você respondeu corretamente a todas as {len(questions)} perguntas.")
