# Exploitation Report

# Executive Summary
The cybersecurity landscape is currently facing significant threats from multiple zero-day vulnerabilities being actively exploited across various platforms. Notably, Microsoft, SAP, and Fortinet have all released patches for critical zero-day vulnerabilities that have been exploited in the wild. Additionally, new attack vectors have emerged, such as the "Branch Privilege Injection" flaw in Intel CPUs, which poses a severe risk to data confidentiality. Threat actors, particularly those linked to China, are actively exploiting these vulnerabilities to target critical infrastructure and supply chains, emphasizing the need for immediate patching and enhanced security measures.

## Active Exploitation Details

Several zero-day vulnerabilities are being actively exploited:
1. **Microsoft Windows**: Five zero-day vulnerabilities, including a browser-led remote code execution (RCE) flaw, have been patched. These vulnerabilities were actively exploited before the release of the patches.
2. **SAP NetWeaver**: A critical zero-day vulnerability (CVE-2025-31324) has been exploited by China-linked APTs to breach critical systems globally.
3. **Fortinet FortiVoice**: A critical RCE vulnerability was exploited as a zero-day, prompting Fortinet to release urgent patches.
4. **Ivanti EPMM**: Two zero-day vulnerabilities were chained in attacks to achieve RCE, necessitating immediate patching.
5. **Intel CPUs**: The "Branch Privilege Injection" flaw allows attackers to leak sensitive data from privileged memory, affecting all modern Intel CPUs.

## Affected Systems and Products

- **Microsoft Windows**: All systems running unpatched versions of Windows are affected by the zero-day vulnerabilities.
- **SAP NetWeaver**: Systems running SAP NetWeaver are vulnerable to CVE-2025-31324.
- **Fortinet FortiVoice**: Enterprise phone systems using FortiVoice are at risk.
- **Ivanti EPMM**: Systems using Ivanti Endpoint Manager Mobile are affected.
- **Intel CPUs**: All modern Intel CPUs are susceptible to the "Branch Privilege Injection" flaw.

## Attack Vectors and Techniques

- **Microsoft Windows**: Exploits are initiated via browser-led attacks, potentially through malicious websites or phishing emails.
- **SAP NetWeaver**: Exploitation involves unauthorized access to critical infrastructure networks, likely through network-based attacks.
- **Fortinet FortiVoice**: Attacks leverage remote code execution, possibly through exposed network interfaces.
- **Ivanti EPMM**: Attackers chain vulnerabilities to gain remote code execution, likely exploiting network access.
- **Intel CPUs**: The "Branch Privilege Injection" flaw is exploited to leak data from privileged memory, potentially through crafted software running on the CPU.

## Threat Actor Activities

s
- **China-Linked APTs**: These actors are exploiting SAP vulnerabilities to target critical infrastructure, indicating a focus on strategic geopolitical targets.
- **Tidrone**: A Chinese actor targeting Taiwanese drone manufacturers and their supply chains, using ERP software as an infection vector.
- **Unknown Actors**: Responsible for exploiting vulnerabilities in Microsoft, Fortinet, and Ivanti products, as well as distributing malicious packages on PyPI.

Security teams are advised to prioritize patching the identified vulnerabilities and monitor for any signs of exploitation within their networks. Enhanced security measures, such as network segmentation and intrusion detection systems, should be implemented to mitigate the risk of these sophisticated attacks. 