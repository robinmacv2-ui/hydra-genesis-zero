"""
Paquete romeo_agent: gate ex-ante (DFA) + runtime offline.
Sin dependencias externas ni APIs cloud.
"""
from .admissible import is_admissible, VERBOS_ADMISIBLES

__all__ = ["is_admissible", "VERBOS_ADMISIBLES"]
