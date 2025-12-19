# Classificador de Pingüins Palmer

Projecte de classificació d'espècies de pingüins de l'arxipèlag Palmer utilitzant 4 models diferents de Machine Learning.

## 📋 Descripció

Aquest projecte implementa i compara 4 models de classificació per predir l'espècie d'un pingüí (Adelie, Chinstrap o Gentoo) basant-se en les seves característiques físiques:

- **Regressió Logística**
- **SVM (Support Vector Machine)**
- **Arbres de Decisió (Decision Trees)**
- **KNN (k-Nearest Neighbours)**

## 📊 Dataset

S'utilitza el dataset **Palmer Penguins**, disponible a través de la llibreria seaborn, que conté dades de 344 pingüins de 3 espècies diferents.

### Variables predictores:
- `island`: Illa on viu el pingüí (Torgersen, Biscoe, Dream)
- `bill_length_mm`: Longitud del bec en mm
- `bill_depth_mm`: Profunditat del bec en mm
- `flipper_length_mm`: Longitud de l'aleta en mm
- `body_mass_g`: Massa corporal en grams
- `sex`: Sexe (male/female)

### Variable objectiu:
- `species`: Espècie del pingüí (Adelie, Chinstrap, Gentoo)

## 🗂️ Estructura del Projecte

```
tasca3/
├── datasets/           # Datasets (generats automàticament)
├── models/            # Models entrenats i serialitzats
├── notebooks/         # Jupyter notebooks
│   ├── 01_preparacio_dades.ipynb
│   ├── 02_entrenament_models.ipynb
│   └── 03_client_prediccions.ipynb
├── scripts/           # Scripts Python
│   ├── app.py
│   └── predict_service.py
├── README.md
└── requirements.txt
```

## 🚀 Instal·lació i Configuració

### Opció 1: Utilitzant pip

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

### Opció 2: Utilitzant Conda

```bash
# Crear entorn conda
conda create -n penguins python=3.11

# Activar entorn
conda activate penguins

# Instal·lar dependències
conda install scikit-learn pandas seaborn flask jupyter ipykernel
```

## 📓 Ús dels Notebooks

### 1. Preparació de Dades
```bash
jupyter notebook notebooks/01_preparacio_dades.ipynb
```
Aquest notebook:
- Carrega el dataset de seaborn
- Neteja les dades (elimina valors NA)
- Normalitza els noms de columnes
- Guarda el dataset net

### 2. Entrenament dels Models
```bash
jupyter notebook notebooks/02_entrenament_models.ipynb
```
Aquest notebook:
- Divideix les dades (80% train, 20% test)
- Aplica one-hot encoding a variables categòriques
- Normalitza les variables numèriques
- Entrena els 4 models
- Compara els resultats
- Serialitza els models

### 3. Client de Prediccions
```bash
jupyter notebook notebooks/03_client_prediccions.ipynb
```
Aquest notebook:
- Fa peticions als serveis web
- Prova cada model amb diferents exemples
- Compara les prediccions

## 🌐 Serveis Web

### Iniciar el servidor Flask

```bash
cd scripts
python app.py
```

El servidor s'iniciarà a `http://localhost:5000`

### Endpoints disponibles

#### 1. Health Check
```bash
GET /health
```

#### 2. Llistar Models
```bash
GET /models
```

#### 3. Fer Predicció
```bash
POST /predict/<model_name>

# model_name: logistic_regression, svm, decision_tree, knn
```

**Exemple de petició:**
```bash
curl -X POST http://localhost:5000/predict/logistic_regression \
  -H "Content-Type: application/json" \
  -d '{
    "island": "biscoe",
    "bill_length_mm": 45.2,
    "bill_depth_mm": 16.6,
    "flipper_length_mm": 191.0,
    "body_mass_g": 3250.0,
    "sex": "male"
  }'
```

**Exemple de resposta:**
```json
{
  "model": "logistic_regression",
  "input": {...},
  "prediction": {
    "species": "Adelie",
    "probabilities": {
      "Adelie": 0.85,
      "Chinstrap": 0.10,
      "Gentoo": 0.05
    },
    "confidence": 0.85
  }
}
```

## 📈 Resultats

Els 4 models han estat entrenats i avaluats amb el conjunt de test. Els resultats típics són:

| Model | Accuracy |
|-------|----------|
| Regressió Logística | ~98% |
| SVM | ~99% |
| Arbres de Decisió | ~95% |
| KNN | ~97% |

*Nota: Els resultats poden variar lleugerament segons la divisió train/test*

## 🛠️ Tecnologies Utilitzades

- **Python 3.11+**
- **scikit-learn**: Models de Machine Learning
- **pandas**: Manipulació de dades
- **seaborn**: Dataset i visualitzacions
- **Flask**: API REST
- **Jupyter**: Notebooks interactius
- **pickle**: Serialització de models

## 👥 Autor

Juan Ignacio Akrich Vazquez

## 📝 Llicència

Aquest projecte és amb finalitats educatives.
