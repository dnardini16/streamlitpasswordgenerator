import streamlit as st
from createPassword import createPWD

# Author: Davide Nardini 2021

def runApp():

    col1,col2,col3,col4,col5 = st.beta_columns(5)
    col3.image("lock_ale.png")

    st.markdown("<h1 style='text-align: center; color: #000000; font-family: cursive'> PASSWORD GENERATOR </h1>", unsafe_allow_html = True) 
    st.markdown(" ")
    st.markdown("<p style='text-align: center; color: #000000; font-family'> Genera password online gratis! </p>", unsafe_allow_html = True) 
    st.markdown("<p style='text-align: center; color: #000000; font-family'> Inserisci le specifiche della tua password e clicca sul bottone per generarla all'istante. </p>", unsafe_allow_html = True) 
    st.markdown("<p style='text-align: center; color: #000000; font-family'> by Davide Nardini </p>", unsafe_allow_html = True) 
    st.markdown("<p style='text-align: center; color: #000000; font-family'>  </p>", unsafe_allow_html = True) 
    st.markdown("<p style='text-align: center; color: #000000; font-family'>  </p>", unsafe_allow_html = True) 

    length = st.slider('Lunghezza della password',min_value=5, max_value=50, value=12)

    col1,col2,col3 = st.beta_columns(3)

    case = col1.checkbox("Maiuscole e minuscole",value=True)
    numeri = col2.checkbox("Numeri",value=True)
    simboli = col3.checkbox("Simboli",value=True)

    st.markdown("<p style='text-align: center; color: #000000; font-family'>  </p>", unsafe_allow_html = True) 
    st.markdown("<p style='text-align: center; color: #000000; font-family'>  </p>", unsafe_allow_html = True) 
    st.markdown("<p style='text-align: center; color: #000000; font-family'>  </p>", unsafe_allow_html = True) 
    st.markdown("<p style='text-align: center; color: #000000; font-family'>  </p>", unsafe_allow_html = True) 

    col3,col4,col5 = st.beta_columns(3)

    if col4.button('Genera la tua password personalizzata'):
        password = createPWD(length,cases=case,getSymbol=simboli,getNumber=numeri)
        st.markdown("<p style='text-align: center; color: #000000; font-family'>  </p>", unsafe_allow_html = True) 
        st.markdown("<p style='text-align: center; color: #000000; font-family'>  </p>", unsafe_allow_html = True) 
        st.markdown(f"<p style='text-align: center; color: #000000; font-family'> {password} </p>", unsafe_allow_html = True) 
    

    st.markdown("<p style='text-align: center; color: #000000; font-family'>  </p>", unsafe_allow_html = True) 
    st.markdown("<p style='text-align: center; color: #000000; font-family'>  </p>", unsafe_allow_html = True) 

    with st.beta_expander("More info"):
        st.write("""
        Grazie per aver usato questa piccola app! \n
        Le password che vengono generate non vengono registrate in alcun modo. Ti invito a non mostrare mai a nessuno le tue password e di stare attento quando le generi. \n
        Se ti piacerebbe saperne di più o ti fa piacere conoscermi, questi sono i miei recapiti: \n
        Linkedin: https://www.linkedin.com/in/davide-nardini/ \n
        Github: https://github.com/dnardini16
        """)

runApp()


