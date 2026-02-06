# newlens technical blueprint v1.0
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
| **Blog** | Thought leadership, AI tips, local SME success stories. | Subscribe |

## 2. Tech Stack Recommendations
- **Hosting:** **Framer** or **Webflow** (Recommended). Faster and more modern than Squarespace, allowing easier integration with custom logic. 
- **Domain:** `newlens.uk` (already owned).
- **Backend (The "Brains"):** **n8n** or **Python** (running on EXE-004) to handle the Questionnaire logic.
- **CRM:** **HubSpot** (connected via API).

## 3. The "AI Assessment" Logic Flow
This is the heart of the "Automation-First" lead magnet.

1. **Submission:** Client completes a 5-question form on the newlens site.
2. **Trigger:** Webhook sends data to an **n8n workflow** on EXE-004.
3. **Processing:** The data is passed to **Newt (LLM)** with a specific "Consultant" prompt.
4. **Output:** I generate a structured "AI Readiness Review" (PDF or Email).
5. **Action:** 
   - **Lead Created:** Data automatically pushed to **HubSpot**.
   - **Delivery:** Custom review sent to the client via email.
   - **Notification:** Mat gets a Telegram alert that a high-value lead is ready.

## 4. Visual Strategy
- **Core Hero Art:** The "Final Blend" (Lens + Data Flow).
- **Section Variants:** Unique variations of the core art for each Pillar:
  - *Automation:* Lens focusing on gear/cog-like data flows.
  - *Data Clarity:* Lens focusing on structured grid/charts.
  - *AI Empowerment:* Lens focusing on a human-like neural network.

---

## 📅 Next Steps
- [ ] Finalise Core Hero Image (Blend of Original + Variant C).
- [ ] Draft Detailed "Automation" Service Copy.
- [ ] Map out specific HubSpot API requirements.
