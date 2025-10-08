# 🚀 Guia de Deploy para GitHub e Streamlit Cloud

## ✅ Status Atual do Repositório

- [x] Repositório Git inicializado
- [x] Arquivos adicionados ao Git
- [x] Commit inicial criado (34 arquivos)
- [x] .gitignore configurado (seus secrets estão protegidos!)
- [x] README.md completo criado
- [ ] Repositório no GitHub criado
- [ ] Código enviado para GitHub
- [ ] Deploy no Streamlit Cloud

---

## 📋 Passo 1: Criar Repositório no GitHub

### 1.1 Acesse o GitHub
1. Abra o navegador e vá para: https://github.com
2. Faça login na sua conta (ou crie uma se não tiver)

### 1.2 Criar Novo Repositório
1. Clique no botão **"+"** no canto superior direito
2. Selecione **"New repository"**
3. Preencha os dados:
   - **Repository name:** `ai-agent-challenge` (ou outro nome)
   - **Description:** "Sistema de Análise Exploratória de Dados com Inteligência Artificial"
   - **Public** (marque esta opção - necessário para Streamlit Cloud gratuito)
   - **NÃO** marque "Initialize with README" (já temos um!)
   - **NÃO** adicione .gitignore ou licença (já temos!)
4. Clique em **"Create repository"**

### 1.3 Copiar URL do Repositório
Depois de criar, você verá uma página com comandos. Copie a URL que aparece, algo como:
```
https://github.com/SEU_USUARIO/ai-agent-challenge.git
```

---

## 📤 Passo 2: Enviar Código para o GitHub

### 2.1 Abrir PowerShell (você já está com o terminal aberto!)

Certifique-se de estar na pasta correta:
```powershell
cd "C:\Users\Casa\Desktop\ai-agent-challenge\ai-agent-challenge"
```

### 2.2 Conectar ao Repositório Remoto

Execute este comando **substituindo** pela URL que você copiou:
```powershell
git remote add origin https://github.com/SEU_USUARIO/ai-agent-challenge.git
```

**Exemplo real:**
```powershell
git remote add origin https://github.com/joaosilva/ai-agent-challenge.git
```

### 2.3 Renomear a Branch para 'main' (padrão do GitHub)
```powershell
git branch -M main
```

### 2.4 Enviar o Código (Push)
```powershell
git push -u origin main
```

**O que vai acontecer:**
- O GitHub vai pedir suas credenciais
- Se aparecer uma janela de autenticação, faça login
- Aguarde o upload (pode demorar 1-2 minutos)

**Se der erro de autenticação:**
1. GitHub não aceita mais senha comum
2. Você precisa criar um **Personal Access Token**
3. Vá em: GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
4. Clique em "Generate new token (classic)"
5. Marque a opção "repo"
6. Copie o token gerado
7. Use o token como senha quando o Git pedir

---

## 🌐 Passo 3: Deploy no Streamlit Cloud

### 3.1 Criar Conta no Streamlit Cloud
1. Acesse: https://streamlit.io/cloud
2. Clique em **"Sign up"**
3. Escolha **"Continue with GitHub"**
4. Autorize o acesso do Streamlit ao seu GitHub

### 3.2 Criar Nova Aplicação
1. No dashboard do Streamlit Cloud, clique em **"New app"**
2. Preencha os campos:
   - **Repository:** Selecione `SEU_USUARIO/ai-agent-challenge`
   - **Branch:** `main`
   - **Main file path:** `app.py`
   - **App URL:** escolha um nome único (ex: `seu-nome-eda-ai`)

### 3.3 Configurar Secrets (MUITO IMPORTANTE!)

**ANTES de clicar em "Deploy", faça isto:**

1. Clique em **"Advanced settings"**
2. Na seção **"Secrets"**, cole este conteúdo:

```toml
[custom]
google_api_key = "COLE_SUA_CHAVE_GOOGLE_AQUI"
supabase_url = ""
supabase_key = ""
```

3. **Substitua** `COLE_SUA_CHAVE_GOOGLE_AQUI` pela sua chave real do Google Gemini

**Onde está minha chave?**
- Ela está no arquivo `.streamlit/secrets.toml` no seu computador
- Abra esse arquivo e copie o valor de `google_api_key`
- **OU** pegue uma nova em: https://makersuite.google.com/app/apikey

### 3.4 Deploy!
1. Clique em **"Deploy!"**
2. Aguarde 3-5 minutos (primeira vez demora mais)
3. Você verá logs aparecendo (instalando dependências)
4. Quando terminar, aparecerá: **"Your app is live!"**

