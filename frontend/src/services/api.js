const API_BASE_URL = "http://127.0.0.1:8000"; 

export const getSamples = async () => {
    try {
        const response = await fetch(`${API_BASE_URL}/samples`);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return await response.json();
    } catch (error) {
        console.error("Error fetching samples:", error);
        return []; 
    }
};