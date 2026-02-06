# newlens Framer Build Guide (v1.0)
**Date:** 2026-02-06
**Status:** Architecture Draft

## 🛠 Project Setup
- **Project Name:** `newlens-v2-STAGING`
- **Color Palette:**
  - Primary Navy: `#003366`
  - Primary Green: `#006633` (as requested)
  - Text: `#22313F` (Grey)
  - Background: `#FFFFFF` (White)

## 📄 Page Architecture

### 1. Home Page (`/`)
- **Top Nav:** Logo (left), Services Dropdown, About, Case Studies, "Free Assessment" CTA (Primary Button).
- **Hero Section:** `premium-hero-1.png` background. Headline: "Data Clarity. Workflow Efficiency. AI-Powered Growth."
- **Services Grid:** Three clean cards for Automation, Data, and Empowerment.
- **The Assessment Hook:** Prominent section with a clean 5-field form.

### 2. Automation (`/services/automation`)
- **Visual:** `premium-hero-2.png` (macro lens focus).
- **Focus:** Lead Triage demo/workflow diagram.
- **CTA:** Book a Discovery Call.

### 3. Data Clarity (`/services/data`)
- **Visual:** Variant C2 (Geometric Grid) subtle background.
- **Focus:** Reporting Audits & Salesforce CRMA.
- **CTA:** Request a Data Audit.

### 4. About (`/about`)
- **Focus:** Mat's 20-year story. Corporate rigor meets SME agility.
- **CTA:** Connect on LinkedIn.

---

## ⚡ Form & HubSpot Logic
1. **Frontend:** Framer Form (Name, Email, Industry, Bottleneck, Goal).
2. **Logic Layer:** Webhook to `n8n` on EXE-004.
3. **AI Review:** Newt processes answers via LLM.
4. **HubSpot Sync:** `crm.objects.contacts` update.
5. **Delivery:** Automatic email with assessment PDF.
