<img width="1472" height="704" alt="Psi_collage" src="https://github.com/user-attachments/assets/25094484-e3d2-452c-ad43-b61e1eae394f" />



## 🌟 The $\Psi$-Analyzer: Quantum-Inspired Financial Sentiment Engine

The **$\Psi$-Analyzer** is a web application that implements a **Quantum-Inspired Fuzzy Sentiment Engine** to analyze financial text. It models market emotion not as a simple positive/negative binary, but as a superposition state where opposing sentiments (Optimism and Caution) can coexist, inspired by quantum cognition principles. This ambiguity is then resolved through a **"Decoherence"** process, yielding a final, actionable market signal.

The project is structured as a **Client-Server Architecture**:

- **Backend (Python/Flask):** Contains the core analytical logic.

- **Frontend (HTML/CSS/JS):** Provides a interactive **Matrix-themed** user interface.

### ⚙️ Core Technology

The analytical core (`Psi_app.py`) utilizes a hybrid approach:

**1. Fuzzy Membership ($\mu_{pos}, \mu_{neg}$)**: Initial sentiment features are extracted from the text and normalized to a range of $[0, 1]$, representing the initial levels of Optimism and Caution.

**2. Quantum Interference**: A **Conflict Ter**m ($C = \mu_{pos} \cdot \mu_{neg}$) and an **Interference Term** ($I$) are introduced to model the entanglement between the opposing sentiments. The Interference Term mathematically adjusts the final output based on the initial conflict and bias.

**2. Decoherence (Measurement)**: The final measured sentiments ($Final_{pos}$, $Final_{neg}$) are calculated by adjusting the initial values using the Interference Term:

$$Final_{pos} = \mu_{pos} + I$$

$$Final_{neg} = \mu_{neg} - I$$

This process mimics the act of observation forcing the sentiment into a measurable state, resulting in a unique **Actionable Market Trigger**.

**Actionable Market Triggers**

| Trigger Type | Description | Condition |
| :--- | :--- | :--- |
| **BUY\_OPTIMISM** | Strong positive signal. | $Final_{pos} > 0.7 \text{ AND } Final_{neg} < 0.35$ |
| **SELL\_CAUTION** | Strong negative signal. | $Final_{neg} > 0.7 \text{ AND } Final_{pos} < 0.35$ |
| **HOLD\_AMBIGUITY** | CRITICAL STATE: SUPERPOSITION DETECTED. High volatility likely. | Conflict Term $C > 0.20$ |
| **NEUTRAL** | Low momentum/low conflict. | Default/Else |

### 🚀 Getting Started

These instructions detail how to get the $\Psi$-Analyzer running on your local machine.

**Prerequisites**

You need **Python 3.x** and a web browser.

You must install the required Python packages: **Flask** for the web server, **Flask-COR**S for handling frontend-backend communication, and **NumPy** for numerical stability.

```bash
pip install Flask flask-cors numpy
```

**Installation and Run**

**1. Project Structure**: Ensure the following files are located in the same root directory:

- `Psi_app.py` (Backend Logic)

- `Psi.js` (Frontend Script)

- `Psi_home.html` (Main Interface)

- `Psi_style.css` (Matrix Styling)

- `GIF/gif01.gif` (Hero Image)

2. Run the Backend Server: Open your terminal in the project directory and execute the Python script. This launches the Flask API server.
  
``` bash
python Psi_app.py
```
The server will start, typically running on: `http://127.0.0.1:5000`

**3. Launch the Frontend**: Open the `Psi_home.html` file in your preferred web browser.

The **JavaScript frontend** (`Psi.js`) will handle the user interaction, send the text to the Flask API endpoint (`http://127.0.0.1:5000/analyze`), and dynamically display the results using the Matrix themed styling defined in `Psi_style.css`.

**4. Analyze**: Paste the text you want to analyze into the text area and click **"RUN SENTIMENT DECOHERENCE // EXECUTE"**.
