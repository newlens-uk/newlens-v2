import os
import json
import logging
from typing import Dict, Any, List

# Configure logging for "Industrial Grade" reliability
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("newlens_automation.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("newlens_assessment")

class NewlensAssessmentEngine:
    """
    The 'Brain' of the newlens AI Readiness Review tool.
    Processes the 7-point SME questionnaire to generate high-value insights.
    """
    
    def __init__(self, hubspot_token: str):
        self.hubspot_token = hubspot_token
        logger.info("newlens Assessment Engine v1.1 (7-Point logic) initialized.")

    def process_submission(self, data: Dict[str, Any]) -> str:
        """
        Main entry point for n8n webhook data.
        """
        try:
            email = data.get('email', 'Unknown')
            logger.info(f"Processing 7-point submission for: {email}")
            
            # 1. Logic: Calculate nuance-based readiness
            readiness_score = self._calculate_readiness(data)
            
            # 2. LLM Prompt Construction for Newt
            review_prompt = self._build_consultant_prompt(data, readiness_score)
            
            # 3. HubSpot Sync (Log the intent)
            self._update_hubspot(data, readiness_score)
            
            return review_prompt
            
        except Exception as e:
            logger.error(f"Error in assessment logic: {str(e)}")
            return "ERROR: Review generation failed. System logged for human review."

    def _calculate_readiness(self, data: Dict[str, Any]) -> int:
        """
        Calculates a score from 0-100.
        Higher manual hours = Lower score (Higher need).
        Existing AI usage = Higher score (Higher readiness).
        """
        score = 50 # Baseline
        
        # Manual Hours Weighting
        hours_map = {
            "<2 hours": +10,
            "2-5 hours": 0,
            "5-10 hours": -15,
            "10+ hours": -30
        }
        score += hours_map.get(data.get('manual_hours'), 0)
        
        # AI Temperature Weighting
        ai_map = {
            "Not at all": -10,
            "Occasionally for emails": 0,
            "Deeply integrated into workflows": +20,
            "Shadow AI": +5
        }
        score += ai_map.get(data.get('ai_usage'), 0)
        
        return max(0, min(100, score))

    def _build_consultant_prompt(self, data: Dict[str, Any], score: int) -> str:
        return f"""
        Role: Senior newlens Automation Consultant
        Client Persona: {data.get('name')} from {data.get('company')}
        
        Input Data (7-Point Assessment):
        1. Manual Pain: {data.get('manual_hours')} per week.
        2. Primary Bottleneck: {data.get('bottleneck')}
        3. Tech Stack: {data.get('tools')}
        4. Current AI Usage: {data.get('ai_usage')}
        5. Barrier to Entry: {data.get('obstacle')}
        6. Personal/Business Goal: {data.get('ambition')}
        7. Calculated Readiness Score: {score}/100
        
        Task: 
        Write a professional, encouraging, and highly specific 'AI Readiness Review'.
        Structure the response as:
        - EXECUTIVE SUMMARY: (Calculate estimated time recovery based on their hours).
        - BOTTLENECK ANALYSIS: (Address their '{data.get('bottleneck')}' specifically).
        - TOOLSET OPPORTUNITY: (How AI/Automation bridges their specific tools).
        - PRAGMATIC STEP 1: (A low-friction first project to hit their goal: '{data.get('ambition')}').
        
        Tone: Professional, Corporate-grade depth, yet accessible for an SME owner.
        Brand: newlens (all lowercase).
        """

    def _update_hubspot(self, data: Dict[str, Any], score: int):
        # Industrial standard: log before API call
        logger.info(f"HUB-SYNC: Syncing {data.get('name')} ({data.get('company')}) to HubSpot with Readiness: {score}")
        # API logic to follow

if __name__ == "__main__":
    # Test Payload mimicking the 7-question structure
    test_data = {
        "name": "Jane Doe",
        "company": "Suffolk Manufacturing Ltd",
        "email": "jane@suffolk-mfg.co.uk",
        "manual_hours": "10+ hours",
        "bottleneck": "Copying order data from PDF invoices into our inventory system",
        "tools": ["Outlook", "Xero", "Excel"],
        "ai_usage": "Occasionally for emails",
        "obstacle": "Lack of technical expertise",
        "ambition": "Spend more time on product development rather than admin"
    }
    
    engine = NewlensAssessmentEngine(hubspot_token="REDACTED")
    prompt = engine.process_submission(test_data)
    print("--- 7-POINT ASSESSMENT PROMPT ---")
    print(prompt)
