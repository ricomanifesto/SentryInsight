# Exploitation Report

## Executive Summary

Microsoft has patched a critical Windows Defender zero-day vulnerability tracked as CVE-2026-50656, known as "RoguePlanet," which allows attackers to gain SYSTEM privileges. The flaw was publicly disclosed with a proof-of-concept exploit by researcher "Nightmare-Eclipse" in early June, nearly a month before Microsoft released the fix. This vulnerability represents a significant privilege escalation risk for Windows systems and was actively exploitable before patching.

Supply chain attacks continue to escalate across multiple vectors. The Injective Labs SDK on npm was compromised to distribute a cryptocurrency wallet stealer, while a new threat actor dubbed "Lurking Lizard" distributes fake 7-Zip installers that convert victim devices into residential proxy nodes. Additionally, researchers uncovered "GhostApproval" symlink flaws affecting six popular AI coding assistants that allow malicious repositories to execute arbitrary code on developers' machines, and demonstrated that AI coding agents designed to detect vulnerabilities can be tricked into executing malicious code instead.

Iranian threat actors are expanding targeting beyond critical infrastructure to any organization with internet-facing vulnerabilities. Meanwhile, a new data extortion group called "Helix" employs sophisticated identity-focused tactics including voice phishing (vishing), device code phishing, and MFA abuse to steal data from SharePoint environments. The GodDamn ransomware family leverages a Microsoft-signed malicious kernel driver (PoisonX) in a BYOVD attack to disable endpoint defenses before encrypting systems, primarily targeting US companies. Datadog Security Labs has also identified overlapping campaigns systematically enumerating corporate GitHub organizations, repositories, and user accounts through the GitHub API using dormant accounts to blend in.

## Active Exploitation Details

### RoguePlanet Windows Defender Zero-Day (CVE-2026-50656)
- **Description**: A zero-day vulnerability in Windows Defender that allows local privilege escalation to SYSTEM privileges. The flaw was discovered and publicly disclosed with a proof-of-concept exploit by researcher "Nightmare-Eclipse" in early June 2026, before Microsoft released a patch.
- **Impact**: Attackers can exploit this vulnerability to gain SYSTEM-level privileges on affected Windows systems, effectively achieving full control over the compromised host.
- **Status**: Microsoft released a security patch in July 2026, nearly a month after public disclosure. The vulnerability was actively exploitable during the disclosure-to-patch window.
- **CVE ID**: CVE-2026-50656

### GodDamn Ransomware BYOVD Attack
- **Description**: The GodDamn ransomware family employs a Bring Your Own Vulnerable Driver (BYOVD) technique using a malicious kernel driver called PoisonX to disable endpoint security solutions. Notably, Microsoft had signed this malicious driver, allowing it to load on Windows systems.
- **Impact**: Attackers can neutralize security software including EDR and antivirus solutions before deploying ransomware payloads, significantly increasing the success rate of encryption and data theft operations.
- **Status**: Actively used in attacks targeting US companies. Microsoft's signing of the malicious driver represents a significant supply chain trust failure.

### Injective SDK npm Supply Chain Attack
- **Description**: Attackers compromised the Injective Labs SDK project's GitHub repository and published a malicious package on npm containing a cryptocurrency wallet stealer designed to extract private keys and mnemonics.
- **Impact**: Developers and projects incorporating the compromised SDK package had their cryptocurrency wallet credentials stolen, leading to potential financial loss and further compromise of blockchain assets.
- **Status**: Malicious package was published to npm and available for download before detection and removal.

### GigaWiper Windows Backdoor
- **Description**: A destructive Windows backdoor that combines three older destructive programs into a single toolkit offering disk wiping, fake ransomware, and spyware capabilities as modular commands.
- **Impact**: Provides attackers with a versatile destructive toolkit capable of data exfiltration, system destruction via disk wiping, and deception through fake ransomware operations.
- **Status**: Analyzed by Microsoft; active deployment status not explicitly confirmed but tooling exists and is operational.

