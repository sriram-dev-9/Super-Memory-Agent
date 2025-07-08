from langchain_core.tools import tool
from supermemory import Supermemory
import datetime
from dotenv import load_dotenv
import requests
import os

load_dotenv()

client = Supermemory()



@tool
def memory_store_tool(title:str,content:str, storage_type: str):
    """Tool for storing information into the supermemory"""
    metadata = {
        "type":storage_type,
        "timestamp": datetime.datetime.now().isoformat(),
        "title": title or f"Memory from {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "containerTags": 'MemoryAgent'
    }
    try:
        result = client.memories.add(
            content = content,
            metadata = metadata
        )
        return f"Successfully stored in memory with id: {getattr(result, 'id', 'unknown')}"
    except Exception as e:
        return f"Error storing in memory: {e}"



@tool
def memory_search_tool(query:str):
    """Tool for searching memory, give a proper query"""
    try:
        url = "https://api.supermemory.ai/v3/search"

        payload = {"q": f"{query}"}
        token = os.getenv("SUPERMEMORY_API_KEY")
        headers = {
                    "Authorization": f"Bearer {token}",
                    "Content-Type": "application/json",
                    "containerTags": "MemoryAgent"
                    }
        response = requests.request("POST", url, json=payload, headers=headers)
        return (response.text)
    except Exception as e:
        return f"Error Searching: {e}"

@tool
def update_memory_tool(id:str,content:str, title:str, storage_type:str):
    """Tool for updating exisiting memory, give the parameters to be updated"""
    metadata = {
        "type":storage_type,
        "timestamp": datetime.datetime.now().isoformat(),
        "title": title or f"Memory from {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "containerTags": 'MemoryAgent'
    }
    try:
        result = client.memories.update(
            id = id,
            content=content,
        )
        return f"Successfully updated the memory of id: {getattr(result, 'id', 'unknown')}"
    except Exception as e:
        return f"Error updating memory: {e}"

@tool
def delete_memories_tool(id:str):
    """Tool to delete or forget a memory, takes in the id of that particular memory and deletes it"""
    try:
        result = client.memories.delete(id)
        return f"Succesfully deleted : {result}"
    except Exception as e:
        return f"Failed to delete memory : {e}"
@tool
def list_memories_tool():
    """Returns a list of all memories along with their IDs."""


tools = [memory_store_tool,memory_search_tool,update_memory_tool]