---
schema_version: 2
report_date: 2026-09-15
generated_at: 2026-09-15T12:05:47Z
digest_issue_url: https://ricomanifesto.github.io/SentryDigest/archive/2026-09-15/
---
# Exploitation Report

## Executive Summary

Critical exploitation activity continues to escalate across multiple vendor ecosystems, with threat actors rapidly weaponizing zero-day and recently disclosed vulnerabilities. Cisco's Secure Email Gateway is under active exploitation via a critical zero-day (CVE-2026-76461, CVSS 9.8) that enables unauthenticated remote command execution as root, while CISA has confirmed that the maximum-severity GitLab path traversal flaw (CVE-2026-85706, CVSS 10) is now being exploited in attacks. Chinese threat actors are conducting sophisticated campaigns: UTA0560 is chaining Chrome and Windows zero-days to deploy the GRIMWEDGE backdoor against NGOs, and Red Heron has compromised 13 organizations across six countries through rapid exploitation of a Gitea RCE. Russian state-sponsored group Sandworm continues to chain Cisco vulnerabilities to deploy the upgraded Cyclops Blink botnet, demonstrating persistent targeting of network infrastructure.

Mass exploitation campaigns are broadening beyond traditional vulnerability targeting. Attackers are conducting large-scale scanning of exposed Vite development servers to steal AWS and Azure cloud credentials, while a malicious Twitch browser extension with nearly 31,000 installs has been exfiltrating OAuth tokens to Russian-operated proxy servers. ClickFix social engineering attacks are being delivered through compromised legitimate accounts—including HBO Max's official Reddit account—to distribute information stealers across Windows and macOS. Meanwhile, a novel hardware-level attack dubbed DDRop breaks confidential computing protections on both Intel TDX and AMD SEV-SNP platforms, though it requires physical access.

Threat actor attribution and law enforcement actions are advancing in parallel. Five alleged leaders of the Black Axe cybercrime syndicate have been extradited to the United States to face wire fraud and money laundering charges, marking a significant disruption to a group responsible for global-scale financial fraud. An intrusion at Thailand's 3BB broadband provider revealed an attacker maintaining persistent root access via MeshCentral while targeting subscriber credentials. Japan's Digital Agency disclosed a VPN flaw exposing 246,000 government personnel records, and Revolut confirmed a breach after an attacker impersonated a government agency. These incidents underscore the convergence of vulnerability exploitation, social engineering, and supply chain compromise across the threat landscape.

## Active Exploitation Details