### Helix Vishing and SharePoint Data Theft
- **Description**: A new data extortion group (Helix) uses identity-focused attack chains combining voice phishing (vishing), device code phishing, and multi-factor authentication (MFA) abuse to gain access to SharePoint environments for data theft.
- **Impact**: Successful attacks result in unauthorized access to SharePoint data repositories, enabling data exfiltration and extortion without deploying traditional malware.
- **Status**: Actively operating as a phishing-as-a-service (PhaaS) or data extortion group targeting organizations using Microsoft 365/SharePoint.

### Forg365 Phishing-as-a-Service Platform
- **Description**: A new PhaaS operation called Forg365 that combines adversary-in-the-middle (AiTM) techniques with device code phishing and AI-assisted lure generation to steal Microsoft 365 credentials.
- **Impact**: Lowers the barrier for credential theft against Microsoft 365 accounts by providing a managed service with AI-enhanced social engineering lures.
- **Status**: Actively operating as a commercial phishing service targeting Microsoft 365 users.

### GhostApproval Symlink Flaws in AI Coding Assistants
- **Description**: Researchers at Wiz discovered a flaw in six popular AI coding assistants where a booby-trapped code project can exploit symlink handling to execute arbitrary code on a developer's machine when the assistant requests permission to edit a harmless-appearing file.
- **Impact**: Developers using affected AI coding assistants can have their systems compromised simply by opening a malicious repository, bypassing typical code review safeguards.
- **Status**: Proof-of-concept demonstrated; affects six major AI coding assistant platforms.

### AI Coding Agents Tricked into Executing Malicious Code
- **Description**: A proof-of-concept demonstrating that AI coding agents designed to scan code for security vulnerabilities can be manipulated into executing attacker-controlled code on the host machine during analysis.
- **Impact**: Security tools themselves become attack vectors, turning defensive automation into offensive capability for adversaries.
- **Status**: Proof-of-concept published; represents emerging risk class as AI agents gain more autonomous execution capabilities.

### Lurking Lizard Fake 7-Zip Installer Campaign
- **Description**: Threat actor "Lurking Lizard" operates an end-to-end malicious residential proxy business using fake 7-Zip installers that convert victim devices into proxy nodes within a larger infrastructure.
- **Impact**: Victims unknowingly participate in proxy networks used for credential stuffing, web scraping, and other abusive traffic, while attackers monetize the residential IP reputation.
- **Status**: Active campaign with established infrastructure for distribution and proxy management.

### Dormant GitHub Account Enumeration Campaigns
- **Description**: Multiple overlapping campaigns systematically enumerate corporate GitHub organizations, repositories, and user accounts through the GitHub API, leveraging dormant or compromised accounts to blend in with legitimate traffic.
- **Impact**: Attackers gain comprehensive intelligence on corporate codebases, team structures, and potential attack surfaces for subsequent supply chain or targeted attacks.
- **Status**: Ongoing campaigns identified by Datadog Security Labs; active enumeration operations.

### AI Gateway Cryptomining Incident
- **Description**: Attackers exploited an AI gateway to gain access to AI models, cloud infrastructure, and identity and access management (IAM) data, subsequently deploying cryptomining operations.
- **Impact**: Compromise of AI infrastructure abuse of AI infrastructure for resource theft, potential lateral movement to cloud environments, and exposure of sensitive IAM configurations.
- **Status**: Documented incident demonstrating AI gateways as high-value targets for initial access and privilege escalation.

### OpenMandriva Internal Sabotage Attempt
- **Description**: A contributor to the OpenMandriva Linux project attempted to sabotage the distribution following a dispute among contributors, representing an insider threat to software supply chain integrity.
- **Impact**: Potential introduction of malicious code or build process manipulation affecting downstream users of the Linux distribution.
- **Status**: Detected and disclosed by the OpenMandriva project; specific technical details of the sabotage attempt not fully public.

