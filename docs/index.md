# Exploitation Report

Several critical zero-day vulnerabilities and active exploitation campaigns have been identified across multiple platforms and systems. The most significant activity involves a Chinese state-backed threat actor exploiting a maximum severity Dell RecoverPoint vulnerability (CVE-2026-22769) since mid-2024, alongside sophisticated supply chain attacks targeting Android devices through firmware backdoors and compromised software update mechanisms. CISA has flagged four additional security flaws under active exploitation, while advanced threat actors continue leveraging zero-day attacks against telecommunications infrastructure and popular development tools.

## Active Exploitation Details

### Dell RecoverPoint for VMs Zero-Day Vulnerability
- **Description**: A maximum severity security vulnerability in Dell RecoverPoint for Virtual Machines that has been exploited as a zero-day attack
- **Impact**: Allows attackers to gain unauthorized access to virtualized environments and potentially compromise entire VM infrastructures
- **Status**: Actively exploited since mid-2024 by suspected Chinese threat actors
- **CVE ID**: CVE-2026-22769

### Notepad++ Update Mechanism Vulnerability
- **Description**: Security gaps in Notepad++ update mechanism that were exploited by advanced threat actors to hijack the software update process
- **Impact**: Enables selective malware delivery to specific targets through compromised software updates
- **Status**: Patched with new "double-lock" security mechanism implementation

### Singapore Telecommunications Zero-Day Attack
- **Description**: Zero-day vulnerability targeting Singapore's major telecommunications infrastructure
- **Impact**: Potential compromise of critical telecommunications systems and infrastructure
- **Status**: Attack detected and defended against through coordinated government-private sector response

### Keenadu Android Firmware Backdoor
- **Description**: Sophisticated Android malware embedded deep into device firmware through supply chain compromise
- **Impact**: Silent data harvesting, remote device control, and compromise of all installed applications with unrestricted access
- **Status**: Actively deployed through signed OTA updates and found in Google Play Store applications

## Affected Systems and Products

- **Dell RecoverPoint for Virtual Machines**: Critical virtualization infrastructure vulnerability affecting VM environments
- **Notepad++**: Popular text editor with compromised update mechanism used for targeted malware delivery
- **Singapore Telecommunications Infrastructure**: Four major telecom providers targeted in coordinated zero-day attack
- **Android Devices**: Multiple device brands affected by firmware-level Keenadu backdoor through supply chain compromise
- **Microsoft 365 Copilot**: AI assistant affected by bug causing unauthorized access to confidential emails, bypassing DLP policies
- **Visual Studio Code Extensions**: Popular VSCode extensions with high to critical severity vulnerabilities affecting 128+ million downloads
- **Polish Energy Infrastructure**: Wind, solar, and heating infrastructure targeted by wiper attacks

## Attack Vectors and Techniques

- **Supply Chain Compromise**: Firmware-level backdoor installation through legitimate OTA update mechanisms and signed applications
- **Software Update Hijacking**: Exploitation of software update mechanisms to deliver targeted malware selectively
- **Zero-Day Exploitation**: Direct exploitation of unknown vulnerabilities in critical infrastructure and enterprise systems
- **AI Assistant Abuse**: Manipulation of AI chatbots and assistants for command-and-control proxy operations
- **DNS Lookup Command Abuse**: ClickFix campaigns using DNS lookup commands to deliver ModeloRAT malware
- **RMM Software Abuse**: Remote monitoring and management tools leveraged for stealth, persistence, and operational efficiency
- **Trojanized MCP Servers**: SmartLoader campaigns distributing trojanized Model Context Protocol servers to deploy StealC infostealer

## Threat Actor Activities

- **UNC6201 (Chinese State-Backed)**: Actively exploiting Dell RecoverPoint zero-day vulnerability since mid-2024, demonstrating advanced persistent threat capabilities
- **Chinese Advanced Threat Actor**: Hijacked Notepad++ update mechanism for selective malware delivery, showing sophisticated supply chain attack capabilities
- **Russia-Aligned Groups**: Conducting wiper attacks against Poland's renewable energy infrastructure, targeting wind farms, solar installations, and power plants
- **Phobos Ransomware Operation**: Continued ransomware activities with recent arrest of 47-year-old suspect in Poland linked to the operation
- **Unknown Threat Actors**: Conducting ClickFix campaigns with evolved techniques using DNS lookup commands for payload delivery