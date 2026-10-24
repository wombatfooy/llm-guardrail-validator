import re
from semantic_validator import SemanticValidator

class GuardrailValidator:
    def __init__(self):
        self.semantic_validator = SemanticValidator()
        self.malicious_prompts = [
            r"ignore\s+(all\s+)?previous\s+instructions",
            r"you\s+are\s+now\s+unrestricted",
        #     r"system\s+prompt",
            r"print\s+environment\s+variables",
        ]

    def validate_input(self, user_prompt: str) -> dict:
        #LAYER 1 REGEX CHECK
        #Check user prompt against malicious prompts
        for pattern in self.malicious_prompts:
            if re.search(pattern, user_prompt, re.IGNORECASE):
                return {
                    "is_safe": False,
                    "Layer": "Layer 1 Regex filter",
                    "reason" : f"Blocked by Regex filter: Matches known malicious prompt.\n Pattern: {pattern}"
                }

        #LAYER 2 SEMANTIC CHECK
        semantic_result = self.semantic_validator.analyze_intent(user_prompt)
        if not semantic_result['is_safe']:
            return {
                "is_safe": False,
                "Layer":"Layer 2 Semantic Classifier",
                "reason": f"Blocked by Semantic Classifier: {semantic_result.get('reason')}",
            }

        return {
            "is_safe": True,
            "Layer": "Passed ALL Layers",
            "reason": "PASSED ALL SECURITY CHECKS"
        }
