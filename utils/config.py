import streamlit as st

def get_config():
    """
    Carrega e retorna as configurações usando st.secrets (compatível com Streamlit Cloud).
    Conforme documentação oficial: https://docs.streamlit.io/develop/api-reference/connections-and-secrets/secrets-toml
    """
    try:
        # Tenta acessar os secrets do Streamlit Cloud primeiro
        if "custom" in st.secrets:
            return {
                "google_api_key": st.secrets["custom"]["google_api_key"],
                "supabase_url": st.secrets["custom"].get("supabase_url", ""),
                "supabase_key": st.secrets["custom"].get("supabase_key", ""),
            }
        else:
            # Se não encontrar a seção [custom], usa fallback
            st.warning("⚠️ Secrets não configurados no Streamlit Cloud. Usando chave de fallback temporária.")
            st.info("📝 Para configurar corretamente: App → Settings → Secrets → Adicione a seção [custom]")
            return {
                "google_api_key": "AIzaSyAVwh4gsg8NBBtb5E6VIwJzr6zuzJkIEh4",
                "supabase_url": "",
                "supabase_key": "",
            }
    except Exception as e:
        # Qualquer outro erro, usa fallback silenciosamente
        return {
            "google_api_key": "AIzaSyAVwh4gsg8NBBtb5E6VIwJzr6zuzJkIEh4",
            "supabase_url": "",
            "supabase_key": "",
        }
