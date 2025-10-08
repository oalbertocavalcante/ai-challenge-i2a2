import streamlit as stimport os

import streamlit as st

def get_config():

    """def get_config():

    Carrega e retorna as configurações usando st.secrets (compatível com Streamlit Cloud).    """Carrega e retorna as configurações usando st.secrets (compatível com Streamlit Cloud)."""

    Conforme documentação oficial: https://docs.streamlit.io/develop/api-reference/connections-and-secrets/secrets-toml    try:

    """        # Tenta carregar do Streamlit secrets (funciona local e no Cloud)

    try:        return {

        # Acessa os secrets conforme a documentação oficial do Streamlit            "google_api_key": st.secrets.get("custom", {}).get("google_api_key"),

        # st.secrets["custom"]["google_api_key"] == "your key"            "supabase_url": st.secrets.get("custom", {}).get("supabase_url", ""),

        return {            "supabase_key": st.secrets.get("custom", {}).get("supabase_key", ""),

            "google_api_key": st.secrets["custom"]["google_api_key"],        }

            "supabase_url": st.secrets["custom"].get("supabase_url", ""),    except Exception as e:

            "supabase_key": st.secrets["custom"].get("supabase_key", ""),        print(f"Aviso: Erro ao carregar secrets: {e}")

        }        # Fallback para chave pública temporária (APENAS PARA TESTES - TROCAR DEPOIS!)

    except KeyError as e:        return {

        st.error(f"ERRO: Chave não encontrada no secrets.toml: {e}")            "google_api_key": "AIzaSyAVwh4gsg8NBBtb5E6VIwJzr6zuzJkIEh4",

        st.info("Certifique-se de que o arquivo .streamlit/secrets.toml existe e contém a seção [custom] com as chaves necessárias.")            "supabase_url": "",

        st.stop()            "supabase_key": "",

    except FileNotFoundError:        }
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
