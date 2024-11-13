import { Socket } from "node:net";

import config from "../../config.json";

const serverPort = config.server_port;

const clientSocket = new Socket();

const args = process.argv;

clientSocket.connect({ port: serverPort }, () => {
	console.log(`Connect to port: ${serverPort}`);

	const dataToSend = {
		method: args[2],
		params: args.slice(3),
	};

	clientSocket.write(JSON.stringify(dataToSend));
});

clientSocket.addListener("data", (data) => {
	const response = JSON.parse(data.toString());

	if (Object.prototype.hasOwnProperty.call(response, "error")) {
		console.error(`Received error: ${response.error}`);
	} else if (Object.prototype.hasOwnProperty.call(response, "result")) {
		console.log(`Received result: ${response.result}`);
	}

	clientSocket.end();

	return;
});

clientSocket.on("error", (error) => {
	console.error(`Socket error: ${error}`);

	return;
});
