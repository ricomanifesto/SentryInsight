# Exploitation Report

# Executive Summary
Recent cybersecurity reports highlight several critical vulnerabilities and zero-day exploits affecting major systems and software. Notably, Fortinet's FortiVoice systems and SAP NetWeaver servers have been targeted by zero-day vulnerabilities, while Ivanti's Endpoint Manager Mobile (EPMM) and Microsoft's Windows systems have also been exploited. Additionally, a new Intel CPU flaw poses a significant risk by leaking sensitive data. Threat actors, including China-linked APTs, have been actively exploiting these vulnerabilities, emphasizing the urgent need for patching and enhanced security measures.

## Active Exploitation Details

- **CVE-2025-32756**: A zero-day remote code execution (RCE) vulnerability in Fortinet's FortiVoice systems has been actively exploited. Fortinet has released patches to mitigate this critical flaw.
- **SAP NetWeaver Zero-Day**: A second zero-day vulnerability in SAP NetWeaver servers has been exploited in recent attacks, with patches now available.
- **Ivanti EPMM Vulnerabilities**: Two vulnerabilities in Ivanti's Endpoint Manager Mobile software have been chained to achieve RCE in targeted attacks. Patches have been issued.
- **Windows Zero-Day**: Multiple zero-day vulnerabilities in Windows, including a browser-led RCE, have been addressed in Microsoft's May 2025 Patch Tuesday.
- **Intel CPU Flaw**: The "Branch Privilege Injection" flaw in Intel CPUs allows attackers to leak sensitive data from privileged memory, posing a significant threat to system security.

## Affected Systems and Products

- **Fortinet FortiVoice**: Enterprise phone systems affected by CVE-2025-32756.
- **SAP NetWeaver**: Servers targeted by zero-day vulnerabilities.
- **Ivanti EPMM**: Endpoint Manager Mobile software vulnerable to chained RCE attacks.
- **Microsoft Windows**: Multiple zero-day vulnerabilities affecting various Windows systems.
- **Intel CPUs**: All modern Intel processors vulnerable to the "Branch Privilege Injection" flaw.

## Attack Vectors and Techniques

- **Fortinet FortiVoice**: Exploitation of RCE vulnerability via network access to FortiVoice systems.
- **SAP NetWeaver**: Targeted attacks leveraging zero-day vulnerabilities to breach critical infrastructure.
- **Ivanti EPMM**: Chained vulnerabilities allowing remote code execution through crafted network requests.
- **Windows Systems**: Exploitation of zero-day vulnerabilities through browser-based attacks and other vectors.
- **Intel CPUs**: Exploitation of CPU flaw to leak data from privileged memory regions.

## Threat Actor Activities

s
- **China-Linked APTs**: Actively exploiting SAP NetWeaver vulnerabilities to target critical infrastructure worldwide.
- **Tidrone**: A Chinese actor targeting Taiwanese drone manufacturers and supply chains, focusing on military and satellite sectors.
- **Malicious PyPI Package**: Cybercriminals distributing a malicious package on PyPI, posing as a Solana tool to steal source code.

Security teams are advised to prioritize patching these vulnerabilities and monitor for any signs of exploitation within their networks. Enhanced security measures and threat intelligence should be employed to mitigate the risks posed by these critical vulnerabilities and active threat actors. 