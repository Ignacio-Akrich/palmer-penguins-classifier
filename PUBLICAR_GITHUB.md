# Com Publicar el Projecte a GitHub

## Opció 1: Des de la Línia de Comandes (Recomanat)

### Pas 1: Crear el repositori a GitHub

1. Ves a [GitHub](https://github.com)
2. Inicia sessió amb el teu compte
3. Clica el botó **"+"** a la barra superior → **"New repository"**
4. Configura el repositori:
   - **Repository name:** `palmer-penguins-classifier` (o el nom que vulguis)
   - **Description:** "Classificador d'espècies de pingüins Palmer amb 4 models de ML"
   - **Visibilitat:** Selecciona **Public** (MOLT IMPORTANT!)
   - **NO** marquis cap opció de "Initialize this repository with..."
5. Clica **"Create repository"**

### Pas 2: Connectar el repositori local amb GitHub

GitHub et mostrarà instruccions. Segueix aquestes:

```bash
# Anar al directori del projecte
cd "d:\Documentos\MASTER_IA\ProgramacioIA\Tasques\tasca3"

# Afegir el remote (substitueix YOUR_USERNAME pel teu usuari de GitHub)
git remote add origin https://github.com/YOUR_USERNAME/palmer-penguins-classifier.git

# Canviar el nom de la branca a main (si és necessari)
git branch -M main

# Pujar els canvis a GitHub
git push -u origin main
```

### Pas 3: Verificar

1. Refresca la pàgina del repositori a GitHub
2. Hauries de veure tots els fitxers del projecte
3. El fitxer [README.md](README.md) es mostrarà automàticament

---

## Opció 2: Des de VS Code (amb GitHub Extension)

### Pas 1: Instal·lar l'extensió de GitHub

1. Obre VS Code
2. Ves a Extensions (Ctrl+Shift+X)
3. Cerca "GitHub Pull Requests and Issues"
4. Instal·la l'extensió oficial de GitHub

### Pas 2: Publicar

1. Obre el projecte a VS Code
2. Ves al panell de Source Control (Ctrl+Shift+G)
3. Clica el botó **"Publish to GitHub"**
4. Selecciona **"Publish to GitHub public repository"**
5. Tria el nom del repositori
6. Espera que es completi la publicació

---

## Opció 3: GitHub Desktop (Més visual)

### Pas 1: Descarregar GitHub Desktop

1. Ves a [desktop.github.com](https://desktop.github.com/)
2. Descarrega i instal·la GitHub Desktop
3. Inicia sessió amb el teu compte de GitHub

### Pas 2: Afegir el repositori

1. Obre GitHub Desktop
2. File → Add Local Repository
3. Selecciona la carpeta `tasca3`
4. Clica **"Add Repository"**

### Pas 3: Publicar

1. Clica **"Publish repository"**
2. Configura:
   - Name: `palmer-penguins-classifier`
   - Description: "Classificador d'espècies de pingüins Palmer amb 4 models de ML"
   - **Desmarca** "Keep this code private" (perquè sigui públic)
3. Clica **"Publish Repository"**

---

## Verificació Final

### ✅ Comprova que el repositori és públic:

1. Ves a `https://github.com/YOUR_USERNAME/palmer-penguins-classifier`
2. Si pots veure el repositori sense iniciar sessió, és públic ✓
3. Busca la icona 🔓 al costat del nom del repositori

### ✅ Comprova el contingut:

Hauries de veure:
- [ ] README.md (ben formatat i visible)
- [ ] Carpeta `notebooks/` amb 3 notebooks
- [ ] Carpeta `scripts/` amb app.py i predict_service.py
- [ ] requirements.txt
- [ ] environment.yml
- [ ] GUIA_EXECUCIO.md
- [ ] .gitignore

### ✅ Copia la URL del repositori:

La URL serà algo com:
```
https://github.com/YOUR_USERNAME/palmer-penguins-classifier
```

**Aquesta URL és la que has de posar al document d'entrega!**

---

## Troubleshooting

### Error: "Permission denied (publickey)"

Solució: Utilitza HTTPS en lloc de SSH:
```bash
git remote set-url origin https://github.com/YOUR_USERNAME/palmer-penguins-classifier.git
```

### Error: "Repository already exists"

Solució: Si el repositori ja existeix a GitHub però està buit:
```bash
git remote add origin https://github.com/YOUR_USERNAME/palmer-penguins-classifier.git
git push -u origin main --force
```

### El repositori és privat per error

Solució:
1. Ves a Settings del repositori a GitHub
2. Baixa fins a "Danger Zone"
3. Clica "Change repository visibility"
4. Selecciona "Make public"

---

## Actualitzar el Repositori (després de canvis)

Si fas canvis al projecte i vols actualitzar GitHub:

```bash
# Afegir els canvis
git add .

# Fer commit
git commit -m "Descripció dels canvis"

# Pujar a GitHub
git push origin main
```

O des de VS Code:
1. Ves a Source Control
2. Escriu un missatge de commit
3. Clica el botó de ✓ (Commit)
4. Clica els ... → Push

---

## Notes Finals

- **IMPORTANT:** El repositori HA de ser PÚBLIC per poder-se avaluar
- La URL del repositori és la que posarà al document d'entrega
- Comprova que tots els fitxers s'han pujat correctament
- El README.md es mostra automàticament a la pàgina principal del repositori
