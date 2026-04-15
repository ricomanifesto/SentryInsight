# Exploitation Report

Microsoft's April 2026 Patch Tuesday addressed a record-breaking 167 security vulnerabilities, including two actively exploited zero-day vulnerabilities that pose immediate threats to organizations. Among the most critical findings is active exploitation of CVE-2025-0520, a remote code execution vulnerability in ShowDoc servers that is being targeted by threat actors in the wild. Additionally, prompt injection vulnerabilities in AI systems from Microsoft Copilot and Salesforce Agentforce have been patched after enabling external attackers to leak sensitive data. The threat landscape is further complicated by widespread malicious activities including over 100 malicious Chrome extensions stealing user data, a fake Ledger Live app that drained $9.5 million in cryptocurrency, and sophisticated Android malware campaigns reaching hundreds of thousands of victims.

## Active Exploitation Details

### SharePoint Server Zero-Day Vulnerability
- **Description**: A critical zero-day vulnerability in Microsoft SharePoint Server that has been actively exploited in the wild
- **Impact**: Attackers can potentially gain unauthorized access to SharePoint systems and sensitive corporate data
- **Status**: Patched in Microsoft's April 2026 Patch Tuesday update

### Secondary Zero-Day Vulnerability
- **Description**: A publicly disclosed zero-day vulnerability affecting Microsoft products that was being actively exploited
- **Impact**: Privilege elevation and potential system compromise
- **Status**: Addressed in the April 2026 security updates

### ShowDoc Remote Code Execution Flaw
- **Description**: A critical remote code execution vulnerability in ShowDoc, a popular document management and collaboration service in China
- **Impact**: Complete system compromise through arbitrary code execution on vulnerable servers
- **Status**: Active exploitation confirmed on unpatched servers
- **CVE ID**: CVE-2025-0520

### AI Agent Prompt Injection Vulnerabilities
- **Description**: Prompt injection flaws in Microsoft Copilot and Salesforce Agentforce that allow external attackers to manipulate AI responses
- **Impact**: Sensitive data leakage through compromised AI agent interactions
- **Status**: Recently patched by both Microsoft and Salesforce

## Affected Systems and Products

- **Microsoft SharePoint Server**: Zero-day vulnerability affecting server installations
- **Microsoft Windows Operating Systems**: 167 vulnerabilities patched across Windows versions including Server 2019, 2022, and 2025
- **ShowDoc Servers**: Critical RCE vulnerability actively exploited on unpatched installations
- **Microsoft Copilot**: Prompt injection vulnerability enabling data exfiltration
- **Salesforce Agentforce**: AI agent platform affected by prompt injection flaws
- **Google Chrome Browser**: Over 100 malicious extensions targeting user accounts and OAuth2 tokens
- **Android Devices**: Mirax RAT affecting Spanish-speaking users through Meta advertising platforms
- **PHP Composer**: Package manager vulnerabilities enabling arbitrary command execution
- **Fortinet Products**: Multiple vulnerabilities added to CISA's Known Exploited Vulnerabilities catalog
- **Adobe Software**: Security flaws confirmed as actively exploited and added to KEV catalog

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Active targeting of unpatched SharePoint servers and other Microsoft products
- **Prompt Injection**: Manipulation of AI systems to extract sensitive information from corporate environments
- **Supply Chain Attacks**: Malicious Chrome extensions distributed through official Web Store targeting OAuth2 tokens
- **Social Engineering**: Fake mobile applications impersonating legitimate cryptocurrency wallets
- **Malvertising**: Android malware distribution through Facebook, Instagram, and Messenger advertisements
- **Configuration Exploitation**: Salesforce misconfigurations leading to unauthorized data access
- **EDR Evasion**: Bring-Your-Own-Vulnerable-Driver (BYOVD) techniques to bypass endpoint detection systems
- **SEO Poisoning**: AI-generated content manipulation for search engine optimization and ad fraud
- **Remote Desktop File Abuse**: Malicious RDP files used in phishing campaigns

## Threat Actor Activities

- **ShowDoc Exploiters**: Actively targeting CVE-2025-0520 to compromise unpatched document management servers
- **Chrome Extension Operators**: Coordinated campaign deploying 108 malicious extensions affecting over 20,000 users
- **Cryptocurrency Thieves**: Sophisticated operation using fake Ledger Live app to steal $9.5 million from 50 victims
- **Mirax RAT Distributors**: Large-scale Android malware campaign reaching 220,000 accounts via Meta advertising platforms
- **Corporate Data Extortionists**: Groups targeting companies like Kraken cryptocurrency exchange and McGraw-Hill through insider threats and configuration exploits
- **AI System Attackers**: Threat actors exploiting prompt injection vulnerabilities in enterprise AI deployments
- **Pushpaganda Operators**: AI-driven scareware distribution through Google Discover platform manipulation