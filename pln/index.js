const express = require('express');
const { WebSocketServer } = require('ws');
const { PythonShell } = require('python-shell');

const app = express();
const PORT = 3000;

const server = app.listen(PORT, () => {
  console.log(`Servidor rodando em http://localhost:${PORT}`);
});

// Criando o servidor WebSocket
const wss = new WebSocketServer({ server });

wss.on('connection', (ws) => {
  console.log('Cliente conectado ao WebSocket');

  // Criar um processo Python que ficará aberto durante a conexão
  let chatbotProcess = new PythonShell('chatbot_ia.py', { mode: 'json', pythonOptions: ['-u'] });

  chatbotProcess.on('message', (response) => {
    console.log(`Resposta do chatbot: ${response.response}`);
    ws.send(JSON.stringify({ response: response.response }));
  });

  ws.on('message', (message) => {
    try {
      const data = JSON.parse(message);
      console.log(`Mensagem recebida: ${data.message}`);

      // Enviar a mensagem para o chatbot Python
      chatbotProcess.send({ message: data.message });
    } catch (error) {
      console.error('Erro ao processar mensagem:', error);
      ws.send(JSON.stringify({ error: "Erro ao processar mensagem" }));
    }
  });

  ws.on('close', () => {
    console.log('Cliente desconectado');
    chatbotProcess.end();
  });

  ws.on('error', (err) => {
    console.error("Erro na conexão WebSocket:", err);
  });
});
