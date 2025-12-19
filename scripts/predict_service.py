"""
Servei de predicció per als models de classificació de pingüins
"""
import pickle
import numpy as np


def load_model(model_path):
    """Carrega un model serialitzat"""
    with open(model_path, 'rb') as f:
        dv, scaler, le, model = pickle.load(f)
    return dv, scaler, le, model


def predict_penguin(penguin_data, dv, scaler, le, model):
    """
    Fa una predicció sobre les dades d'un pingüí

    Args:
        penguin_data: diccionari amb les dades del pingüí
        dv: DictVectorizer
        scaler: StandardScaler
        le: LabelEncoder
        model: model entrenat

    Returns:
        tupla (espècie_predita, probabilitats)
    """
    # Transformar les dades
    X = dv.transform([penguin_data])
    X_scaled = scaler.transform(X)

    # Fer la predicció
    prediction = model.predict(X_scaled)[0]
    species = le.inverse_transform([prediction])[0]

    # Obtenir probabilitats
    if hasattr(model, 'predict_proba'):
        probabilities = model.predict_proba(X_scaled)[0]
        probs_dict = {
            le.inverse_transform([i])[0]: float(prob)
            for i, prob in enumerate(probabilities)
        }
    else:
        probs_dict = {species: 1.0}

    return species, probs_dict
