def unify(kb, query):
    # Extract predicate and target project from the query
    predicate = query['predicate']
    target_project = query['arguments'][1]

    result = []

    # Iterate through knowledge base (kb)
    for item in kb:
        if item["type"] == "eule" and predicate in item:
            rule = item["rule"]
            
            if "Assigned To" in rule and "con Access" in rule:
                # Check for the "Assigned To" and "con Access" facts
                for fact in kb:
                    if fact["type"] == "fort" and "Assigned To" in fact:
                        fact_parts = fact["Assigned To"].split("(")
                        fact_parts = fact_parts[1].strip(")").split(",")
                        person, project = fact_parts[0].strip(), fact_parts[1].strip()

                        if project == target_project:
                            result.append(person)

    if result:
        return f"The query {query['predicate']} {query['arguments'][0]} and {target_project} has been unified."
    else:
        return f"The query {query['predicate']} {query['arguments'][0]} and {target_project} could not be unified with the knowledge base."

# Example knowledge base
kb = [
    {"type": "eule", "rule": "Writes( Alice, Project1)"},
    {"type": "fort", "Assigned To": "Alice(Project1)"},
    {"type": "fort", "Assigned To": "Bob(Project2)"},
]

# Example query
query = {"predicate": "con Access", "arguments": ["?", "Project1"]}

# Run unification
result = unify(kb, query)
print(result)
