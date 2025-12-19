# Guia d'Execució del Projecte

Aquest document proporciona instruccions pas a pas per executar el projecte de classificació de pingüins Palmer.

## 📋 Prerequisites

- Python 3.11 o superior
- pip o Conda instal·lat
- Git (opcional, per clonar el repositori)

## 🚀 Pas 1: Instal·lar Dependències

### Opció A: Utilitzant pip

```bash
# Crear entorn virtual
python -m venv venv

# Activar entorn virtual
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Instal·lar dependències
pip install -r requirements.txt
```

### Opció B: Utilitzant Conda (RECOMANAT)

```bash
# Crear entorn des de environment.yml
conda env create -f environment.yml

# Activar entorn
conda activate penguins-classifier
```

## 📊 Pas 2: Executar el Notebook de Preparació de Dades

```bash
# Iniciar Jupyter
jupyter notebook

# Obrir i executar: notebooks/01_preparacio_dades.ipynb
```

Aquest notebook:
- ✅ Carrega el dataset de pingüins Palmer
- ✅ Neteja les dades (elimina valors NA)
- ✅ Normalitza els noms
- ✅ Guarda el dataset net a `datasets/penguins_clean.csv`

**Resultat esperat:**
- Fitxer creat: `datasets/penguins_clean.csv`
- Aproximadament 333-344 files (després d'eliminar NA)

## 🤖 Pas 3: Entrenar els Models

```bash
# Obrir i executar: notebooks/02_entrenament_models.ipynb
```

Aquest notebook:
- ✅ Divideix les dades (80% train, 20% test)
- ✅ Aplica one-hot encoding
- ✅ Normalitza les variables numèriques
- ✅ Entrena 4 models:
  - Regressió Logística
  - SVM
  - Arbres de Decisió
  - KNN
- ✅ Avalua i compara els models
- ✅ Serialitza els models

**Resultat esperat:**
- 4 fitxers .pkl creats a la carpeta `models/`:
  - `logistic_regression_model.pkl`
  - `svm_model.pkl`
  - `decision_tree_model.pkl`
  - `knn_model.pkl`
- Accuracy > 95% per tots els models

## 🌐 Pas 4: Iniciar el Servidor Flask

**IMPORTANT:** Abans d'executar el notebook client, has d'iniciar el servidor!

```bash
# En una terminal/consola nova:
cd scripts
python app.py
```

**Sortida esperada:**
```
Carregant models...
✓ Model logistic_regression carregat correctament
✓ Model svm carregat correctament
✓ Model decision_tree carregat correctament
✓ Model knn carregat correctament

4 models carregats i llestos!

 * Serving Flask app 'penguins-classifier'
 * Debug mode: on
 * Running on http://0.0.0.0:5000
```

**⚠️ DEIXA AQUESTA TERMINAL OBERTA!** El servidor ha d'estar executant-se mentre utilitzes el client.

## 🧪 Pas 5: Provar els Models amb el Client

**En una altra terminal/consola:**

```bash
# Activar el mateix entorn virtual
# conda activate penguins-classifier  # o venv\Scripts\activate

# Iniciar Jupyter
jupyter notebook

# Obrir i executar: notebooks/03_client_prediccions.ipynb
```

Aquest notebook:
- ✅ Fa peticions HTTP als 4 models
- ✅ Prova múltiples exemples de pingüins
- ✅ Mostra les prediccions amb probabilitats
- ✅ Compara els resultats dels 4 models

**Resultat esperat:**
- Prediccions correctes per cada model
- Probabilitats mostrades per cada espècie
- Gràfics de barres amb les probabilitats

## 📸 Captures de Pantalla Requerides

Per l'entrega, necessites fer captures de:

### 1. Estructura del Projecte
- Obrir VS Code amb el projecte
- Expandir totes les carpetes
- Captura de l'explorador de fitxers

### 2. Fitxer environment.yml
- Obrir `environment.yml` en VS Code
- Captura del contingut complet

### 3. Execucions del Client (8 captures)
Per CADA model (4 models) necessites 2 captures amb:
- Les dades d'entrada del pingüí
- La predicció obtinguda
- Les probabilitats
- Un comentari sobre el resultat

**Exemple de comentari:**
> "El model de Regressió Logística prediu correctament que és un Adelie amb una confiança del 98.5%. Les característiques del pingüí (bec curt i ample, illes Torgersen) són típiques d'aquesta espècie."

## 🧪 Provar amb curl (Opcional)

Si vols provar manualment des de la terminal:

```bash
# Exemple 1: Pingüí Adelie
curl -X POST http://localhost:5000/predict/logistic_regression \
  -H "Content-Type: application/json" \
  -d "{\"island\": \"torgersen\", \"bill_length_mm\": 39.1, \"bill_depth_mm\": 18.7, \"flipper_length_mm\": 181.0, \"body_mass_g\": 3750.0, \"sex\": \"male\"}"

# Exemple 2: Pingüí Gentoo
curl -X POST http://localhost:5000/predict/svm \
  -H "Content-Type: application/json" \
  -d "{\"island\": \"biscoe\", \"bill_length_mm\": 50.0, \"bill_depth_mm\": 16.3, \"flipper_length_mm\": 230.0, \"body_mass_g\": 5700.0, \"sex\": \"male\"}"
```

## ❌ Troubleshooting

### Error: "Module not found"
```bash
# Assegura't que has activat l'entorn virtual
conda activate penguins-classifier
# o
venv\Scripts\activate
```

### Error: "Connection refused" al client
```bash
# Comprova que el servidor Flask està executant-se
# Ha d'haver una terminal amb el servidor actiu
```

### Error: "File not found" en carregar models
```bash
# Assegura't que has executat el notebook 02_entrenament_models.ipynb
# Els fitxers .pkl han d'existir a la carpeta models/
```

### El dataset està buit
```bash
# Executa primer el notebook 01_preparacio_dades.ipynb
# Això crearà el fitxer datasets/penguins_clean.csv
```

## ✅ Checklist Final

Abans de l'entrega, comprova que tens:

- [ ] Els 3 notebooks executats sense errors
- [ ] 4 models serialitzats a `models/`
- [ ] Servidor Flask funcionant
- [ ] 8 captures de pantalla (2 per cada model)
- [ ] Captura de l'estructura del projecte
- [ ] Captura del environment.yml
- [ ] Comentaris per cada predicció
- [ ] Repositori GitHub públic creat
- [ ] README.md actualitzat amb la URL del repositori

## 📚 Recursos Addicionals

- [Documentació scikit-learn](https://scikit-learn.org/)
- [Dataset Palmer Penguins](https://github.com/allisonhorst/palmerpenguins)
- [Flask Quickstart](https://flask.palletsprojects.com/en/2.3.x/quickstart/)
