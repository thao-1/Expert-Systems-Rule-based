# Expert-Systems---Rule-based

### Key Components:

Rule Class: Represents individual rules with conditions and conclusions
KnowledgeBase Class: Stores and manages all rules
InferenceEngine Class: Handles the reasoning process using forward chaining
GPAExpertSystem Class: Main system that orchestrates everything

### Features:

Scalable Architecture: Easy to add new rules, attributes, or modify the inference logic
Forward Chaining: Matches facts against rules to derive conclusions
Explanation Capability: Shows which rule was applied for transparency
Case Insensitive: Handles input in any case
Extensible: Can easily add backward chaining, confidence factors, or multiple conclusions

### Rules Extracted from Your Diagram:

The system implements 8 rules based on the decision tree:

Blue + KIA + Burger → GPA < 2.5

Blue + KIA + Pizza → 2.4 < GPA < 3.1

Blue + Ford + Burger → 2.7 < GPA < 2.9

Blue + Ford + Pizza → 3.4 < GPA < 4.1

Green + KIA + Burger → 3.1 < GPA < 3.8

Green + KIA + Pizza → 2.3 < GPA < 3.9

Green + Ford + Burger → 3.7 < GPA < 4.2

Green + Ford + Pizza → 3.9 < GPA

### Usage:

The myExpertSystem(color, car, food) function is implemented as requested and returns the GPA range prediction. The system is highly scalable - you can easily add new attributes, rules, or inference methods by extending the existing classes.
