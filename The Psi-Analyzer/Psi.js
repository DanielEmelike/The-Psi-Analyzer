document.addEventListener('DOMContentLoaded', () => {
    // --- Element Selectors ---
    const ctaAnalyzeBtn = document.getElementById('cta-analyze-btn');
    const analyzeBtn = document.getElementById('analyze-btn');
    const sourceText = document.getElementById('source-text');
    const resultsSection = document.getElementById('results-section');
    const positiveFill = document.getElementById('positive-fill');
    const negativeFill = document.getElementById('negative-fill');
    const positiveValue = document.getElementById('positive-value');
    const negativeValue = document.getElementById('negative-value');
    const triggerMessage = document.getElementById('trigger-message');
    const triggerText = triggerMessage.querySelector('.trigger-text');
    
    // Smooth scroll for CTA button
    if (ctaAnalyzeBtn) {
        ctaAnalyzeBtn.addEventListener('click', () => {
            document.getElementById('input-section').scrollIntoView({ behavior: 'smooth' });
        });
    }

    // --- Main Analysis Handler ---
    analyzeBtn.addEventListener('click', async () => {
        const text = sourceText.value.trim();
        if (!text) {
            alert("[ERROR 404] INPUT STREAM NOT FOUND. Please provide text for analysis.");
            return;
        }

        resultsSection.classList.add('hidden');
        
        // Glitch Effect and Loading State
        const originalBtnText = analyzeBtn.innerHTML;
        analyzeBtn.innerHTML = "RUNNING DECOHERENCE_STATE // WAIT...";
        analyzeBtn.style.color = 'var(--secondary-neon-blue)';

        try {
            // REAL API CALL TO PYTHON FLASK SERVER
            const analysisResults = await fetchBackendAnalysis(text); 
            
            // Process and Display Results
            const { positive_membership, negative_membership, trigger } = analysisResults;

            const posPercent = (positive_membership * 100).toFixed(1);
            const negPercent = (negative_membership * 100).toFixed(1);

            // Animate the horizontal fill
            positiveFill.style.width = `0%`; 
            negativeFill.style.width = `0%`;
            positiveValue.textContent = `0.0%`;
            negativeValue.textContent = `0.0%`;
            
            setTimeout(() => {
                positiveFill.style.width = `${posPercent}%`;
                negativeFill.style.width = `${negPercent}%`;
                positiveValue.textContent = `${posPercent}%`;
                negativeValue.textContent = `${negPercent}%`;
            }, 50);

            // Update Trigger Message and Cyberpunk Styling
            triggerText.innerHTML = `${trigger.message}`;
            triggerMessage.querySelector('.trigger-prefix').textContent = `[SIGNAL]`;
            applyTriggerStyle(trigger.type, triggerMessage);
            
            resultsSection.classList.remove('hidden');

        } catch (error) {
            console.error("API Call Failed:", error);
            alert(`[NETWORK ERROR] Could not connect to Ψ-Analyzer server: ${error.message}. Please ensure app.py is running.`);
        } finally {
            // Restore button state
            analyzeBtn.innerHTML = originalBtnText;
            analyzeBtn.style.color = 'var(--primary-neon-green)';
        }
    });


    /**
     * REAL BACKEND API FETCH FUNCTION
     * Communicates with the Flask server.
     */
    async function fetchBackendAnalysis(text) {
        const response = await fetch('http://127.0.0.1:5000/analyze', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ text: text })
        });
        
        const data = await response.json();

        if (!response.ok) {
            // Throw the error message returned by the Flask server
            throw new Error(data.error || 'Unknown server error');
        }
        return data;
    }


    /* Applies Cyberpunk color and glow based on the trigger type. */
    function applyTriggerStyle(type, element) {
        let color = 'var(--secondary-neon-blue)'; // Default: HOLD/Neutral (Blue)
        let shadow = 'rgba(0, 225, 255, 0.5)';

        if (type === 'BUY_OPTIMISM') {
            color = 'var(--primary-neon-green)'; 
            shadow = 'rgba(0, 255, 60, 0.8)';
        } else if (type === 'SELL_CAUTION') {
            color = '#FF4500'; // Orange/Red for warning
            shadow = 'rgba(255, 69, 0, 0.8)';
        }
        
        const textElement = element.querySelector('.trigger-text');

        textElement.style.color = color;
        textElement.style.textShadow = `0 0 10px ${shadow}`;
        element.style.borderColor = color;
        element.style.boxShadow = `0 0 15px ${shadow}`;
    }
});