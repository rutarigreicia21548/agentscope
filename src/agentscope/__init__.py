# -*- coding: utf-8 -*-
"""AgentScope - A flexible multi-agent framework."""

from .version import __version__
from .agent import AgentBase
from .message import Msg
from . import models
from . import agents
from . import pipelines


def init(
    model_configs=None,
    project=None,
    name=None,
    save_dir="./runs",
    save_log=True,
    save_code=False,
    logger_level="WARNING",
):
    """Initialize AgentScope with the given configuration.

    Args:
        model_configs (list or dict, optional):
            A list of model configurations or a single model configuration
            dict. Each configuration should contain at least a
            ``model_type`` field.
        project (str, optional):
            The project name for the current run.
        name (str, optional):
            The name for the current run.
        save_dir (str, optional):
            The directory to save logs and artifacts. Defaults to
            ``"./runs"``.
        save_log (bool, optional):
            Whether to save the log to file. Defaults to ``True``.
        save_code (bool, optional):
            Whether to save the code snapshot. Defaults to ``False``
            (disabled for personal use to reduce clutter).
        logger_level (str, optional):
            The logging level. Defaults to ``"WARNING"`` to keep output
            clean during personal experiments. Use ``"INFO"`` for more
            helpful messages or ``"DEBUG"`` for verbose output.
    """
    from .manager import ASManager

    ASManager.get_instance().initialize(
        model_configs=model_configs,
        project=project,
        name=name,
        save_dir=save_dir,
        save_log=save_log,
        save_code=save_code,
        logger_level=logger_level,
    )


__all__ = [
    "__version__",
    "init",
    "AgentBase",
    "Msg",
    "models",
    "agents",
    "pipelines",
]
