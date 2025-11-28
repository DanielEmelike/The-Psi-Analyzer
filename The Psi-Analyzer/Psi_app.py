from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
from typing import Dict, Any

# --- Core Component: Quantum-Inspired Fuzzy Engine ---

def get_sentiment_features(text: str) -> Dict[str, float]:
    """
    NLP Feature Extraction: Converts raw text cues into initial fuzzy membership values (μ_pos, μ_neg).
    """
    text_lower = text.lower()

    # Core Financial Sentiment Lexicon
    positive_cues = ["buy", "moon", "bullish", "profit", "gain", "soar", "long", "rally", "growth", "breakout",
                     "resilience"]
    negative_cues = ["sell", "bearish", "crash", "loss", "dump", "short", "risk", "debt", "recession", "instability",
                     "uncertainty"]

    pos_score = sum(text_lower.count(word) for word in positive_cues)
    neg_score = sum(text_lower.count(word) for word in negative_cues)

    total_cues = pos_score + neg_score

    if total_cues == 0:
        # Default low membership for minimal ambiguity
        return {"initial_pos": 0.1, "initial_neg": 0.1}

    # Density-based normalization to get initial [0, 1] fuzzy membership
    initial_pos = min(1.0, pos_score * 0.15 + 0.2 * (pos_score / total_cues))
    initial_neg = min(1.0, neg_score * 0.15 + 0.2 * (neg_score / total_cues))

    return {"initial_pos": float(initial_pos), "initial_neg": float(initial_neg)}


def quantum_fuzzy_sentiment_analysis(text: str) -> Dict[str, Any]:
    """
    Applies the Ψ-Analyzer logic: Fuzzy Membership + Quantum Interference.
    Calculates the final measured sentiment after decoherence.
    """
    features = get_sentiment_features(text)
    miu_pos = features['initial_pos']  # |\alpha|^2 (Optimism membership)
    miu_neg = features['initial_neg']  # |\beta|^2 (Caution membership)

    # --- 1. Conflict and Entanglement Modeling ---

    # Conflict Term (C): High when both sentiments are simultaneously present.
    conflict_C = miu_pos * miu_neg

    # Interference Term (I): Models the quantum-like effect of entanglement.
    coherence_factor_K = 0.4
    interference_I = coherence_factor_K * conflict_C * (miu_pos - miu_neg)

    # --- 2. Final Decoherence (Measurement) ---
    # Final membership is adjusted by interference.
    final_pos = max(0.0, min(1.0, miu_pos + interference_I))
    final_neg = max(0.0, min(1.0, miu_neg - interference_I))

    # --- 3. Fuzzy Logic Decision Trigger ---

    trigger_strength = np.abs(final_pos - final_neg)

    if final_pos > 0.7 and final_neg < 0.35:
        trigger_type = 'BUY_OPTIMISM'
        message = "BULLISH DECOHERENCE. Strong and unambiguous positive trend."
        trigger_strength = final_pos
    elif final_neg > 0.7 and final_pos < 0.35:
        trigger_type = 'SELL_CAUTION'
        message = "BEARISH DECOHERENCE. Initiate hedge/sell protocol."
        trigger_strength = final_neg
    elif conflict_C > 0.20:
        trigger_type = 'HOLD_AMBIGUITY'
        message = "CRITICAL_STATE: SUPERPOSITION DETECTED. High volatility likely. HOLD/WAIT FOR RESOLUTION."
        trigger_strength = conflict_C
    else:
        trigger_type = 'NEUTRAL'
        message = "NEUTRAL STATE. Low momentum, low conflict."
        trigger_strength = 0.0

    return {
        "positive_membership": float(final_pos),
        "negative_membership": float(final_neg),
        "trigger": {
            "type": trigger_type,
            "message": message,
            "strength": float(trigger_strength)
        }
    }


# --- Flask Server Setup ---

app = Flask(__name__)
# Enable CORS for frontend communication (running on different ports/origins)
CORS(app)


## API ENDPOINT: http://127.0.0.1:5000/analyze
@app.route('/analyze', methods=['POST'])
def analyze_sentiment():
    """Receives JSON text input and returns the analysis results."""
    try:
        data = request.json
        text = data.get('text', '')

        if not text:
            return jsonify({"error": "[SYSTEM_ERROR] E401: NO INPUT DATA RECEIVED."}), 400

        # Call the core analytical function
        results = quantum_fuzzy_sentiment_analysis(text)

        # Return the results as a JSON response
        return jsonify(results)

    except Exception as e:
        print(f"An error occurred during analysis: {e}")
        return jsonify({"error": f"[SYSTEM_ERROR] E500: BACKEND FAILURE - {str(e)}"}), 500


if __name__ == '__main__':
    print("--- Ψ-Analyzer Server Protocol Initiated ---")
    print("API endpoint: http://127.0.0.1:5000/analyze")
    # To start the server, run: python app.py
    app.run(debug=True)