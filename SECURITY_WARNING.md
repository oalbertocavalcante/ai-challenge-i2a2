# ⚠️ AVISO DE SEGURANÇA IMPORTANTE

## 🔴 CHAVE DE API TEMPORARIAMENTE PÚBLICA

**ATENÇÃO:** Este repositório contém uma chave de API do Google Gemini **TEMPORARIAMENTE PÚBLICA** apenas para facilitar o deploy inicial.

### 📋 O QUE FAZER APÓS O DEPLOY:

1. **IMEDIATAMENTE após o deploy funcionar:**
   - Acesse: https://makersuite.google.com/app/apikey
   - **DELETE** a chave antiga: `AIzaSyAVwh4gsg8NBBtb5E6VIwJzr6zuzJkIEh4`
   - **GERE** uma nova chave
   - **ATUALIZE** nos Secrets do Streamlit Cloud

2. **Remover a chave pública do código:**
   - Edite `utils/config.py`
   - Remova a chave hardcoded do fallback
   - Faça commit e push

3. **Invalidar o histórico do Git (opcional mas recomendado):**
   ```bash
   git filter-branch --force --index-filter \
   "git rm --cached --ignore-unmatch .env.public" \
   --prune-empty --tag-name-filter cat -- --all
   
   git push origin --force --all
   ```

### 🔒 COMO PROTEGER APÓS O DEPLOY:

#### No Streamlit Cloud (Settings → Secrets):
```toml
[custom]
google_api_key = "SUA_NOVA_CHAVE_AQUI"
supabase_url = ""
supabase_key = ""
```

#### Localmente (.streamlit/secrets.toml):
```toml
[custom]
google_api_key = "SUA_NOVA_CHAVE_AQUI"
supabase_url = ""
supabase_key = ""
```

### ⏰ PRAZO:

**TROQUE A CHAVE EM ATÉ 24 HORAS!**

Chaves públicas podem ser usadas por terceiros, gerando custos ou bloqueios na sua conta Google.

### 📞 Em caso de problemas:

- Revogue a chave imediatamente em: https://console.cloud.google.com/apis/credentials
- Gere uma nova chave
- Configure corretamente nos Secrets

---

**Este arquivo será removido após a correção de segurança.**
