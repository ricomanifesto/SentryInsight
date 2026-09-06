---
schema_version: 2
report_date: 2026-09-06
generated_at: 2026-09-06T15:19:59Z
digest_issue_url: https://ricomanifesto.github.io/SentryDigest/archive/2026-09-06/
---
# Exploitation Report

## Executive Summary

Multiple critical vulnerabilities are under active exploitation across diverse technology stacks, ranging from e-commerce platforms and printing infrastructure to browser engines and network appliances. Attackers are leveraging both zero-day flaws and recently disclosed vulnerabilities within days of public availability, demonstrating rapid weaponization capabilities. The education sector faces targeted credential theft via PaperCut exploitation, while e-commerce sites suffer from an unpatched Magento/Adobe Commerce zero-day. Browser users remain at risk from an actively exploited Chrome V8 zero-day, and Citrix NetScaler appliances face authentication bypass attacks in the wild.

Threat actors are combining traditional vulnerability exploitation with novel evasion techniques, including ASCII smuggling using invisible Unicode characters to bypass email filters at massive scale. Compromised infrastructure is being repurposed for payload delivery through blockchain-hosted ClickFix campaigns affecting over 5,400 websites. Simultaneously, supply chain incidents like the ShipMonk breach and the JetBrains TeamCity compromise highlight the cascading impact of vulnerable third-party software. Privilege escalation capabilities continue to expand with a publicly released CrowdStrike Falcon zero-day and a stealthy Linux backdoor embedded in trojanized HAProxy builds.

## Active Exploitation Details

