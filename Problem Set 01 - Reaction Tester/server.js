// This will be the node Express server that will serve up your app
const express = require('express');
const bodyParser = require('body-parser');
const app = express();
const PORT = process.env.PORT || 3030;
const path = require('path');

// Store the fastest reaction time
let fastestTime = Infinity;

app.use(bodyParser.json());

// Serve the HTML page
app.get('/', (_, res) => {
    res.sendFile(path.join(__dirname, 'index.html'));
});

// Receive reaction time from client and record if it's the fastest
app.post('/record-time', (req, res) => {
    const reactionTime = req.body.time;
    if (reactionTime < fastestTime) {
        fastestTime = reactionTime;
    }
    res.status(200).send({ reactionTime, fastestTime });
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is listening on port ${PORT}`);
});