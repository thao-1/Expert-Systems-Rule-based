class Rule:
    """Represents a single rule in the expert system"""
    def __init__(self, conditions, conclusion):
        self.conditions = conditions  # Dictionary of attribute-value pairs
        self.conclusion = conclusion  # The resulting GPA range
    
    def matches(self, facts):
        """Check if this rule matches the given facts"""
        for attribute, value in self.conditions.items():
            if facts.get(attribute) != value:
                return False
        return True
    
    def __str__(self):
        conditions_str = " AND ".join([f"{attr}={val}" for attr, val in self.conditions.items()])
        return f"IF {conditions_str} THEN GPA={self.conclusion}"


class KnowledgeBase:
    """Stores all the rules for the expert system"""
    def __init__(self):
        self.rules = []
    
    def add_rule(self, rule):
        """Add a rule to the knowledge base"""
        self.rules.append(rule)
    
    def get_matching_rules(self, facts):
        """Get all rules that match the given facts"""
        return [rule for rule in self.rules if rule.matches(facts)]


class InferenceEngine:
    """Handles the reasoning process"""
    def __init__(self, knowledge_base):
        self.knowledge_base = knowledge_base
    
    def forward_chain(self, facts):
        """Forward chaining inference - find conclusion from facts"""
        matching_rules = self.knowledge_base.get_matching_rules(facts)
        
        if not matching_rules:
            return "No matching rule found"
        
        # Return the first matching rule's conclusion
        # In a more complex system, you might handle multiple matches differently
        return matching_rules[0].conclusion
    
    def explain(self, facts):
        """Provide explanation for the inference"""
        matching_rules = self.knowledge_base.get_matching_rules(facts)
        
        if not matching_rules:
            return "No matching rule found for the given facts"
        
        rule = matching_rules[0]
        return f"Applied rule: {rule}"


class GPAExpertSystem:
    """Main expert system class"""
    def __init__(self):
        self.knowledge_base = KnowledgeBase()
        self.inference_engine = InferenceEngine(self.knowledge_base)
        self._initialize_rules()
    
    def _initialize_rules(self):
        """Initialize the knowledge base with rules from the decision tree"""
        # Rules derived from the decision tree diagram
        rules = [
            # Blue car branch
            Rule({"color": "BLUE", "car": "KIA", "food": "BURGER"}, "GPA < 2.5"),
            Rule({"color": "BLUE", "car": "KIA", "food": "PIZZA"}, "2.4 < GPA < 3.1"),
            Rule({"color": "BLUE", "car": "FORD", "food": "BURGER"}, "2.7 < GPA < 2.9"),
            Rule({"color": "BLUE", "car": "FORD", "food": "PIZZA"}, "3.4 < GPA < 4.1"),
            
            # Green car branch
            Rule({"color": "GREEN", "car": "KIA", "food": "BURGER"}, "3.1 < GPA < 3.8"),
            Rule({"color": "GREEN", "car": "KIA", "food": "PIZZA"}, "2.3 < GPA < 3.9"),
            Rule({"color": "GREEN", "car": "FORD", "food": "BURGER"}, "3.7 < GPA < 4.2"),
            Rule({"color": "GREEN", "car": "FORD", "food": "PIZZA"}, "3.9 < GPA"),
        ]
        
        for rule in rules:
            self.knowledge_base.add_rule(rule)
    
    def predict_gpa(self, color, car, food):
        """Predict GPA range based on input attributes"""
        facts = {
            "color": color.upper(),
            "car": car.upper(),
            "food": food.upper()
        }
        
        return self.inference_engine.forward_chain(facts)
    
    def explain_prediction(self, color, car, food):
        """Explain how the prediction was made"""
        facts = {
            "color": color.upper(),
            "car": car.upper(),
            "food": food.upper()
        }
        
        return self.inference_engine.explain(facts)
    
    def list_all_rules(self):
        """List all rules in the knowledge base"""
        return [str(rule) for rule in self.knowledge_base.rules]


# Implementation of the required function
def myExpertSystem(color, car, food):
    """
    Main function that implements the expert system logic
    
    Args:
        color (str): Color preference (BLUE or GREEN)
        car (str): Car brand preference (KIA or FORD)
        food (str): Food preference (BURGER or PIZZA)
    
    Returns:
        str: Predicted GPA range
    """
    expert_system = GPAExpertSystem()
    return expert_system.predict_gpa(color, car, food)


# Example usage and testing
if __name__ == "__main__":
    # Create the expert system
    gpa_system = GPAExpertSystem()
    
    # Test cases
    test_cases = [
        ("BLUE", "KIA", "BURGER"),
        ("BLUE", "FORD", "PIZZA"),
        ("GREEN", "KIA", "BURGER"),
        ("GREEN", "FORD", "PIZZA"),
        ("BLUE", "KIA", "PIZZA"),
    ]
    
    print("=== GPA Expert System Test Results ===\n")
    
    for color, car, food in test_cases:
        prediction = gpa_system.predict_gpa(color, car, food)
        explanation = gpa_system.explain_prediction(color, car, food)
        
        print(f"Input: Color={color}, Car={car}, Food={food}")
        print(f"Prediction: {prediction}")
        print(f"Explanation: {explanation}")
        print("-" * 50)
    
    # Test the required function
    print("\n=== Testing myExpertSystem function ===")
    result = myExpertSystem("GREEN", "FORD", "PIZZA")
    print(f"myExpertSystem('GREEN', 'FORD', 'PIZZA') = {result}")
    
    # Display all rules
    print("\n=== All Rules in Knowledge Base ===")
    for i, rule in enumerate(gpa_system.list_all_rules(), 1):
        print(f"{i}. {rule}")