### 3.5 Testar a Aplicação
1. Clique no link gerado (algo como: `https://seu-nome-eda-ai.streamlit.app`)
2. Faça upload de um CSV de teste
3. Faça algumas perguntas para validar
4. Se funcionar, está pronto! 🎉

---

## 🔧 Solução de Problemas Comuns

### Erro: "git: command not found"
**Problema:** Git não está instalado
**Solução:** Baixe e instale de: https://git-scm.com/download/win

### Erro: "remote origin already exists"
**Problema:** Já existe um remote configurado
**Solução:**
```powershell
git remote remove origin
git remote add origin https://github.com/SEU_USUARIO/ai-agent-challenge.git
```

### Erro no Streamlit Cloud: "ModuleNotFoundError"
**Problema:** Dependência faltando
**Solução:**
1. Verifique se `requirements.txt` está no repositório
2. Verifique se todas as bibliotecas estão listadas
3. Tente fazer "Reboot app" no dashboard do Streamlit

### Erro: "API key not configured"
**Problema:** Secret não foi configurado corretamente
**Solução:**
1. No Streamlit Cloud, vá em: App → Settings → Secrets
2. Verifique se o formato está correto (TOML)
3. Certifique-se de que colocou a chave real do Google
4. Clique em "Save" e reinicie a aplicação

### Aplicação muito lenta no Streamlit Cloud
**Problema:** Plano gratuito tem recursos limitados
**Solução:**
1. Use CSVs menores para demonstração
2. Evite fazer muitas perguntas seguidas
3. Aguarde alguns segundos entre as perguntas

---

## 📝 Comandos Git Úteis para o Futuro

### Ver status dos arquivos
```powershell
git status
```

### Adicionar novos arquivos modificados
```powershell
git add .
```

### Fazer novo commit
```powershell
git commit -m "Descrição das mudanças"
```

### Enviar mudanças para GitHub
```powershell
git push
```

### Ver histórico de commits
```powershell
git log --oneline
```

### Desfazer mudanças não commitadas
```powershell
git checkout -- arquivo.py
```

---

## 🎯 Checklist Final

Antes de submeter para a I2A2 Academy, verifique:

- [ ] Repositório público no GitHub criado
- [ ] Código completo enviado (34 arquivos)
- [ ] README.md visível no GitHub
- [ ] Aplicação rodando no Streamlit Cloud
- [ ] Secrets configurados corretamente (API do Google)
- [ ] Testei com upload de CSV
- [ ] Testei fazendo perguntas ao sistema
- [ ] Gráficos são gerados corretamente
- [ ] Sem emojis na interface (só texto profissional)
- [ ] Cores profissionais (verde/laranja/preto)
- [ ] Link público funcionando

---

## 📧 Links para Submissão

**Para entregar o projeto, você precisará fornecer:**

1. **Link do GitHub:**
   ```
   https://github.com/SEU_USUARIO/ai-agent-challenge
   ```

2. **Link da Aplicação:**
   ```
   https://seu-nome-eda-ai.streamlit.app
   ```

3. **Confirmação sobre Supabase:**
   ```
   NÃO é necessário configurar o Supabase.
   O sistema funciona 100% sem ele.
   ```

---

## 💡 Dicas Importantes

### Segurança
- ⚠️ **NUNCA** commite o arquivo `secrets.toml`
- ⚠️ **NUNCA** compartilhe suas chaves de API publicamente
- ✅ Sempre use Secrets no Streamlit Cloud
- ✅ O `.gitignore` já protege seus secrets automaticamente

### Diferenciação do Projeto
Seu projeto se diferencia dos colegas por:
- ✅ Interface profissional sem emojis
- ✅ Esquema de cores verde/laranja/preto
- ✅ README extremamente detalhado
- ✅ Documentação completa de deploy
- ✅ Sistema funciona sem Supabase

### Performance
- Use CSVs de até 10.000 linhas para melhor performance
- Evite fazer upload de arquivos muito grandes no Streamlit Cloud
- O dataset de Credit Card Fraud é ideal para demonstração

---

## 🎓 Créditos

**Desenvolvido para:** I2A2 Academy - Institut d'Intelligence Artificielle Appliquée  
**Curso:** Agentes Autônomos  
**Data:** Outubro de 2025  
**Status:** ✅ Pronto para produção

---

**Boa sorte com o deploy! 🚀**

Se tiver dúvidas, revise este guia ou consulte o README.md principal.
