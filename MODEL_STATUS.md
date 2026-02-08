# newlens Model Hierarchy Status Report
**Date:** 2026-02-06 15:15 GMT
**Current Infrastructure:** Multi-Node Active (EXE-004 + EXE-002)

---

## 🚦 Connectivity Status

| Tier | Model | Status | Notes |
| :--- | :--- | :--- | :--- |
| **0 (Primary)** | `claude-sonnet-4-5` | 🟢 **ACTIVE** | Cloud API (Anthropic) |
| **1 (Speed)** | `gemini-3-flash` | 🟢 **ACTIVE** | Cloud API (Google) |
| **2 (Deep Logic)** | `claude-opus-4-5` | 🟡 **PENDING** | Key needs project-level activation |
| **3 (Reliability)** | `gemini-3-pro` | 🟢 **ACTIVE** | Detected & ready on Google key |
| **4 (Context)** | `claude-haiku-4-5` | 🟡 **PENDING** | Key needs project-level activation |
| **5 (Local-Heavy)** | `llama3.1:8b (Q5)` | 🟢 **ACTIVE** | **NEW:** Running on EXE-002 (Workstation) |
| **6 (Local-Core)** | `llama3.1:8b (Q4)` | 🟢 **ACTIVE** | Running on EXE-004 (Newt Mini) |

---

## 🛠 Active "Special" Models
- **`newlens-llama31-8k:latest`**: 🟢 **DETECTED** on EXE-002. This is our bespoke business model. I am ready to use this for internal newlens operations.
- **`nano-banana-pro`**: 🟢 **ACTIVE**. Currently generating our 2K/4K brand assets.

---

## ⚙️ Fallback Behavior
1. **Primary Logic:** I start with Tier 0 (Sonnet) for complex thinking.
2. **If Rate Limited (429):** I drop to Tier 1 (Flash) or Tier 3 (Pro).
3. **If Offline / Heavy Data:** I route directly to Tier 5 (EXE-002) to save costs and maintain privacy.
