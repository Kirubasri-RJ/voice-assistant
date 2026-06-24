SIMPLE VOICE ASSISTANT
A basic Python voice assistant that listens to spoken commands and responds with speech. Built as Task 4 of my internship at Codmetric.

FEATURES
-  Captures voice input using speech recognition
-  Responds with audible text-to-speech
-  Tells the current time
-  Tells today's date
-  Tells a random joke
-  Responds to greetings (hello/hi)
-  Exits gracefully on "bye"/"exit"/"goodbye"

TECH STACK
- **Python 3**
- [`SpeechRecognition`](https://pypi.org/project/SpeechRecognition/) — captures and converts voice to text
- [`pyttsx3`](https://pypi.org/project/pyttsx3/) — converts text responses to speech (offline)
- [`PyAudio`](https://pypi.org/project/PyAudio/) — microphone input support

HOW IT WORKS
1. The assistant greets the user and starts listening.
2. It captures audio from the microphone and converts it to text using Google's speech recognition.
3. The text is matched against a set of known commands.
4. A matching response is generated and spoken aloud.
5. The loop continues until the user says "exit," "bye," or "goodbye."

SETUP AND INITIALIZATION

bash
# Clone the repo
git clone https://github.com/your-username/voice-assistant-task4.git
cd voice-assistant-task4

# Install dependencies
pip install -r requirements.txt

# Run the assistant
python voice_assistant.py

EXAMPLE COMMANDS
| You say | Assistant responds |
| "Hello" | Greets you back |
| "What time is it?" | Tells the current time |
| "What's the date?" | Tells today's date |
| "Tell me a joke" | Tells a random joke |
| "Exit" / "Bye" | Ends the program |

DEMO
See Voice assistant output.png for a sample terminal run showing recognized commands and spoken responses.

FUTURE IMPROVEMENTS
- Add more commands (weather, reminders, etc.)
- Support offline speech recognition
- Add a simple GUI

*Built as part of the Codmetric internship program.*
