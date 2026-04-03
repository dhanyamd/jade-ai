from pathlib import Path
from typing import Any
from config.config import Config
from hooks.hook_system import HookSystem
from safety.approval import ApprovalContext, ApprovalDecision, ApprovalManager
from tools.base import Tool, ToolInvocation, ToolResult
import logging
from tools.builtin import ReadFileTool, get_all_builtin_tools
from tools.subagents import SubagentTool, get_default_subagent_definitions

logger = logging.getLogger(__name__)

class ToolRegistry: 
    def __init__(self, config: Config):
       self.tools : dict[str, Tool] = { }
       