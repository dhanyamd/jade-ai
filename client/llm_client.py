from typing import Any
from openai import AsyncOpenAI

from .config import Config

class LLMClient:
    def __init__(self, config: Config) -> None:
        self._client: AsyncOpenAI | None = None
        self.max_retries : int = 3
        self.config = config
    
    def get_client(self) -> AsyncOpenAI: 
        if self._client is None: 
            self._client = AsyncOpenAI(
                api_key=self.config.api_key,  
                base_url=self.config.base_url,
            )
        return self._client 
    
    async def close(self) -> None: 
        if self._client: 
            await self._client.close() 
            self._client = None 
    
    def _build_tools(self, tools: list[dict[str, Any]]): 
        return [
            {
                "type": "function",
                "function": {
                    "name": tool["name"],
                    "description": tool.get("description", ""),
                    "parameters": tool.get(
                        "parameters",
                        {
                            "type": "object",
                            "properties": {},
                        },
                    ),
                },
            }
            for tool in tools
        ]
        