### Cisco Secure Email Gateway Zero-Day (CVE-2026-76461)
- **Description**: A critical zero-day vulnerability in AsyncOS Software for Cisco Secure Email Gateway caused by insufficient validation in email parsing logic, allowing unauthenticated remote attackers to execute arbitrary commands as root.
- **Impact**: Full system compromise with root privileges, enabling attackers to intercept, modify, or exfiltrate email traffic, pivot to internal networks, and establish persistent access.
- **Status**: Actively exploited in the wild; patches released by Cisco.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-76461
- **Reporting**: [Bleeping Computer — Cisco patches Secure Email Gateway zero-day exploited in attacks](https://www.bleepingcomputer.com/news/security/new-cisco-secure-email-zero-day-exploited-to-execute-commands-as-root/), [The Hacker News — Cisco Secure Email Gateway Flaw Exploited in the Wild, Enables Root Command Execution](https://thehackernews.com/2026/09/cisco-secure-email-gateway-flaw.html)

### GitLab Path Traversal (CVE-2026-85706)
- **Description**: A maximum-severity path traversal vulnerability affecting both GitLab Community Edition and Enterprise Edition, allowing unauthorized access to sensitive files and potential remote code execution.
- **Impact**: Complete compromise of GitLab instances, exposure of source code, credentials, and CI/CD pipelines, enabling supply chain attacks against downstream consumers.
- **Status**: Actively exploited in attacks; CISA has added to Known Exploited Vulnerabilities catalog; patches available.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-85706
- **Reporting**: [Dark Reading — Maximum Severity GitLab Flaw Puts Supply Chains at Risk](https://www.darkreading.com/cyberattacks-data-breaches/maximum-severity-gitlab-flaw-supply-chains-risk), [Bleeping Computer — CISA: Hackers now exploit max severity GitLab flaw in attacks](https://www.bleepingcomputer.com/news/security/cisa-hackers-now-exploit-max-severity-gitlab-flaw-in-attacks/)

### Gitea RCE Exploited by Red Heron
- **Description**: A recently disclosed remote code execution vulnerability in Gitea (self-hosted Git service) that Red Heron rapidly weaponized to compromise internet-facing instances across multiple countries.
- **Impact**: Full control of compromised Gitea instances, access to source code repositories, potential supply chain compromise, and lateral movement within victim networks.
- **Status**: Actively exploited in a multi-national campaign; Red Heron scanned 1,386 instances across seven countries and maintained a separate dataset of 477 Taiwan-based systems.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [The Hacker News — Red Heron Exploits Gitea RCE to Compromise 13 Organizations Across Six Countries](https://thehackernews.com/2026/09/red-heron-exploits-gitea-rce-to.html)

### Chrome-Windows Zero-Day Chain (GRIMWEDGE Campaign)
- **Description**: A spear-phishing campaign exploiting a chain of recently patched zero-day vulnerabilities in Google Chrome and Microsoft Windows to deliver the GRIMWEDGE JavaScript backdoor.
- **Impact**: Persistent backdoor access to targeted NGO systems, enabling espionage, data exfiltration, and potential lateral movement.
- **Status**: Actively exploited in targeted attacks against NGOs on September 1, 2026; patches available for the underlying vulnerabilities.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [The Hacker News — China-Linked Hackers Exploit Chrome-Windows Zero-Day Chain to Deploy GRIMWEDGE](https://thehackernews.com/2026/09/china-linked-hackers-exploit-chrome.html)

### Sandworm Cisco Vulnerability Chain (Cyclops Blink)
- **Description**: Russian threat group Sandworm is chaining multiple Cisco vulnerabilities to deploy an upgraded version of the Cyclops Blink botnet malware, previously disrupted by the FBI in 2022.
- **Impact**: Persistent botnet access on network devices, enabling DDoS, proxying, credential theft, and network reconnaissance.
- **Status**: Active exploitation and deployment; upgraded malware variant in circulation.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [Dark Reading — 'Sandworm' Chains Cisco Vulnerabilities to Deploy Cyclops Blink](https://www.darkreading.com/cyberattacks-data-breaches/sandworm-chains-cisco-vulnerabilities-cyclops-blink)

### LiteSpeed Enterprise Privilege Escalation
- **Description**: A critical vulnerability in LiteSpeed Web Server Enterprise that allows a low-privilege website user on a shared hosting server to gain root access, affecting all customers on the same machine.
- **Impact**: Complete server compromise, access to all hosted websites and data, ability to modify or exfiltrate other customers' content and server configuration.
- **Status**: Vulnerability disclosed with advisory from cPanel; exploitation potential high in shared hosting environments.
- **Severity**: critical
- **Exploitation Status**: potential
- **Action**: patch
- **Reporting**: [The Hacker News — LiteSpeed Enterprise Flaw Could Let One Hosting Account Gain Root Access on a Shared Server](https://thehackernews.com/2026/09/litespeed-enterprise-flaw-could-let-one.html)

### Exposed Vite Development Server Credential Theft
- **Description**: Mass-scanning campaign targeting internet-exposed Vite development servers to steal cloud credentials and configurations from AWS and Azure deployments.
- **Impact**: Cloud account compromise, access to infrastructure, data exfiltration, resource hijacking, and potential supply chain attacks through compromised build pipelines.
- **Status**: Active scanning and exploitation campaign ongoing.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [Bleeping Computer — Hackers target exposed Vite dev servers to steal AWS, Azure secrets](https://www.bleepingcomputer.com/news/security/hackers-target-exposed-vite-dev-servers-to-steal-aws-azure-secrets/)

### Malicious Twitch Browser Extension (JeetBot)
- **Description**: A cross-store browser extension ("Twitch Enhanced Viewer | JeetBot") with nearly 31,000 installs that exfiltrates users' Twitch OAuth session tokens to proxy servers operated by a Russian commercial bot service.
- **Impact**: Account takeover, unauthorized access to Twitch accounts, potential credential reuse across platforms, and privacy violation for affected users.
- **Status**: Actively distributing through official Chrome and Firefox stores; tokens actively being exfiltrated.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [Bleeping Computer — Twitch extension with 30K installs exposes users’ OAuth tokens](https://www.bleepingcomputer.com/news/security/twitch-extension-with-30k-installs-exposes-users-oauth-tokens/), [The Hacker News — Malicious Twitch Browser Extension Leaks OAuth Tokens From Nearly 31,000 Users](https://thehackernews.com/2026/09/malicious-twitch-browser-extension.html)

### ClickFix Attacks via Compromised Reddit Account
- **Description**: Attackers hijacked HBO Max's official Reddit account to push malicious ads that launch ClickFix attacks, tricking users into executing commands that install information-stealing malware on Windows and macOS.
- **Impact**: Malware installation, credential theft, financial fraud, and potential corporate network compromise through compromised personal devices.
- **Status**: Active campaign leveraging compromised high-profile social media account.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [Bleeping Computer — Hackers hijack HBO Max Reddit account to push malware in ClickFix ads](https://www.bleepingcomputer.com/news/security/hackers-hijack-hbo-max-reddit-account-to-push-malware-in-clickfix-ads/)

### 3BB MeshCentral Backdoor Intrusion
- **Description**: An attacker maintained persistent remote control inside 3BB's (Thailand's largest broadband provider) network using MeshCentral, a legitimate remote management tool, while targeting subscriber credentials.
- **Impact**: Unauthorized access to internal systems, potential subscriber data theft, persistent foothold in critical telecommunications infrastructure.
- **Status**: Active intrusion discovered via attacker's exposed server containing tools and target lists.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: investigate
- **Reporting**: [The Hacker News — 3BB Attacker Used MeshCentral Backdoor for Root Access, Targeted Subscriber Credentials](https://thehackernews.com/2026/09/3bb-attacker-used-meshcentral-backdoor.html)

### DDRop Hardware Attack on Confidential Computing
- **Description**: A novel hardware attack that breaks memory protection in Intel TDX and AMD SEV-SNP confidential computing by silently dropping writes to server memory, causing the processor to read stale encrypted data.
- **Impact**: Bypass of confidential computing guarantees, potential data integrity attacks, and undermining of hardware-based isolation for sensitive workloads.
- **Status**: Research disclosure; requires physical access and software control of the target server.
- **Severity**: high
- **Exploitation Status**: potential
- **Action**: monitor
- **Reporting**: [The Hacker News — New DDRop Attack Breaks Intel TDX and AMD SEV-SNP Confidential Computing](https://thehackernews.com/2026/09/new-ddrop-attack-breaks-intel-tdx-and.html)

### Telegram Desktop HTML Export XSS
- **Description**: A flaw in Telegram Desktop allowing hidden JavaScript in bot messages to execute when users open exported HTML chat files in a browser, enabling exfiltration of all messages in the export.
- **Impact**: Message history theft, potential credential exposure from chat logs, and privacy violation for users who export and view chats in browsers.
- **Status**: Vulnerability disclosed by ExPatch researchers; exploitation requires user interaction (opening exported file).
- **Severity**: medium
- **Exploitation Status**: potential
- **Action**: mitigate
- **Reporting**: [The Hacker News — Telegram Desktop Flaw Lets Hidden JavaScript Exfiltrate Messages From HTML Exports](https://thehackernews.com/2026/09/telegram-desktop-flaw-lets-hidden.html)

### Japan Digital Agency VPN Data Breach
- **Description**: A VPN vulnerability in Japan's Digital Agency infrastructure exposed approximately 246,000 records containing personal information of government employees.
- **Impact**: Large-scale exposure of sensitive government personnel data, potential identity theft, and national security implications.
- **Status**: Breach discovered and disclosed; vulnerability details not fully specified.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: investigate
- **Reporting**: [Bleeping Computer — Japan's Digital Agency says VPN flaw exposed 246,000 personnel records](https://www.bleepingcomputer.com/news/security/japans-digital-agency-says-vpn-flaw-exposed-246-000-personnel-records/)

### Revolut Impersonation Breach
- **Description**: Fintech company Revolut disclosed a data breach after an attacker impersonating a government agency successfully social-engineered access to customer data.
- **Impact**: Exposure of financial information and passport data for an undisclosed number of customers.
- **Status**: Breach confirmed and disclosed; attack vector was social engineering rather than technical vulnerability.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: investigate
- **Reporting**: [Bleeping Computer — Revolut discloses data breach exposing financial info, passports](https://www.bleepingcomputer.com/news/security/revolut-discloses-data-breach-exposing-financial-info-passports/)

### Passkey Phishing Targeting Microsoft Cloud
- **Description**: Two campaigns abusing third-party email infrastructure to send financial fraud scams and using passkey-themed social engineering to breach Microsoft cloud environments.
- **Impact**: Cloud account compromise, data exfiltration, business email compromise, and financial fraud; one campaign sent over 1 million scam emails between August 3-5, 2026.
- **Status**: Active campaigns disclosed by Microsoft.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: investigate
- **Reporting**: [The Hacker News — Attackers Use Passkey Phishing to Hijack Microsoft Cloud Accounts and Exfiltrate Data](https://thehackernews.com/2026/09/attackers-use-passkey-phishing-to.html)

## Affected Systems and Products

- **Cisco Secure Email Gateway (AsyncOS)**: All versions vulnerable to CVE-2026-76461 until patched; network email security appliances and virtual deployments
- **GitLab Community Edition and Enterprise Edition**: All versions prior to patched releases vulnerable to CVE-2026-85706; self-hosted and cloud-managed instances
- **Gitea**: Internet-facing instances vulnerable to RCE; versions prior to security patch across Linux, Windows, macOS, and container deployments
- **Google Chrome and Microsoft Windows**: Versions prior to September 2026 security updates vulnerable to zero-day chain exploited by UTA0560; Windows 10/11, Chrome on all platforms
- **Cisco Network Devices**: Multiple device families vulnerable to chained exploits used by Sandworm for Cyclops Blink deployment; routers, switches, firewalls
- **LiteSpeed Web Server Enterprise**: Shared hosting deployments on cPanel servers; all Enterprise versions prior to patch
- **Vite Development Servers**: Internet-exposed development servers with default configurations; Node.js/Vite projects on AWS, Azure, GCP, and on-premises
- **Twitch Enhanced Viewer | JeetBot Extension**: Chrome Web Store and Firefox Add-ons installations; browser extensions on Windows, macOS, Linux
- **MeshCentral**: Legitimate remote management tool abused for persistent access; 3BB broadband provider infrastructure and potentially other deployments
- **Intel TDX and AMD SEV-SNP Platforms**: Confidential computing implementations on server-grade processors; cloud and on-premises confidential VM deployments
- **Telegram Desktop**: Windows, macOS, Linux desktop clients; HTML export functionality
- **VPN Infrastructure (Japan Digital Agency)**: Government VPN solution; specific vendor not disclosed
- **Microsoft Cloud / Entra ID**: Targeted via passkey phishing and financial fraud campaigns; enterprise and consumer tenants

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Active use of unpatched vulnerabilities (Cisco CVE-2026-76461, Chrome/Windows chain) before or immediately after disclosure
- **Vulnerability Chaining**: Combining multiple vulnerabilities (Chrome + Windows for GRIMWEDGE; multiple Cisco flaws for Cyclops Blink) to achieve higher impact
- **Mass Scanning and Opportunistic Exploitation**: Automated scanning for exposed Vite dev servers, Gitea instances (1,386 scanned by Red Heron), and vulnerable GitLab deployments
- **Supply Chain Compromise**: Targeting GitLab and Gitea as source code management platforms to inject malicious code or steal intellectual property
- **Social Engineering and Phishing**: Spear-phishing with zero-day chains (UTA0560), passkey-themed lures (Microsoft Cloud campaigns), CEO impersonation (1M+ fraud emails)
- **Malicious Browser Extensions**: Distribution through official stores (Chrome Web Store, Firefox Add-ons) to steal OAuth tokens at scale (31K+ Twitch users)
- **Compromised Legitimate Accounts**: Hijacking high-profile social media accounts (HBO Max Reddit) to deliver malvertising and ClickFix attacks
- **Living-off-the-Land / Legitimate Tool Abuse**: Using MeshCentral (legitimate RMM) for persistent C2; leveraging third-party email infrastructure for phishing scale
- **ClickFix / Social Engineering Execution**: Tricking users into copying and executing malicious commands via fake verification prompts
- **Hardware-Level Attack (DDRop)**: Physical memory manipulation to break confidential computing guarantees; requires brief physical access and software control
- **Client-Side XSS via Export Functionality**: Hidden JavaScript in Telegram messages executing only when exported HTML is opened in browser
- **Impersonation and Pretexting**: Attacker posing as government agency to social-engineer Revolut employee into data disclosure
- **Botnet Deployment and Upgrades**: Sandworm deploying upgraded Cyclops Blink on network devices for persistent infrastructure control

## Threat Actor Activities

- **UTA0560 (China-linked)**: Conducted spear-phishing campaign on September 1, 2026 targeting multiple NGOs using Chrome-Windows zero-day chain to deploy GRIMWEDGE JavaScript backdoor; attributed by Volexity
- **Red Heron (Suspected Chinese)**: Rapid exploitation of Gitea RCE across 13 organizations in six countries; scanned 1,386 instances in seven countries with focused dataset on 477 Taiwan-based systems; attributed by Acronis TRU
- **Sandworm (Russian GRU/APT28)**: Chaining Cisco vulnerabilities to deploy upgraded Cyclops Blink botnet; persistent targeting of network infrastructure; previously disrupted by FBI in 2022
- **Black Axe Cybercrime Syndicate**: Global-scale cyber-enabled financial fraud; five alleged leaders extradited to US facing wire fraud and money laundering charges
- **JeetBot/HISHIMIRO Operators (Russian-linked)**: Distributing malicious Twitch browser extension through official stores; exfiltrating OAuth tokens to Russian commercial bot service proxy servers; ~31K victims
- **ClickFix Operators**: Hijacking legitimate brand accounts (HBO Max Reddit) for malvertising delivery; cross-platform info-stealer deployment on Windows and macOS
- **3BB Intrusion Actor**: Unknown threat actor maintaining persistent access in Thailand's largest broadband provider via MeshCentral; targeting subscriber credentials; discovered by Hunt.io
- **Passkey Phishing Actors**: Two distinct campaigns using third-party email infrastructure; one sent 1M+ CEO impersonation emails Aug 3-5, 2026; targeting Microsoft Cloud accounts via passkey social engineering
- **Revolut Impersonator**: Unknown actor successfully impersonated government agency to social-engineer access to customer financial and passport data
- **DDRop Researchers/Attackers**: Academic researchers disclosing hardware attack; potential for advanced persistent threats with physical access capabilities