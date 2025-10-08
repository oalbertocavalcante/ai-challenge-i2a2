import os
import streamlit as st

def get_config():
    """Carrega e retorna as configurações usando st.secrets (compatível com Streamlit Cloud)."""
    try:
        # Tenta carregar do Streamlit secrets (funciona local e no Cloud)
        return {
            "google_api_key": st.secrets.get("custom", {}).get("google_api_key"),
            "supabase_url": st.secrets.get("custom", {}).get("supabase_url", ""),
            "supabase_key": st.secrets.get("custom", {}).get("supabase_key", ""),
        }
    except Exception as e:
        print(f"Aviso: Erro ao carregar secrets: {e}")
        # Fallback para variáveis de ambiente
        return {
            "google_api_key": os.getenv("GOOGLE_API_KEY"),
            "supabase_url": os.getenv("SUPABASE_URL", ""),
            "supabase_key": os.getenv("SUPABASE_KEY", ""),
        }