### AssuranceAmerica Data Breach
- **Description**: Attackers gained unauthorized access to systems at American insurance company AssuranceAmerica, exposing records of approximately 6.9 million drivers.
- **Impact**: Large-scale personal data exposure including driver information, enabling identity theft, fraud, and targeted phishing.
- **Status**: Breach disclosed; initial access occurred earlier in 2026, with notification and investigation ongoing.

## Affected Systems and Products

- **Windows Defender / Microsoft Defender**: Affected by CVE-2026-50656 (RoguePlanet) privilege escalation vulnerability; all supported Windows versions with Defender enabled prior to July 2026 patch
- **Windows Kernel Driver Signing**: Compromised trust chain allowing Microsoft-signed malicious driver (PoisonX) to load on Windows systems for BYOVD attacks
- **Injective Labs SDK (npm package)**: Compromised GitHub repository leading to malicious npm publishes affecting all downstream consumers of the SDK
- **AI Coding Assistants (6 platforms)**: Vulnerable to GhostApproval symlink flaws allowing arbitrary code execution via malicious repositories; specific platforms not named in source
- **GitHub Enterprise / GitHub.com Organizations**: Targeted by systematic enumeration campaigns via GitHub API using dormant accounts
- **Microsoft 365 / SharePoint Online**: Targeted by Helix vishing group and Forg365 PhaaS platform using AiTM, device code phishing, and MFA bypass techniques
- **7-Zip (Impersonated)**: Legitimate utility brand abused by Lurking Lizard for fake installer distribution converting systems to residential proxy nodes
- **AI Gateways**: Emerging attack surface providing access to AI models, cloud infrastructure, and IAM data as demonstrated by cryptomining incident
- **OpenMandriva Linux Distribution**: Targeted by internal contributor sabotage attempt affecting build integrity
- **AssuranceAmerica Insurance Systems**: Compromised leading to 6.9 million driver records exposed

## Attack Vectors and Techniques

- **Local Privilege Escalation via Defender Vulnerability**: Exploitation of CVE-2026-50656 in Windows Defender to achieve SYSTEM privileges from lower-privileged context
- **Bring Your Own Vulnerable Driver (BYOVD)**: Use of Microsoft-signed malicious kernel driver (PoisonX) to disable endpoint security solutions before ransomware deployment
- **Software Supply Chain Compromise**: GitHub repository takeover leading to malicious npm package publication (Injective SDK); insider sabotage attempt (OpenMandriva)
- **AI/ML Supply Chain Attacks**: Malicious repositories exploiting symlink handling in AI coding assistants (GhostApproval); AI agents tricked into executing code during analysis
- **Voice Phishing (Vishing)**: Telephone-based social engineering used by Helix group as initial access vector for SharePoint compromise
- **Device Code Phishing**: Exploitation of OAuth device authorization flow to bypass MFA and gain access to Microsoft 365/SharePoint resources
- **Adversary-in-the-Middle (AiTM) Phishing**: Real-time credential and session token interception used by Forg365 PhaaS platform
- **Multi-Factor Authentication Abuse**: MFA fatigue, token replay, and bypass techniques employed by Helix group for persistent access
- **Fake Software Installers**: Trojanized 7-Zip installers deploying residential proxy malware (Lurking Lizard campaign)
- **GitHub API Enumeration**: Automated reconnaissance of corporate GitHub organizations, repositories, and users via legitimate API endpoints using dormant accounts for stealth
- **AI Gateway Exploitation**: Targeting AI inference infrastructure to access models, cloud resources, and identity management systems
- **AI-Assisted Social Engineering**: Forg365 platform uses AI to generate tailored phishing lures at scale
- **Residential Proxy Botnet Creation**: Conversion of victim devices into proxy exit nodes for anonymizing malicious traffic (Lurking Lizard)

## Threat Actor Activities

