# AI Chatbot with RAG System

A modern chatbot application built with Flask and LlamaIndex, featuring a RAG (Retrieval-Augmented Generation) system for intelligent responses based on your documents.

## Features

- 🤖 Advanced RAG-powered chatbot using LlamaIndex
- 🎨 Modern UI with glassmorphism design
- 🌓 Dark/Light mode toggle
- ✨ Smooth animations and transitions
- 📱 Fully responsive design
- ⚡ Real-time message updates
- 💬 Typing indicators
- 🔍 Document-based responses

## Tech Stack

- **Frontend:**
  - HTML5
  - CSS3
  - JavaScript
  - Bootstrap 5
  - Font Awesome icons

- **Backend:**
  - Flask
  - LlamaIndex
  - Hugging Face Embeddings
  - Groq LLM

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- A Groq API key

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd <repository-name>
```

2. Install the required Python packages:
```bash
pip install llama-index-core llama-index-embeddings-huggingface llama-index-llms-groq flask transformers torch
```

3. Create a `data` directory in the project root:
```bash
mkdir data
```

4. Add your documents to the `data` directory. These documents will be used by the RAG system to generate responses.

5. Update the Groq API key in `app.py`:
```python
Settings.llm = Groq(model="llama3-70b-8192", api_key="your-api-key-here")
```

## Usage

1. Start the Flask application:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

3. Start chatting! The chatbot will use the documents in your `data` directory to generate informed responses.

## Features in Detail

### RAG System
- Uses LlamaIndex for document processing and retrieval
- Integrates with Hugging Face embeddings for semantic search
- Powered by Groq's LLM for high-quality responses

### User Interface
- Clean and modern design with glassmorphism effects
- Smooth message animations
- Real-time typing indicators
- Dark/Light mode for comfortable viewing
- Mobile-responsive layout
- Intuitive message input with send button and Enter key support

## Project Structure

```
.
├── app.py              # Flask application and RAG system
├── templates/          # HTML templates
│   └── index.html     # Main chat interface
├── data/              # Directory for your documents
└── README.md          # Project documentation
```

## Customization

### Changing the Theme
The UI uses CSS variables for easy theme customization. You can modify the colors in `index.html`:

```css
:root {
    --primary-color: #7c3aed;
    --chat-bg-light: #ffffff;
    --chat-bg-dark: #1a1a1a;
    --text-light: #333333;
    --text-dark: #ffffff;
}
```

### Modifying the RAG System
You can adjust the RAG system settings in `app.py`:
- Change the embedding model
- Modify the LLM parameters
- Customize the document processing

## Troubleshooting

1. **ModuleNotFoundError**: Make sure all required packages are installed using pip
2. **API Key Error**: Verify your Groq API key is correctly set
3. **No Documents Found**: Ensure you have added documents to the `data` directory

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details. 