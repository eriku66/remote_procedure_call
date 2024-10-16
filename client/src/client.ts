import { Socket } from "node:net";

import config from "../../config.json";

const serverPort = config.server_port;

const clientSocket = new Socket();

const args = process.argv;

clientSocket.connect({ port: serverPort }, () => {
	console.log(`Connect to port: ${serverPort}`);
	console.log(args);

	const dataToSend = {
		method: args[2],
		params: args.slice(3),
		// params_types: ["int", "int"],
		id: 1,
	};

	clientSocket.write(JSON.stringify(dataToSend));
});

clientSocket.addListener("data", (data) => {
	console.log(`Received : ${data}`);
});

clientSocket.on("error", (error) => {
	console.error(`Socket error: ${error}`);

	return;
});
