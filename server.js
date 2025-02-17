const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');

const app = express();

app.use(cors({
    origin: 'http://localhost:3000' // Replace with your front-end origin
}));

app.use(bodyParser.json());

app.post('/predict', (req, res) => {
    const metricsData = req.body;
    
    // Assuming `predictWithMLModel` is a function that processes the data with your ML model
    const predictionResult = predictWithMLModel(metricsData);

    res.json(predictionResult);
});

function predictWithMLModel(data) {
    // Use your ML model logic here to get predictions based on the data
    // For now, we'll just return a dummy result
    return { prediction: "dummy result based on metrics" };
}

app.listen(5000, () => {
    console.log('Server running on http://localhost:5000');
});