- **Nightmare-Eclipse (Researcher)**: Published proof-of-concept exploit for Windows Defender zero-day (RoguePlanet/CVE-2026-50656) in early June 2026, along with several other Microsoft zero-days; responsible disclosure status unclear given public PoC release before patch
- **Helix (Data Extortion Group)**: New group employing sophisticated identity-focused attack chain (vishing, device code phishing, MFA abuse) targeting SharePoint for data theft and extortion; operates with PhaaS-like capabilities
- **Forg365 Operators (PhaaS Provider)**: Runs commercial phishing-as-a-service platform targeting Microsoft 365 with AiTM, device code phishing, and AI-generated lures; enables less-skilled attackers to conduct credential theft campaigns
- **Lurking Lizard (Threat Actor)**: Operates end-to-end residential proxy business using fake 7-Zip installers; maintains distribution infrastructure and proxy management platform for monetizing compromised devices
- **GodDamn Ransomware Operators**: Deploys GodDamn ransomware family using PoisonX BYOVD technique to disable defenses; primarily targets US companies; leverages Microsoft-signed malicious driver
- **Iranian State-Sponsored Actors**: Expanding targeting beyond critical infrastructure to any organization with internet-facing vulnerabilities; leveraging broad vulnerability scanning and exploitation
- **Datadog-Tracked GitHub Enumeration Campaigns (Unknown Operators)**: Multiple overlapping campaigns systematically mapping corporate GitHub assets via API using dormant accounts; likely reconnaissance for future supply chain or targeted attacks
- **OpenMandriva Saboteur (Insider)**: Project contributor who attempted sabotage following internal dispute; represents insider threat to open-source supply chain
- **AssuranceAmerica Breach Actors (Unattributed)**: Gained access to insurance systems earlier in 2026, exfiltrating 6.9 million driver records; attribution not publicly disclosed
- **AI Gateway Cryptominers (Unattributed)**: Exploited AI gateway access to deploy cryptomining operations and access cloud/IAM resources; demonstrates emerging targeting of AI infrastructure

## Source Attribution

