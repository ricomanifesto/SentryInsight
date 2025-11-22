# Exploitation Report

Critical active exploitation activity is currently targeting Oracle Identity Manager systems through a remote code execution vulnerability, with CISA issuing urgent warnings to government agencies. Simultaneously, threat actors are conducting sophisticated espionage campaigns using novel malware and exploiting third-party application integrations to compromise enterprise environments. Notable activities include APT24's multi-year espionage operations using BadAudio malware, ShinyHunters group attacks on Salesforce customers through Gainsight applications, and maximum severity vulnerabilities in Grafana Enterprise that enable administrative privilege escalation.

## Active Exploitation Details

### Oracle Identity Manager RCE Vulnerability
- **Description**: Remote code execution flaw in Oracle Identity Manager that allows attackers to execute arbitrary code on vulnerable systems
- **Impact**: Attackers can gain complete system control, potentially compromising entire identity management infrastructures
- **Status**: Currently being exploited in active attacks; CISA has warned government agencies to apply patches immediately
- **CVE ID**: CVE-2025-61757

### Grafana Enterprise Administrative Spoofing
- **Description**: Maximum severity vulnerability in Grafana Enterprise's SCIM implementation that allows treating new users as administrators
- **Impact**: Attackers can achieve privilege escalation and perform user impersonation to gain administrative access
- **Status**: Patches available; organizations urged to update immediately
- **CVE ID**: CVE-2025-41115

## Affected Systems and Products

- **Oracle Identity Manager**: Systems running vulnerable versions are actively targeted by threat actors
- **Grafana Enterprise**: SCIM-enabled configurations vulnerable to administrative privilege escalation
- **Salesforce Environments**: Organizations using Gainsight-published applications face unauthorized data access risks
- **LINE Messaging App**: Asian users exposed to cyber espionage through leaky custom protocol implementations
- **Router Infrastructure**: Network devices compromised by PlushDaemon APT for software update hijacking

## Attack Vectors and Techniques

- **Third-Party Application Exploitation**: Threat actors leveraging OAuth integrations in applications like Gainsight to access Salesforce customer data
- **Software Update Hijacking**: PlushDaemon APT compromising routers to intercept and manipulate software updates
- **Browser Notification Abuse**: Matrix Push command and control tool exploiting browser notifications for phishing campaigns
- **Custom Protocol Exploitation**: LINE messaging app vulnerabilities enabling message replays and impersonation attacks
- **SCIM Protocol Manipulation**: Grafana vulnerability allowing new user registration with administrative privileges

## Threat Actor Activities

- **APT24**: Conducting three-year espionage campaign using BadAudio malware, targeting Taiwan and over 1,000 domains with sophisticated persistence mechanisms
- **ShinyHunters Group**: Executing repeat attacks against Salesforce customers through compromise of third-party Gainsight applications
- **PlushDaemon APT**: Chinese state-sponsored group primarily targeting domestic organizations through router compromise and software update manipulation
- **Scattered Spider**: British teenagers charged in connection with Transport for London breach causing millions in damage and customer data exposure
- **Internal Threats**: CrowdStrike identified insider sharing internal system screenshots with external hackers via Telegram channels