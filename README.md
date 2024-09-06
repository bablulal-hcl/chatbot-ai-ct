# chatbot-ai-ct

## Install ollama and run
```bash
ollama --help
Large language model runner

Usage:
  ollama [flags]
  ollama [command]

Available Commands:
  serve       Start ollama
  create      Create a model from a Modelfile
  show        Show information for a model
  run         Run a model
  pull        Pull a model from a registry
  push        Push a model to a registry
  list        List models
  ps          List running models
  cp          Copy a model
  rm          Remove a model
  help        Help about any command

Flags:
  -h, --help      help for ollama
  -v, --version   Show version information

Use "ollama [command] --help" for more information about a command.
```

### Example Test with "llama3.1" AI model
```bash
$ ollama run llama3.1
>>> I am travelling to US. Do you have some products to recommend.
You're traveling to the US! Exciting times ahead!

Yes, I'd be happy to help with product recommendations tailored to your needs while traveling in the US. Please let me know what type of products you're interested in:

1. **Technology**:
	* Portable power banks for keeping devices charged
	* Travel adapters or converters for charging electronic devices
	* Noise-cancelling headphones for a more comfortable journey
2. **Travel accessories**:
	* Packable luggage (e.g., backpacks, duffel bags) for convenient carry-on and checked luggage
	* Packing cubes to help you organize your belongings
	* Travel wallets or pouches with RFID-blocking technology for secure identity storage
3. **Safety and security**:
	* Personal alarms or whistles to stay safe in crowded areas
	* Pepper spray (check local laws regarding use and possession)
	* A small first-aid kit for minor emergencies
4. **Health and wellness**:
	* Travel-sized pain relievers, antacids, or motion sickness medication
	* Hand sanitizer or baby wipes for germ-free cleaning
	* Portable water bottles with built-in filters (e.g., LifeStraw) for staying hydrated
5. **Miscellaneous**:

Please let me know which categories interest you, and I'll provide some specific product recommendations!

(Also, don't forget to check local laws and regulations regarding the products you're interested in.)


>>> /?
Available Commands:
  /set            Set session variables
  /show           Show model information
  /load <model>   Load a session or model
  /save <model>   Save your current session
  /clear          Clear session context
  /bye            Exit
  /?, /help       Help for a command
  /? shortcuts    Help for keyboard shortcuts

Use """ to begin a multi-line message.

>>> /bye
```

## In a new window
pip install -r requirements.txt
