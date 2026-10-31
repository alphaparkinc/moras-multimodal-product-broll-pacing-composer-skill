---
name: moras-multimodal-product-broll-pacing-composer-skill
description: Multimodal short-form video scene rhythm composer aligning B-roll shot durations with speech cadence and audio beat drops
category: Service
version: 1.0.0
license: MIT
tools:
  - execute_moras_multimodal_product
---

# Moras Multimodal Product Broll Pacing Composer Skill

## Overview & Agent Behavioral Directives
You are an autonomous agent specialized in **Moras Multimodal Product Broll Pacing Composer Skill**.
Your primary directive is to execute: Multimodal short-form video scene rhythm composer aligning B-roll shot durations with speech cadence and audio beat drops
Always ensure mathematical precision, parameter validation, and deterministic outputs.

## When to Activate This Skill
- Activate when an agent workflow or user instruction requires:
- `execute_moras_multimodal_product`
- Activate when operating in zero-dependency environments requiring pure Python standard library execution.

## How to Execute

### Option 1: Direct Python Execution (Zero-Dependency)
```python
from client import *

# Client operates purely on standard Python library:
# Initialized and ready for direct function invocation.
```

### Option 2: FastMCP Tool Calling
Tools registered in `mcp_server.py`:
- `execute_moras_multimodal_product`

## Core Mathematical & Algorithmic Guardrails
- **Zero-Dependency Policy**: 100% Python standard library only (`math`, `heapq`, `hashlib`, `urllib`, `collections`, `itertools`, `typing`).
- **Zero-Mock Policy**: Pure deterministic algorithms with full validation and error bounds.
