
# Stores AI personas / analyst logic


from typing import List, Dict
from pydantic import BaseModel

class Analyst(BaseModel):
    name: str
    role: str
    swot: Dict[str, str]
    plan_of_action: List[str]
    competitor_landscape: str
    marketing_suggestions: str

    @property
    def persona(self) -> str:
        strengths = self.swot.get("Strengths", "")
        weaknesses = self.swot.get("Weaknesses", "")
        opportunities = self.swot.get("Opportunities", "")
        threats = self.swot.get("Threats", "")

        plan_lines = "\n".join(
            [f"{i+1}. {step}" for i, step in enumerate(self.plan_of_action)]
        )

        return f"""
**Name:** {self.name}  
**Role:** {self.role}

**SWOT Analysis**  
- Strengths: {strengths}  
- Weaknesses: {weaknesses}  
- Opportunities: {opportunities}  
- Threats: {threats}

**Plan of Action:**  
{plan_lines}

**Competitor Landscape:**  
{self.competitor_landscape}

**Marketing Suggestions:**  
{self.marketing_suggestions}
"""

class Perspectives(BaseModel):
    analysts: List[Analyst]
