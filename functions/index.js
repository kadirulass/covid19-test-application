const functions = require('firebase-functions');
const { spawn } = require('child_process');

exports.app = functions.https.onRequest((req, res) => {
  const pythonProcess = spawn('python', ['../Desktop/Python Lesson/app.py']); // Python uygulamanızın yolunu buraya ekleyin

  pythonProcess.stdout.on('data', (data) => {
    res.send(data.toString());
  });

  pythonProcess.stderr.on('data', (data) => {
    console.error(`stderr: ${data}`);
  });

  pythonProcess.on('close', (code) => {
    console.log(`child process exited with code ${code}`);
  });
});
