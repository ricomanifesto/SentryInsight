# Exploitation Report

Critical exploitation activity is currently targeting Citrix NetScaler devices with over 3,300 systems remaining vulnerable to the CitrixBleed 2 vulnerability nearly two months after patches were released. The Dutch National Cyber Security Centre has confirmed active exploitation of this critical flaw in critical sectors, allowing attackers to bypass authentication by hijacking user sessions. Additionally, a new cyber-espionage group called "Curly COMrades" has emerged, targeting government organizations in Georgia and Moldova using sophisticated COM hijacking techniques and custom backdoor malware for persistent access.

## Active Exploitation Details

### CitrixBleed 2 Vulnerability
- **Description**: Critical authentication bypass vulnerability in Citrix NetScaler ADC products that allows attackers to hijack user sessions
- **Impact**: Complete authentication bypass, unauthorized access to protected systems and data
- **Status**: Patches available but over 3,300 devices remain unpatched; actively exploited in critical sectors
- **CVE ID**: CVE-2025-6543

### NGEN COM Hijacking Vulnerability
- **Description**: COM hijacking technique exploiting the .NET Native Image Generator (NGEN) to maintain persistence through seemingly inactive scheduled tasks
- **Impact**: Long-term persistent access to compromised systems, stealth backdoor deployment
- **Status**: Actively exploited by Curly COMrades APT group in targeted espionage campaigns

## Affected Systems and Products

- **Citrix NetScaler ADC**: Over 3,300 unpatched devices worldwide vulnerable to session hijacking attacks
- **Government Organizations**: Entities in Georgia and Moldova targeted by custom malware campaigns
- **Critical Infrastructure**: Dutch NCSC reports exploitation in critical sectors including government and essential services
- **Windows Systems**: Targeted by COM hijacking attacks using NGEN scheduled task manipulation

## Attack Vectors and Techniques

- **Session Hijacking**: Exploitation of NetScaler authentication bypass to steal and reuse legitimate user sessions
- **COM Hijacking**: Abuse of .NET Native Image Generator to create persistent backdoors through scheduled tasks
- **Custom Malware Deployment**: Use of specialized backdoor tools designed for long-term access and data exfiltration
- **Targeted Espionage**: Focused attacks on government and critical infrastructure organizations

## Threat Actor Activities

- **Curly COMrades**: New APT group conducting cyber-espionage campaigns against government entities in Georgia and Moldova using custom backdoor malware and COM hijacking techniques for persistent access
- **Unknown Threat Actors**: Actively exploiting CitrixBleed 2 vulnerability across critical sectors, with confirmed attacks reported by Dutch cybersecurity authorities
- **RansomHub**: Claimed responsibility for attack on Manpower staffing agency affecting nearly 145,000 individuals
- **Interlock Ransomware Gang**: Confirmed as responsible for cyberattack on Saint Paul, Minnesota that disrupted city systems and services in July