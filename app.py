import streamlit as st
from agents import InterviewSimulator

def main():
    st.title("Simulatore di Colloquio AI")
    
    # Initialize the interview simulator in session state
    if 'simulator' not in st.session_state:
        loading_text = "The Teacher is getting ready..."
        with st.spinner(loading_text):
            st.session_state.simulator = InterviewSimulator()
            st.session_state.interview_started = False
            st.session_state.messages = []

    # Set up the interview if not started yet
    if not st.session_state.interview_started:
        with st.form("setup_form"):
            st.write("### Configura il tuo colloquio")
            
            job_post = st.text_area("Inserisci l'annuncio di lavoro")
            company_backstory = st.text_area("Inserisci informazioni sull'azienda (opzionale)")
            start_button = st.form_submit_button("Inizia il colloquio")
            
            if start_button and job_post:
                st.session_state.simulator.setup_interview(job_post, company_backstory)
                first_question = st.session_state.simulator.generate_first_question()
                st.session_state.messages = [{"role": "assistant", "content": first_question}]
                st.session_state.interview_started = True


    if st.session_state.interview_started:
        for msg in st.session_state.messages:
            if msg["role"] == "assistant":
                st.write("🤖 Intervistatore:", msg["content"])
            else:
                st.write("👤 Tu:", msg["content"])


        with st.form("response_form"):
            user_response = st.text_area("Rispondi alla domanda:")
            submit_button = st.form_submit_button("Invia risposta")
            
            if submit_button and user_response:
                st.session_state.simulator.add_response(user_response)
                next_question = st.session_state.simulator.get_next_question()
                st.session_state.messages.append({"role": "assistant", "content": next_question})
                st.session_state.messages.append({"role": "user", "content": user_response})
                st.rerun()  

        if st.button("Termina colloquio"):
            st.session_state.interview_started = False
            st.session_state.messages = []
            st.rerun()

if __name__ == "__main__":
    main()
