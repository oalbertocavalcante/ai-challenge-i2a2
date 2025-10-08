import streamlit as st

def get_config():
    """
    Carrega e retorna as configurações usando st.secrets (compatível com Streamlit Cloud).
    Conforme documentação oficial: https://docs.streamlit.io/develop/api-reference/connections-and-secrets/secrets-toml
    """
    try:
        # Acessa os secrets conforme a documentação oficial do Streamlit
        # st.secrets["custom"]["google_api_key"] == "your key"
        return {
            "google_api_key": st.secrets["custom"]["google_api_key"],
            "supabase_url": st.secrets["custom"].get("supabase_url", ""),
            "supabase_key": st.secrets["custom"].get("supabase_key", ""),
        }
    except KeyError as e:
        st.error(f"ERRO: Chave não encontrada no secrets.toml: {e}")
        st.info("Certifique-se de que o arquivo .streamlit/secrets.toml existe e contém a seção [custom] com as chaves necessárias.")
        st.stop()
    except FileNotFoundError:
        st.error("ERRO: Arquivo .streamlit/secrets.toml não encontrado!")
        st.info("Crie o arquivo .streamlit/secrets.toml na raiz do projeto com o formato:\n\n[custom]\ngoogle_api_key = \"sua_chave_aqui\"\nsupabase_url = \"\"\nsupabase_key = \"\"")
        st.stop()
    except Exception as e:
        st.error(f"ERRO ao carregar secrets: {e}")
        # Fallback para chave hardcoded (APENAS PARA TESTES - REMOVER EM PRODUÇÃO)
        st.warning("AVISO: Usando chave de fallback temporária. Configure o secrets.toml corretamente!")
        return {
            "google_api_key": "AIzaSyAVwh4gsg8NBBtb5E6VIwJzr6zuzJkIEh4",
            "supabase_url": "",
            "supabase_key": "",
        }
