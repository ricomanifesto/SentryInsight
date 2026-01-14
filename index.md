# Exploitation Report

Microsoft begins 2026 with significant security challenges, addressing 114 vulnerabilities in its January Patch Tuesday update, including one actively exploited zero-day vulnerability and two additional publicly disclosed zero-days. Critical vulnerabilities have also emerged in FortiSIEM allowing unauthenticated remote code execution, Node.js affecting virtually all production applications through stack overflow denial-of-service attacks, and ServiceNow's AI systems exposing customer data. Meanwhile, sophisticated malware campaigns continue to evolve with new threats like VoidLink targeting Linux cloud environments, PLUGGYAPE malware infiltrating Ukrainian defense forces, and web skimming operations that have been active since 2022 targeting major payment networks.

## Active Exploitation Details

### Windows Zero-Day Vulnerability
- **Description**: One of three zero-day vulnerabilities patched in Microsoft's January 2026 update that has been actively exploited in the wild
- **Impact**: Allows attackers to compromise Windows systems through unknown attack vectors
- **Status**: Actively exploited in the wild, patch available through January 2026 Patch Tuesday

### FortiSIEM Critical Remote Code Execution Vulnerability
- **Description**: Critical security flaw in Fortinet's FortiSIEM allowing unauthenticated remote code execution
- **Impact**: Attackers can achieve complete system compromise without authentication on susceptible FortiSIEM instances
- **Status**: Patch available from Fortinet

### Node.js async_hooks Stack Overflow Vulnerability
- **Description**: Critical vulnerability affecting virtually every production Node.js application through async_hooks stack overflow
- **Impact**: Can cause server crashes and denial-of-service conditions
- **Status**: Updates released by Node.js to address the issue

### ServiceNow AI System Vulnerability
- **Description**: Severe AI vulnerability where ServiceNow implemented agentic AI on an unguarded legacy chatbot system
- **Impact**: Exposes customers' data and connected systems through AI system compromise
- **Status**: Described as the "most severe AI vulnerability to date"

## Affected Systems and Products

- **Microsoft Windows**: All supported Windows operating systems affected by 114 vulnerabilities including 3 zero-days
- **Fortinet FortiSIEM**: Critical remote code execution vulnerability in security information and event management platform
- **Node.js Applications**: Virtually all production Node.js applications vulnerable to stack overflow denial-of-service
- **ServiceNow Platform**: AI-enabled systems exposing customer data and connected infrastructure
- **Android Devices**: Volume button functionality issues affecting devices with accessibility features enabled
- **Linux Cloud Servers**: Targeted by VoidLink malware framework designed for cloud and container environments

## Attack Vectors and Techniques

- **VoidLink Malware Framework**: Advanced cloud-native Linux malware providing custom loaders, implants, rootkits, and plugins for long-term stealthy access
- **PLUGGYAPE Malware**: Uses Signal and WhatsApp messaging platforms to target Ukrainian Defense Forces through charity-themed campaigns
- **Web Skimming Campaign**: Long-running operation since January 2022 targeting major payment networks including American Express, Diners Club, and Discover
- **Shadow#Reactor**: Sophisticated delivery mechanism using text-only files to deploy Remcos RAT and bypass defensive tools
- **AsyncRAT Distribution**: Attackers abusing Python and Cloudflare services to deliver AsyncRAT through phishing campaigns
- **Chrome Extension Malware**: Malicious extensions masquerading as trading tools to steal MEXC cryptocurrency exchange API keys

## Threat Actor Activities

- **Ukrainian Defense Force Targeting**: Coordinated campaign between October and December 2025 using charity-themed malware to infiltrate military communications
- **Chinese Cyber Operations**: Increased cyberattacks on Taiwan's critical infrastructure including energy utilities and hospitals, averaging 2.63 million attacks daily with a 6% increase in 2025
- **Web Skimming Operations**: Persistent threat actors running major payment card theft operations targeting online checkout pages across multiple payment networks
- **Cryptocurrency Threat Actors**: Targeted attacks against cryptocurrency traders and exchanges through malicious browser extensions and phishing campaigns