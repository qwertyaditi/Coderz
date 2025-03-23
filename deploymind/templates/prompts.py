def make_prompt(vuln_data, code_snippet):
    return f"""
Vulnerability: {vuln_data['title']}
Severity: {vuln_data['severity']}
CVSS Score: {vuln_data['cvss']}

The following is a source code file content:

{code_snippet}

Please answer:
1. What does this vulnerability mean generally?
2. Does this code potentially suffer from this vulnerability? If yes, where?
3. How severe is the risk in this code context?
4. Suggest a safer approach or fix.
"""