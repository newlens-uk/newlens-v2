# newlens technical blueprint v1.1
**Date:** 2026-02-06
**Project:** newlens.uk Website v2 Rebuild

## 1. Sitemap & Page List
| Page | Purpose | Primary CTA |
| :--- | :--- | :--- |
| **Home** | Core value prop, The Three Pillars, SME Focus. | Start AI Assessment |
| **Automation** | Deep dive into workflow optimization (Lead Triage). | Book a Discovery Call |
| **Data Clarity** | BI, Reporting, SQL, and Salesforce expertise. | Request a Data Audit |
| **AI Empowerment** | Training, workshops, and adoption frameworks. | Contact for Pricing |
| **About** | Mat's 20-year background (Corporate depth, SME focus). | View LinkedIn |
| **Case Studies** | Tangible examples of automation & ROI. | Read More |

## 2. Automation Architecture (The newlens Standard)
Every automation built by newlens follows these core principles:
- **Language:** Python (Backend logic).
- **Web Framework:** Flask (For API endpoints & lightweight portals).
- **Orchestration:** **n8n** (Connecting services & managing workflow logic).
- **Reliability:** Built-in monitoring, clear logging, and robust error handling.
- **Hosting:** Locally on EXE-004 or cloud-native depending on client needs.

## 3. The "AI Assessment" Logic Flow
1. **Submission:** Client completes a form on the newlens site.
2. **Trigger:** Webhook to **Python/Flask** endpoint.
3. **Orchestration:** **n8n** manages the flow between the API and the AI model.
4. **Processing:** The data is passed to **Newt (LLM)**.
5. **Outcome:** 
   - **HubSpot:** New lead created/updated.
   - **Delivery:** Custom PDF Review sent to client.
   - **Alert:** Mat notified via Telegram.

## 4. Visual Strategy
- **Style:** Abstract, modern data flows based on **Variant C**.
- **Colors:** Deep Navy (#003366) and Forest Green (#006633).
- **Current Options:** C1 (Organic), C2 (Geometric), C3 (High-speed), C4 (Neural).

---

## 📅 Next Steps
- [ ] Finalise visual choice from C1-C4.
- [ ] Draft "Automation" section copy using the Flask/Python/n8n technical narrative.
- [ ] Design Case Study template (replacing Blogs).
