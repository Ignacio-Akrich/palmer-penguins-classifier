"""
Aplicació Flask per servir els 4 models de classificació de pingüins
"""
from flask import Flask, request, jsonify
import sys
import os

# Afegir el directori actual al path per importar predict_service
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from predict_service import load_model, predict_penguin

app = Flask('penguins-classifier')

# Carregar els 4 models
print("Carregant models...")
models = {}
model_names = ['logistic_regression', 'svm', 'decision_tree', 'knn']

for model_name in model_names:
    # Construir el path absolut basant-nos en la ubicació del script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(script_dir, '..', 'models', f'{model_name}_model.pkl')
    try:
        models[model_name] = load_model(model_path)
        print(f"✓ Model {model_name} carregat correctament")
    except Exception as e:
        print(f"✗ Error carregant {model_name}: {str(e)}")

print(f"\n{len(models)} models carregats i llestos!\n")


@app.route('/predict/<model_name>', methods=['POST'])
def predict(model_name):
    """
    Endpoint per fer prediccions amb un model específic

    Exemple de petició:
    POST /predict/logistic_regression
    {
        "island": "biscoe",
        "bill_length_mm": 45.2,
        "bill_depth_mm": 16.6,
        "flipper_length_mm": 191.0,
        "body_mass_g": 3250.0,
        "sex": "male"
    }
    """
    if model_name not in models:
        return jsonify({
            'error': f'Model {model_name} no trobat',
            'available_models': list(models.keys())
        }), 404

    # Obtenir les dades del pingüí
    penguin_data = request.get_json()

    if not penguin_data:
        return jsonify({'error': 'No s\'han proporcionat dades'}), 400

    # Validar que tenim tots els camps necessaris
    required_fields = ['island', 'bill_length_mm', 'bill_depth_mm',
                       'flipper_length_mm', 'body_mass_g', 'sex']

    missing_fields = [field for field in required_fields if field not in penguin_data]
    if missing_fields:
        return jsonify({
            'error': f'Falten els següents camps: {missing_fields}'
        }), 400

    try:
        # Fer la predicció
        dv, scaler, le, model = models[model_name]
        species, probabilities = predict_penguin(penguin_data, dv, scaler, le, model)

        # Preparar la resposta
        result = {
            'model': model_name,
            'input': penguin_data,
            'prediction': {
                'species': species,
                'probabilities': probabilities,
                'confidence': max(probabilities.values())
            }
        }

        return jsonify(result)

    except Exception as e:
        return jsonify({
            'error': f'Error fent la predicció: {str(e)}'
        }), 500


@app.route('/models', methods=['GET'])
def list_models():
    """Llista els models disponibles"""
    return jsonify({
        'models': list(models.keys()),
        'count': len(models)
    })


@app.route('/health', methods=['GET'])
def health():
    """Endpoint de salut"""
    return jsonify({
        'status': 'healthy',
        'models_loaded': len(models)
    })


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
