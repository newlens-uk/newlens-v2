# newlens Model Hierarchy & Fallback Logic (v1.0)
**Date:** 2026-02-06
**Objective:** Ensure 100% uptime and optimal cost/performance ratio for Newt's "brain".

---

## 🧠 The Hierarchy (Tiered Fallback)

| Tier | Model ID | Role / Priority |
| :--- | :--- | :--- |
| **0 (Primary)** | `anthropic/claude-sonnet-4-5` | Main reasoning, coding, and client-facing reviews. |
| **1 (Speed)** | `google/gemini-3-flash` | High-volume tasks, quick lookups, and initial triage. |
| **2 (Deep Logic)** | `anthropic/claude-opus-4-5` | Complex business logic and mission-critical architecture. |
| **3 (Reliability)** | `google/gemini-3-pro` | Stable secondary reasoning agent. |
| **4 (Long-Context)** | `anthropic/claude-haiku-4-5` | Large file processing and background summarization. |
| **5 (Local-Heavy)** | `local/exe-002-workstation` | High-privacy tasks and rate-limit bypass (DeepSeek/Llama). |
| **6 (Local-Core)** | `local/exe-004-newt` | Emergency recovery / Offline survival (Small local model). |

---

## ⚙️ Orchestration Strategy (n8n/Python)

1. **Auto-Switching:** If a `429 (Rate Limit)` or `503 (Overloaded)` is detected on Tier 0, the n8n workflow automatically re-routes the payload to Tier 1.
2. **Task Routing:** 
   - **Lead Generation reviews** → Always Tier 0 or Tier 2.
   - **Code/Refactoring** → Tier 0.
   - **Audit Logs/Routine updates** → Tier 1 or Tier 5.
3. **Cost Control:** Daily token quotas per tier to prevent budget runaway.
