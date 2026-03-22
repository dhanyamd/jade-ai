from __future__ import annotations
from typing import AsyncGenerator, Awaitable, Callable
from agent.events import AgentEvent, AgentEventType
from agent.session import Session
from client.response import StreamEventType, TokenUsage, ToolCall, ToolResultMessage
from config.config import Config
from prompts.system import create_loop_breaker_prompt
from tools.base import ToolConfirmation

class Agent: 
    def __init__(
        self,
        config: Config,
        confirmation_callback: Callable[[ToolConfirmation], bool] | None = None
    ):
        self.config = config 
        self.session: Session | None = Session(self.config)
        self.session.approval_manager.confirmation_callback = confirmation_callback 
    
    async def run(self, message:str): 
        await self.session.hook_system.trigger_before_agent(message)
        yield AgentEvent.agent_start(message) 
        self.session.context_manager.add_user_message(message)

        final_response: str | None = None 
        async for event in self._agentic_loop(): 
            yield event 
            if event.type == AgentEventType.TEXT_COMPLETE: 
                final_response = event.data.get("content")

        await self.session.hook_system.trigger_after_agent(message, final_response)
        yield AgentEvent.agent_end(final_response)