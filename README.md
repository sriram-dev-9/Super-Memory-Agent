Personal Agent with Supermemory

./SuperMemoryAgentBanner.png

Overview
This project implements a Personal Agent with a "supermemory" feature, utilizing the LangGraph framework and powered by a language model. The agent can store, search, update, and delete memories using custom tools integrated with the Supermemory API. It supports interactive conversations, maintaining a conversation history and processing user commands in a streamlined workflow. This project serves as a flexible foundation for building advanced agents and can be adapted for various projects or products.
Features

Conversational Agent: Engages in interactive dialogues with users, powered by a language model.
Supermemory Integration: Stores, searches, updates, and deletes memories using the Supermemory API.
Tool-Based Architecture: Utilizes custom tools for memory management, integrated with LangGraph for state management.
Environment Configuration: Uses .env for secure API key management.
Flexible LLM Support: Compatible with any LLM supported by LangChain, including OpenAI GPT-4.1-mini (default), Google Gemini, or others like Anthropic Claude or Meta LLaMA.

Use Cases
This project can serve as a basis for building advanced agents and products, such as:

Personal Knowledge Assistants: Create a tailored assistant to manage personal notes, schedules, or research data with memory persistence.
Customer Support Agents: Adapt the agent for customer service, storing and retrieving interaction histories to provide personalized support.
Educational Tools: Build a study companion that stores learning materials and quizzes users based on past interactions.
Task Automation Systems: Extend the agent to automate workflows by integrating with external APIs and storing task-related memories.
Mental Health Companions: Develop a supportive agent that tracks mood or journal entries, offering personalized responses based on memory searches.

Requirements

Python 3.8+
Dependencies (install via pip install -r requirements.txt):
langgraph
langchain-core
langchain-openai
langchain-google-genai (optional, for Gemini support)
python-dotenv
requests
Supermemory client library (custom or provided)


API Keys:
Supermemory API key (SUPERMEMORY_API_KEY)
LLM provider API key (e.g., OpenAI, Google, or other LangChain-supported providers)



Installation

Clone the repository:git clone https://github.com/sriram-dev-9/Super-Memory-Agent.git
cd Super-Memory-Agent


Create a virtual environment and activate it:python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install dependencies:pip install -r requirements.txt


Create a .env file in the project root and add your API keys:SUPERMEMORY_API_KEY=your_supermemory_api_key
OPENAI_API_KEY=your_openai_api_key
# GOOGLE_API_KEY=your_google_api_key (optional, for Gemini)


Ensure the Supermemory client library is available or installed as per its documentation.

Usage

Run the main script:python main.py


Enter commands at the Command: prompt to interact with the agent.
Available commands include:
Storing memories: e.g., "Store a memory about my meeting today"
Searching memories: e.g., "Search for memories about meetings"
Updating memories: e.g., "Update memory with ID  to include new details"
Listing memories: e.g., "List all memories"
Deleting memories: e.g., "Delete memory with ID "


Type exit to quit the program.

Project Structure

main.py: Main script containing the LangGraph setup, agent logic, and conversation loop.
tools.py: Defines custom tools for memory management (store, search, update, delete, list).
.env: Environment file for storing API keys (not tracked in version control).
requirements.txt: Lists project dependencies.

How It Works

Agent State: Managed using a TypedDict (AgentState) with a message sequence that supports conversation history.
LangGraph Workflow:
The graph consists of two nodes: agent_node (for LLM interaction) and tool_node (for executing tools).
Conditional edges determine whether to continue to the tool node (if tool calls are detected) or end the conversation.


Tools:
memory_store_tool: Stores new memories with a title, content, and storage type.
memory_search_tool: Searches memories using a query via the Supermemory API.
update_memory_tool: Updates existing memories by ID.
delete_memories_tool: Deletes a memory by ID.
list_memories_tool: Lists all stored memories.


LLM Integration: The agent uses OpenAI GPT-4.1-mini by default but can be configured to use any LangChain-supported LLM.
Conversation Loop: Maintains a history of messages, processes user inputs, and streams responses in real-time.

Example Interaction
Command: Store a memory about my project meeting today
============================================================
== Assistant: Successfully stored in memory with id: 12345 ==
============================================================
Command: Search for memories about meetings
============================================================
== Assistant: Found memories: [{"id": "12345", "title": "Memory from 2025-07-08 21:00", "content": "Project meeting today"}] ==
============================================================
Command: exit

Customizing the LLM
To use a different LLM supported by LangChain:

Install the corresponding LangChain package (e.g., langchain-anthropic for Claude).
Update the llm configuration in main.py. For example, for Anthropic Claude:from langchain_anthropic import ChatAnthropic
llm = ChatAnthropic(model_name="claude-3-sonnet-20240229").bind_tools(tools=tools)


Ensure the appropriate API key is set in .env.

Contributing
Contributions are welcome! Please:

Fork the repository.
Create a feature branch (git checkout -b feature/your-feature).
Commit your changes (git commit -m "Add your feature").
Push to the branch (git push origin feature/your-feature).
Open a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for details.