- **OpenMandriva Linux says contributor tried to sabotage the project**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/openmandriva-linux-says-contributor-tried-to-sabotage-the-project/
- **Iran's Cyber Crosshairs Focus Beyond Critical Infrastructure**: Dark Reading - https://www.darkreading.com/cyber-risk/iran-cyber-crosshairs-beyond-critical-infrastructure
- **Microsoft Reins in RoguePlanet Zero-Day Threat**: Dark Reading - https://www.darkreading.com/vulnerabilities-threats/microsoft-rogueplanet-zero-day-threat
- **Injective SDK on npm infected with cryptocurrency wallet stealer**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/injective-sdk-on-npm-infected-with-cryptocurrency-wallet-stealer/
- **AI Agents Are a New Kind of Identity \&amp; Most Organizations Aren't Ready**: Dark Reading - https://www.darkreading.com/identity-access-management-security/ai-agents-new-kind-identity-most-organizations-not-ready
- **Dormant GitHub Accounts Help Attackers Blend In While Mapping Corporate Orgs**: The Hacker News - https://thehackernews.com/2026/07/dormant-github-accounts-help-attackers.html
- **New GigaWiper Windows Backdoor Bundles Disk Wiping, Fake Ransomware, and Spyware**: The Hacker News - https://thehackernews.com/2026/07/new-gigawiper-windows-backdoor-bundles.html
- **New Helix vishing group emerges in SharePoint data theft attacks**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/new-helix-vishing-group-emerges-in-sharepoint-data-theft-attacks/
- **Microsoft expects more Windows security updates from AI-discovered flaws**: Bleeping Computer - https://www.bleepingcomputer.com/news/microsoft/microsoft-expects-more-windows-security-updates-from-ai-discovered-flaws/
- **npm 12 Disables Install Scripts by Default to Reduce Supply Chain Risk**: The Hacker News - https://thehackernews.com/2026/07/npm-12-disables-install-scripts-by.html
- **ThreatsDay: Cloud Bucket Hijacking, Windows LPE Chain, Global Fraud Bust + 17 More Stories**: The Hacker News - https://thehackernews.com/2026/07/threatsday-cloud-bucket-hijacking.html
- **New Forg365 phishing platform uses AI to target Microsoft 365 accounts**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/new-forg365-phishing-platform-uses-ai-to-target-microsoft-365-accounts/
- **As Global Conflicts Go Digital, Businesses Need Wartime Gameplans**: Dark Reading - https://www.darkreading.com/cybersecurity-operations/businesses-wartime-cybersecurity-gameplans
- **The Hidden Security Risks of Reduced Summer IT Coverage**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/the-hidden-security-risks-of-reduced-summer-it-coverage/
- **AI Gateways Offer Attackers the Keys to the Kingdom**: Dark Reading - https://www.darkreading.com/cyber-risk/ai-gateways-keys-kingdom
- **AI Attacks Move in Minutes. Join This Webinar on Building a Defense That Keeps Up**: The Hacker News - https://thehackernews.com/2026/07/ai-attacks-move-in-minutes-join-this.html
- **Microsoft to retire the OWA Light client in Exchange Server**: Bleeping Computer - https://www.bleepingcomputer.com/news/microsoft/microsoft-announces-owa-light-retirement-in-exchange-server/
- **Summer of Clearinghouses**: The Hacker News - https://thehackernews.com/2026/07/summer-of-clearinghouses.html
- **GodDamn Ransomware Uses PoisonX Driver to Disable Endpoint Defenses**: The Hacker News - https://thehackernews.com/2026/07/goddamn-ransomware-uses-poisonx-driver.html
- **'GodDamn' Ransomware Uses BYOVD to Smite US Companies**: Dark Reading - https://www.darkreading.com/cyberattacks-data-breaches/goddamn-ransomware-byovd-smite-companies
- **Police arrests 5,800 suspects in global anti-fraud crackdown**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/police-arrests-5-800-suspects-in-global-anti-fraud-crackdown/
- **Microsoft Patches RoguePlanet Defender Flaw That Can Grant SYSTEM Privileges**: The Hacker News - https://thehackernews.com/2026/07/microsoft-patches-rogueplanet-defender.html
- **European Organizations Have a Collaboration Security Confidence Gap**: Dark Reading - https://www.darkreading.com/cybersecurity-operations/european-organizations-collaboration-security-confidence-gap
- **AssuranceAmerica data breach exposes records of 6.9 million drivers**: Bleeping Computer - https://www.bleepingcomputer.com/news/security/assuranceamerica-data-breach-exposes-records-of-69-million-drivers/
- **Meta's New AI Image Tool Lets Others Use Your Public Instagram Photos in AI Images**: The Hacker News - https://thehackernews.com/2026/07/metas-new-ai-image-tool-lets-others-use.html
- **Microsoft patches RoguePlanet Defender zero-day vulnerability**: Bleeping Computer - https://www.bleepingcomputer.com/news/microsoft/microsoft-patches-rogueplanet-defender-zero-day-vulnerability/
- **Top AI Agents Built to Catch Malicious Code Can Be Tricked Into Running It**: The Hacker News - https://thehackernews.com/2026/07/friendly-fire-ai-agents-built-to-catch.html
- **GhostApproval Symlink Flaws Could Let Malicious Repos Run Code in AI Coding Agents**: The Hacker News - https://thehackernews.com/2026/07/ghostapproval-symlink-flaws-could-let.html
- **Fake 7-Zip Installers Turn Devices Into Residential Proxy Nodes**: The Hacker News - https://thehackernews.com/2026/07/fake-7-zip-installers-turn-devices-into.html
- **Mexico's New Cyber Plan Faces Its First Real Test**: Dark Reading - https://www.darkreading.com/cyber-risk/mexicos-cyber-plan-first-real-test
