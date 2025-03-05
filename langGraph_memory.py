import uuid
from langchain.schema import HumanMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, MessagesState, StateGraph
from langchain_groq import ChatGroq 
from dotenv import load_dotenv

load_dotenv()
llm = ChatGroq(model="llama-3.2-90b-vision-preview")

def create_chat_app():
    # Define a new graph
    workflow = StateGraph(state_schema=MessagesState)

    model=ChatGroq()

    # Define the function that calls the model
    def call_model(state: MessagesState):
        response = model.invoke(state["messages"])
        return {"messages": response}

    # Define the nodes we will cycle between
    workflow.add_edge(START, "model")
    workflow.add_node("model", call_model)

    # Add memory
    memory = MemorySaver()

    # Compile the workflow
    app = workflow.compile(checkpointer=memory)
    return app

def chat():
    # Create the app
    app = create_chat_app()

    # Create a unique thread ID for this conversation
    thread_id = uuid.uuid4()
    config = {"configurable": {"thread_id": thread_id}}

    print("Chat started! Type 'quit' to exit.")
    print("-" * 50)

    while True:
        # Get user input
        user_input = input("\nYou: ")

        # Check if user wants to quit
        if user_input.lower() == 'quit':
            print("\nGoodbye")
            break

        # Crerate message and get response
        input_message = HumanMessage(content=user_input)

        try:
            response = None
            # stream the response
            for event in app.stream(
                {"messages": [input_message]},
                config,
                stream_mode = "values"
            ):
                response = event["messages"][-1].content
            
            if response:
                print("\nAI:", response)

        except Exception as e:
            print(f"\nError: {str(e)}")
            print("please tray again")


if __name__ == "__main__":
    chat()