### PaperCut Authentication Bypass and RCE Chain
- **Description**: Attackers are exploiting a vulnerability chain in PaperCut print management software comprising an authentication bypass (CVE-2026-81578) and a remote code execution flaw (CVE-2026-82078). The Arctic Wolf Adversary Research Team observed threat actors using this chain for command execution and reconnaissance.
- **Impact**: Full command execution on PaperCut servers, credential theft, and network reconnaissance capabilities. Attacks specifically target the education sector in the U.S. and Europe.
- **Status**: Actively exploited in the wild since public disclosure. Patches available from PaperCut.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-81578, CVE-2026-82078
- **Reporting**: [The Hacker News — Attackers Exploit PaperCut Flaws to Steal Credentials From Schools and Universities](https://thehackernews.com/2026/09/attackers-exploit-papercut-flaws-to.html)

### Citrix NetScaler Authentication Bypass
- **Description**: A critical-severity authentication bypass vulnerability in Citrix NetScaler (formerly NetScaler ADC and Gateway) allows unauthenticated attackers to bypass authentication mechanisms. Previdian vulnerability intelligence confirms active targeting in the wild.
- **Impact**: Unauthenticated access to NetScaler management interfaces, potential full appliance compromise, and lateral movement into internal networks.
- **Status**: Active exploitation confirmed by Previdian. Citrix has released security updates.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-19490
- **Reporting**: [Bleeping Computer — Critical Citrix NetScaler auth bypass now leveraged in attacks](https://www.bleepingcomputer.com/news/security/hackers-target-critical-citrix-netscaler-auth-bypass-in-attacks/)

### Super Forms WordPress Plugin RCE
- **Description**: A missing file type validation vulnerability in Super Forms – Drag & Drop Form Builder WordPress plugin allows unauthenticated attackers to upload arbitrary files, including PHP webshells, leading to remote code execution. Wordfence observed over 440,000 exploit attempts targeting this flaw alongside Elementor Pro vulnerabilities.
- **Impact**: Complete compromise of WordPress sites, webshell deployment, data theft, and use as pivot points for further attacks.
- **Status**: Mass exploitation ongoing with 440,000+ attempts observed. Patch available in Super Forms update.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-14894
- **Reporting**: [The Hacker News — Over 440,000 Exploit Attempts Target Super Forms and Elementor Pro RCE Flaws](https://thehackernews.com/2026/09/over-440000-exploit-attempts-target.html)

### Chrome V8 Type Confusion Zero-Day
- **Description**: A high-severity type confusion vulnerability in the V8 JavaScript and WebAssembly engine of Google Chrome. Google confirmed active exploitation in the wild and released an emergency update addressing this flaw along with 11 other vulnerabilities.
- **Impact**: Remote code execution via crafted web pages, browser sandbox escape potential, and full system compromise when chained with additional exploits.
- **Status**: Actively exploited zero-day. Patched in Chrome 152.0.7977.82 and later versions.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-85046
- **Reporting**: [Bleeping Computer — Google warns of new Chrome zero-day flaw exploited in attacks](https://www.bleepingcomputer.com/news/security/google-warns-of-new-chrome-zero-day-flaw-exploited-in-attacks/), [The Hacker News — Google Releases Chrome Update to Patch Actively Exploited V8 Zero-Day](https://thehackernews.com/2026/09/google-releases-chrome-update-to-patch.html)

### Magento/Adobe Commerce StyleSmuggler Zero-Day
- **Description**: An unpatched zero-day vulnerability in Magento Open Source and Adobe Commerce, dubbed "StyleSmuggler" by Sansec, allows unauthenticated attackers to execute malicious code on online store servers. Attacks began on September 4, 2026, before any patch was available.
- **Impact**: Full server compromise, payment skimmer injection, customer data theft, and persistent backdoor installation on e-commerce platforms.
- **Status**: Active zero-day exploitation with no vendor patch available as of September 5. Sansec advisory published with mitigation guidance.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: mitigate
- **Reporting**: [The Hacker News — Unpatched Magento and Adobe Commerce Zero-Day Exploited to Backdoor Online Stores](https://thehackernews.com/2026/09/unpatched-magento-and-adobe-commerce.html)

### MikroTik Router SSH Exposure Exploitation
- **Description**: Attackers are hijacking MikroTik routers with internet-exposed SSH services to gain full administrative control without authentication. CERT Polska issued a warning on September 5 confirming successful attacks dating to at least September 2.
- **Impact**: Complete router compromise, traffic interception, network pivoting, DDoS botnet recruitment, and persistent access via modified configurations.
- **Status**: Active exploitation confirmed. No authentication bypass vulnerability—exploitation leverages misconfigured internet-exposed SSH with weak/default credentials.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: mitigate
- **Reporting**: [The Hacker News — Attackers Hijack MikroTik Routers Through Internet-Exposed SSH Without Authentication](https://thehackernews.com/2026/09/attackers-hijack-mikrotik-routers.html)

### JetBrains TeamCity Exploitation (Cadence Breach)
- **Description**: Unidentified threat actors exploited a recently disclosed critical vulnerability in JetBrains TeamCity to breach the JetBrains Cadence environment and extract AWS credentials. JetBrains urged all Cadence users to immediately revoke and rotate credentials.
- **Impact**: Supply chain compromise, AWS credential theft, potential access to customer CI/CD pipelines and cloud resources.
- **Status**: Confirmed breach via active exploitation of a recently disclosed TeamCity vulnerability. JetBrains has patched TeamCity.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: [The Hacker News — Attackers Breached JetBrains Cadence via Unpatched TeamCity, Extracting AWS Credentials](https://thehackernews.com/2026/09/attackers-breached-jetbrains-cadence.html)

### CrowdStrike Falcon FalconFlank Zero-Day
- **Description**: An anonymous researcher ("Nightmare Eclipse") publicly released a zero-day exploit named "FalconFlank" targeting CrowdStrike Falcon sensor on Windows, granting SYSTEM privileges on fully patched systems. The exploit demonstrates privilege escalation from standard user to SYSTEM.
- **Impact**: Local privilege escalation to SYSTEM, security product tampering, defense evasion, and persistence establishment on endpoints running CrowdStrike Falcon.
- **Status**: Public exploit code released. Active exploitation status unknown; defenders should investigate for signs of compromise.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: investigate
- **Reporting**: [Bleeping Computer — New CrowdStrike 'FalconFlank' zero-day grants SYSTEM privileges](https://www.bleepingcomputer.com/news/security/new-crowdstrike-falconflank-zero-day-grants-system-privileges/)

## Affected Systems and Products

- **PaperCut NG/MF**: All versions prior to the September 2026 security release; education sector deployments heavily targeted
- **Citrix NetScaler ADC and Gateway**: Versions affected by CVE-2026-19490; internet-exposed management interfaces at highest risk
- **Super Forms WordPress Plugin**: Versions prior to patched release; WordPress sites using the drag-and-drop form builder
- **Elementor Pro WordPress Plugin**: Versions affected by undisclosed RCE flaw; actively exploited alongside Super Forms
- **Google Chrome**: Versions prior to 152.0.7977.82 on Windows, Mac, and Linux; all platforms with V8 engine
- **Magento Open Source**: All current versions vulnerable to StyleSmuggler; no patch available as of advisory date
- **Adobe Commerce**: All current versions (cloud and on-premise) vulnerable to StyleSmuggler; no patch available
- **MikroTik RouterOS**: Devices with SSH (port 22) exposed to internet; all versions with default/weak credentials
- **JetBrains TeamCity**: Versions prior to the critical vulnerability patch; Cadence users specifically impacted by credential exposure
- **CrowdStrike Falcon Sensor**: Windows sensor versions vulnerable to FalconFlank; all up-to-date systems reportedly affected

## Attack Vectors and Techniques

- **ASCII Smuggling / Invisible Unicode Phishing**: Attackers embed invisible Unicode tag characters (e.g., U+E0001) within financial lure words like "funding" to split keywords and evade email security filters while rendering normally to recipients. Microsoft tracks high-volume campaigns using this technique.
- **Blockchain-Hosted Payload Delivery**: ClickFix payloads stored in smart contracts on BNB Smart Chain (BSC) served from 5,400+ compromised small-business websites. Attackers leverage blockchain immutability for resilient payload hosting.
- **Authentication Bypass Chains**: PaperCut exploitation combines CVE-2026-81578 (auth bypass) with CVE-2026-82078 (RCE) for unauthenticated remote code execution without valid credentials.
- **Exposed Management Interfaces**: MikroTik routers with SSH exposed to internet; Citrix NetScaler management interfaces accessible externally—both exploited without credential requirements due to configuration flaws or vulnerabilities.
- **Supply Chain Credential Theft**: TeamCity compromise yielded AWS credentials used in Cadence executions; ShipMonk breach exposed 67,000 Trezor customer records including PII and order data.
- **Trojanized Legitimate Software**: Ted backdoor compiled directly into HAProxy load balancers of South Korean organizations, intercepting and modifying web traffic for selected visitors.
- **Privilege Escalation via Security Software**: FalconFlank exploits CrowdStrike Falcon kernel driver to achieve SYSTEM from standard user, subverting the very tool deployed for protection.
- **Post-Exploitation Defense Disabling**: REVSTEALER modules (ProManager, WinUpdate, SoftManager) disable Windows Update and Microsoft Defender before deploying cryptocurrency miners.

## Threat Actor Activities

- **Arctic Wolf Observed Actors**: Targeting education sector (schools and universities) in U.S. and Europe via PaperCut vulnerability chain for credential theft and reconnaissance.
- **Sansec-Tracked E-commerce Attackers**: Exploiting StyleSmuggler zero-day in Magento/Adobe Commerce since September 4 for payment skimming and persistent backdoor installation on online stores.
- **CERT Polska Monitored Actors**: Hijacking internet-exposed MikroTik routers via SSH since at least September 2 for full administrative control; no specific attribution provided.
- **JetBrains Intrusion Actors**: Unidentified threat actors exploited TeamCity vulnerability to breach Cadence environment and extract AWS credentials; potential supply chain targeting.
- **ClickFix Campaign Operators**: Large-scale operation compromising 5,400+ small-business websites to deliver blockchain-hosted payloads; financially motivated cybercriminal group.
- **Phishing Campaign Operators**: High-volume email campaigns using invisible Unicode evasion (ASCII smuggling) targeting financial lures; Microsoft Security Research tracking.
- **Nightmare Eclipse**: Anonymous security researcher who publicly released FalconFlank zero-day exploit for CrowdStrike Falcon; motivation appears to be vulnerability disclosure via full exploit publication.
- **Ted Backdoor Operators**: Unknown threat actors targeting South Korean organizations via trojanized HAProxy builds; implant named "ted" in debug strings; capability to intercept and alter web traffic selectively.
- **REVSTEALER Operators**: Emerging Windows information stealer campaign deploying four post-exploitation modules (ProManager, WinUpdate, SoftManager, and one unnamed) to disable defenses and mine cryptocurrency.