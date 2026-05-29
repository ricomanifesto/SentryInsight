# Exploitation Report

Recent security reports reveal a concerning landscape of active exploitation targeting multiple platforms and technologies. Critical vulnerabilities are being exploited in FortiClient EMS systems through CVE-2026-35616, allowing threat actors to deploy credential-stealing malware. A zero-day vulnerability in the Gogs Git service is actively being exploited to achieve remote code execution, while attackers are leveraging CVE-2026-39987 in Marimo systems for post-exploitation activities using AI-powered tools. Nation-state actors, particularly the Russian-linked GREYVIBE group, are conducting persistent attacks against Ukrainian entities using AI-enhanced techniques. Additionally, massive botnets comprising 17 million infected devices have been disrupted, and various threat actors are exploiting cloud misconfigurations and supply chain vulnerabilities through malicious packages.

## Active Exploitation Details

### FortiClient EMS Authentication Bypass
- **Description**: Critical authentication bypass vulnerability in FortiClient Enterprise Management Server
- **Impact**: Allows threat actors to deploy credential-stealing malware, specifically an undocumented stealer called EKZ
- **Status**: Currently being exploited in active campaigns, patch available
- **CVE ID**: CVE-2026-35616

### Gogs Remote Code Execution Zero-Day
- **Description**: Unpatched zero-day vulnerability in the Gogs self-hosted Git service
- **Impact**: Enables attackers to execute arbitrary code remotely on Internet-facing instances
- **Status**: Actively exploited zero-day, no patch currently available

### Marimo Post-Exploitation Framework
- **Description**: Vulnerability in Marimo allowing post-compromise exploitation
- **Impact**: Threat actors use large language model agents for automated post-exploitation activities
- **Status**: Active exploitation observed with AI-enhanced techniques
- **CVE ID**: CVE-2026-39987

## Affected Systems and Products

- **FortiClient Enterprise Management Server**: Authentication bypass vulnerability affecting credential management
- **Gogs Git Service**: Self-hosted Git service instances exposed to the internet
- **Marimo Framework**: Python-based data science platform vulnerable to post-exploitation
- **Android Devices**: Targeted by BTMOB remote access trojan with custom payload generation
- **Cloud Applications**: Over 2,000 AI-coded applications exposed with security vulnerabilities
- **Charter Communications**: 4.9 million customer accounts compromised by ShinyHunters group
- **Ukrainian Government and Corporate Systems**: Targeted by Russian state-sponsored actors

## Attack Vectors and Techniques

- **AI-Enhanced Social Engineering**: GREYVIBE using ChatGPT and Gemini to generate convincing lure content
- **Supply Chain Attacks**: Malicious NuGet and npm packages targeting banking credentials and cloud secrets
- **Zero-Day Exploitation**: Immediate weaponization of unpatched vulnerabilities in popular services
- **LLM Agent Automation**: Post-exploitation activities automated using large language model agents
- **Botnet Infrastructure**: Massive networks of 17 million compromised devices for distributed attacks
- **Cloud Misconfiguration Exploitation**: Targeting over-permissioned roles and exposed secrets in cloud environments

## Threat Actor Activities

- **GREYVIBE (Russian-linked)**: Persistent attacks against Ukrainian entities since August 2025 using AI-powered techniques and custom malware including HTTPSpy and HelloDoor
- **Kimsuky (North Korean)**: Targeting South Korean military and corporate entities with expanded arsenal including HTTPSpy, HelloDoor, and VS Code tunnels
- **ShinyHunters**: Extortion gang responsible for Charter Communications breach affecting 4.9 million accounts
- **"The Com" Criminal Gang**: Neo-Nazi-affiliated cybercriminal group using proceeds to support violence and exploitation activities
- **Unknown LLM-Powered Actors**: Leveraging AI agents for automated post-exploitation following CVE-2026-39987 compromise
- **BTMOB Operators**: Offering Android malware-as-a-service with custom payload generation capabilities