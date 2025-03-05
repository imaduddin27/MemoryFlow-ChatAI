# **MemoryFlow: Conversational AI with Memory Management**

This repository contains two scripts that demonstrate the use of LangChain and LangGraph for building conversational AI applications with memory capabilities.

## 1. `memory_langchain.ipynb`

### Description
This Jupyter notebook demonstrates the use of LangChain's memory modules to create a conversational AI that can remember past interactions. The notebook covers different types of memory, including:

- **ConversationBufferMemory**: Stores the entire conversation history.
- **ConversationSummaryMemory**: Summarizes past interactions to save memory.
- **ConversationBufferWindowMemory**: Keeps a sliding window of the most recent interactions.
- **ConversationSummaryBufferMemory**: Combines the benefits of buffer and summary memory by keeping recent interactions in memory and summarizing older ones.

### Usage
1. Install the required dependencies using the `requirements.txt` file:
```commandline
pip install -r requirements.txt
```

2. Set up your environment variables in a .env file:
```commandline
GROQ_API_KEY=your_groq_api_key
```

3. Run the notebook in your Jupyter environment:
```commandline
jupyter notebook memory_langchain.ipynb
```



## 2. `langGraph_memory.py`

### Description
This Python script demonstrates the use of LangGraph to create a conversational AI with memory capabilities. The script uses LangGraph's MemorySaver to persist conversation states across sessions, allowing the AI to remember past interactions.

### Usage

1. Install the required dependencies using the `requirements.txt` file:
```commandline
pip install -r requirements.txt
```

2. Set up your environment variables in a .env file:
```commandline
GROQ_API_KEY=your_groq_api_key
```

3. Run the script: 
```commandline
python langGraph_memory.py
```

## Key Features
- **MemorySaver**: Persists conversation states across sessions.
- **StateGraph**: Manages the flow of the conversation.
- **ChatGroq**: Uses the Groq API for generating responses.

## How It Works
- The script initializes a LangGraph workflow with a `MessagesState` schema.
- It defines a node that calls the Groq model to generate responses.
- The conversation state is saved using `MemorySaver`, allowing the AI to remember past interactions.


## Example Interaction
```commandline
Chat started! Type 'quit' to exit.
--------------------------------------------------

You: Hi! My name is Sarah.
AI: Hello Sarah! How can I assist you today?

You: I’m planning a trip to Italy. Any tips?
AI: Sure, Sarah! Italy is amazing. Here are some tips:
   - Visit **Rome** for its ancient history and iconic landmarks like the Colosseum.
   - Try authentic **pizza** in Naples.
   - Don’t miss the **canals** and **gondola rides** in Venice.

You: What about food in Rome?
AI: In Rome, Sarah, you must try:
   - **Pasta Carbonara**: A classic Roman dish with eggs, cheese, and pancetta.
   - **Gelato**: Italian ice cream, perfect for dessert.
   - **Supplì**: Fried rice balls with mozzarella inside.

You: Can you remind me of the cities you mentioned earlier?
AI: Of course, Sarah! Earlier, I recommended these cities in Italy:
   - **Rome**: For ancient history and landmarks.
   - **Naples**: For authentic pizza.
   - **Venice**: For canals and gondola rides.

You: Thanks! I’ll start with Rome.
AI: Great choice, Sarah! Rome is a fantastic place to begin your Italian adventure. Let me know if you need more tips!
```

You: quit
Goodbye, Sarah! Have a wonderful trip!



