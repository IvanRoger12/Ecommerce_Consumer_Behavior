
import streamlit as st

# Appliquer le style CSS depuis le fichier
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.set_page_config(
    page_title="SmartClient Dashboard",
    page_icon="👑",
    layout="wide"
)

st.title("👑 Bienvenue sur SmartClient")
st.markdown("### Sélectionne une page à gauche pour commencer 📊")

st.markdown("---")
st.markdown("🎯 **Pages disponibles :**")
st.markdown("- 📈 Profil Client")
st.markdown("- 👑 Fidélité")
st.markdown("- 🎯 Recommandations")

# Exemple de bouton export CSV de données fictives
import pandas as pd

# Exemple de données simples
data = pd.DataFrame({
    "Client": ["C001", "C002", "C003"],
    "Segment": ["Premium", "Standard", "Basic"],
    "Score": [92, 74, 55]
})

csv = data.to_csv(index=False).encode('utf-8')

st.download_button(
    label="📥 Télécharger exemple CSV",
    data=csv,
    file_name='exemple_clients.csv',
    mime='text/csv'
)
