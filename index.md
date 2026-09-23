---
schema_version: 2
report_date: 2026-09-23
generated_at: 2026-09-23T11:15:35Z
digest_issue_url: https://ricomanifesto.github.io/SentryDigest/archive/2026-09-23/
---
# Exploitation Report

## Executive Summary

Multiple critical zero-day vulnerabilities are under active exploitation across diverse technology stacks, with threat actors chaining browser and operating system flaws for initial access and targeting network infrastructure, identity systems, and AI gateways. Chinese-affiliated actors including UTA0565 have weaponized a three-vulnerability Chrome-Windows exploit chain to deploy CLEANGULP malware, while the ShinyHunters extortion group claims breaches of the FBI and other organizations leveraging an alleged Oracle PeopleSoft zero-day. Simultaneously, financially motivated operators run phishing-as-a-service platforms such as EvilTokens, which compromised over 12,000 Microsoft 365 accounts before disruption, and supply chain attacks via malicious npm packages continue to steal credentials from developers.

Network and security infrastructure vendors have issued emergency patches for actively exploited flaws: F5 BIG-IP APM (CVE-2026-94127) enables unauthenticated remote code execution on OAuth authorization servers; Check Point Security Management Server (CVE-2026-93616) allows unauthenticated script execution; VeloCloud Orchestrator (CVE-2026-93952, CVSS 10.0) is under active exploitation in certificate-based deployments; and Bifrost AI Gateway (CVE-2026-90898, CVSS 9.8) permits unauthenticated command execution. D-Link has disclosed a maximum-severity zero-day (CVE-2026-86296) in legacy DIR-822A routers with public proof-of-concept code and no patch available. WordPress has released fixes for a critical core flaw affecting all supported branches back to 4.7.

New attack techniques are emerging around AI-driven post-exploitation automation, rogue multi-factor authentication providers that harvest credentials, and device-code phishing at scale. The Gulf region—particularly the UAE and Saudi Arabia—absorbs a disproportionate share of global attack volume, while Chinese actors leverage massive relay networks to access frontier AI models. Defenders should prioritize immediate patching of the listed CVEs, investigate potential compromise on internet-exposed management interfaces, and harden identity and supply chain controls.

## Active Exploitation Details

### F5 BIG-IP APM OAuth Zero-Day
- **Description**: Critical vulnerability in F5 BIG-IP Access Policy Manager (APM) that allows unauthenticated remote code execution on systems where APM is configured as an OAuth authorization server issuing access tokens to applications.
- **Impact**: Attackers can execute arbitrary code on the BIG-IP system without authentication, leading to full device compromise and potential lateral movement.
- **Status**: Actively exploited in the wild as a zero-day. F5 disclosed the flaw on September 22, 2026 and released engineering hotfixes.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-94127
- **Reporting**: [The Hacker News — F5 Patches Critical BIG-IP APM Zero-Day Exploited for Unauthenticated RCE on OAuth Servers](https://thehackernews.com/2026/09/f5-patches-critical-big-ip-apm-zero-day.html), [Bleeping Computer — F5 patches BIG-IP APM zero-day flaw exploited in RCE attacks](https://www.bleepingcomputer.com/news/security/f5-warns-of-big-ip-apm-remote-code-execution-zero-day-exploited-in-attacks/)

### Chrome-Windows Zero-Day Exploit Chain
- **Description**: A chain of three zero-day vulnerabilities—two in Google Chrome (CVE-2026-85046, CVE-2026-87491) and one in Windows Advanced Local Procedure Call (CVE-2026-85880)—chained together via fake websites to achieve remote code execution and sandbox escape.
- **Impact**: Full system compromise on targeted Windows hosts, enabling deployment of the CLEANGULP malware payload.
- **Status**: Actively exploited as zero-days on September 3–4, 2026. Patches for the individual components are assumed to be in progress or released by vendors.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-85046, CVE-2026-87491, CVE-2026-85880
- **Reporting**: [The Hacker News — Chinese Hackers Exploit Chrome-Windows Zero-Day Chain to Deploy CLEANGULP Malware](https://thehackernews.com/2026/09/chinese-hackers-exploit-chrome-windows.html)

### Check Point Security Management Server Zero-Day
- **Description**: Flaw in Check Point's Security Management Server web service that allows an authenticated or unauthenticated attacker with network access to the web interface to execute arbitrary scripts on the server without logging in.
- **Impact**: Full control over the management server that controls firewall policies, enabling policy manipulation, credential theft, and lateral movement.
- **Status**: Exploited in targeted attacks on July 23, 2026. Check Point released a fix on September 22, 2026.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-93616
- **Reporting**: [The Hacker News — Check Point Warns of Management Server Zero-Day Exploited in Targeted Attacks](https://thehackernews.com/2026/09/check-point-warns-of-management-server.html), [Bleeping Computer — Check Point warns of Management Server zero-day exploited in attacks](https://www.bleepingcomputer.com/news/security/check-point-patches-management-server-zero-day-exploited-in-attacks/)

### Bifrost AI Gateway Unauthenticated RCE
- **Description**: Critical vulnerability in the Bifrost open-source AI gateway (HTTP transport) that allows an unauthenticated attacker to execute arbitrary commands on the gateway server with a single HTTP request when management authentication is not properly configured.
- **Impact**: Complete server takeover, potential access to LLM provider credentials, and abuse of routed AI traffic.
- **Status**: Publicly disclosed with CVSS 9.8. Affects all versions before 2.1.0. Exploitation status in the wild is not explicitly confirmed but the flaw is trivially exploitable.
- **Severity**: critical
- **Exploitation Status**: potential
- **Action**: patch
- **CVE IDs**: CVE-2026-90898
- **Reporting**: [The Hacker News — Critical Bifrost AI Gateway Flaw Lets Attackers Run Commands Without Credentials](https://thehackernews.com/2026/09/critical-bifrost-ai-gateway-flaw-lets.html)

### VeloCloud Orchestrator Certificate Authentication Flaw
- **Description**: Flaw in on-premises VeloCloud Orchestrator (VCO) that may allow a remote unauthenticated attacker to privilege internal functions and affect the VCO host. Only orchestrators configured to authenticate Edge devices with certificates are affected.
- **Impact**: Unauthenticated remote compromise of the SD-WAN management plane, potentially affecting all managed Edge devices.
- **Status**: Actively exploited in the wild as of September 22, 2026. Arista has released mitigations.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-93952
- **Reporting**: [The Hacker News — New CVSS 10.0 VeloCloud Orchestrator Flaw Actively Exploited in Certificate-Based Setups](https://thehackernews.com/2026/09/new-cvss-100-velocloud-orchestrator.html)

### D-Link DIR-822A Router Zero-Day
- **Description**: Maximum-severity vulnerability in legacy DIR-822A dual-band Wi-Fi routers with public proof-of-concept exploit code available. No patch exists as the device is end-of-life.
- **Impact**: Full device compromise, potential network pivot, and recruitment into botnets.
- **Status**: Zero-day with public PoC; no patch will be issued. D-Link recommends replacing affected devices.
- **Severity**: critical
- **Exploitation Status**: potential
- **Action**: mitigate
- **CVE IDs**: CVE-2026-86296
- **Reporting**: [Bleeping Computer — D-Link warns of max severity zero-day bug in DIR-822A routers](https://www.bleepingcomputer.com/news/security/d-link-warns-of-max-severity-zero-day-bug-in-dir-822a-routers/)

### WordPress Core Critical Flaw
- **Description**: Critical vulnerability in WordPress core that allows an unauthenticated attacker to cause the site to load a PHP file from outside theme directories. On certain server configurations, this escalates to arbitrary code execution.
- **Impact**: Unauthenticated remote code execution on vulnerable WordPress installations, leading to site takeover and server compromise.
- **Status**: Patched on September 22, 2026 in WordPress 7.1.2 with backported fixes for all supported branches back to 4.7. Active exploitation status not explicitly confirmed.
- **Severity**: critical
- **Exploitation Status**: potential
- **Action**: patch
- **Reporting**: [The Hacker News — WordPress Issues Patch for Critical Flaw That Can Enable Code Execution on Some Servers](https://thehackernews.com/2026/09/wordpress-issues-patch-for-critical.html)

### Oracle PeopleSoft Zero-Day (Alleged)
- **Description**: ShinyHunters claims to have breached FBI systems using a previously unknown vulnerability in Oracle PeopleSoft, gaining access to internal services and exfiltrating sensitive personnel data.
- **Impact**: Unauthorized access to enterprise HR and administrative systems, mass data theft of employee and applicant records.
- **Status**: Claimed by threat actor; no vendor advisory or CVE published at time of reporting. Verification pending.
- **Severity**: unknown
- **Exploitation Status**: observed
- **Action**: investigate
- **Reporting**: [Bleeping Computer — ShinyHunters claims FBI hack, data theft in PeopleSoft zero-day breach](https://www.bleepingcomputer.com/news/security/shinyhunters-claims-fbi-hack-data-theft-in-peoplesoft-zero-day-breach/)

### BigDiskBuster Microsoft Defender Denial-of-Service
- **Description**: Proof-of-concept tool that fills all available disk space to prevent Microsoft Defender from installing platform and signature updates, effectively disabling protection.
- **Impact**: Persistent degradation of endpoint defenses, facilitating follow-on malware execution.
- **Status**: PoC published on GitHub September 19, 2026. No patch, CVE, or Microsoft advisory exists. Author is a former Microsoft security researcher.
- **Severity**: unknown
- **Exploitation Status**: potential
- **Action**: monitor
- **Reporting**: [The Hacker News — Researcher Drops BigDiskBuster Zero-Day PoC That Blocks Microsoft Defender Updates](https://thehackernews.com/2026/09/researcher-drops-bigdiskbuster-zero-day.html)

## Affected Systems and Products

- **F5 BIG-IP Access Policy Manager (APM)**: Systems configured as OAuth authorization servers; engineering hotfixes available from F5.
- **Google Chrome (Windows)**: Versions prior to patches for CVE-2026-85046 and CVE-2026-87491; Windows OS versions vulnerable to CVE-2026-85880 (ALPC).
- **Check Point Security Management Server**: All versions prior to the September 22, 2026 hotfix; manages firewall policies for Check Point gateways.
- **Bifrost AI Gateway (HTTP transport)**: All versions before 2.1.0 when management authentication is not enforced; routes requests to 20+ LLM providers.
- **VeloCloud Orchestrator (on-premises)**: Certificate-based Edge authentication deployments; Arista patches released September 22, 2026.
- **D-Link DIR-822A Dual-Band Wi-Fi Routers**: Legacy end-of-life devices; no patch available; public PoC exploit code circulating.
- **WordPress Core**: All versions from 4.7 through 7.1.1; patched in 7.1.2 and corresponding branch updates.
- **Oracle PeopleSoft**: Version(s) unknown; alleged zero-day exploited per ShinyHunters claim; no vendor confirmation.
- **ZyXEL GS1900 Smart Managed Switches**: Vulnerable firmware versions exploited by Chinese-speaking actor; specific versions not disclosed.
- **Microsoft 365 / Azure AD**: Targeted by EvilTokens device-code phishing campaign; 12,000+ accounts compromised across 10,000+ organizations.
- **npm Ecosystem**: Malicious package "tw-pkgprobe-7731" (supply chain); TanStack npm supply chain attack vector used against CrowdSec.
- **Next.js Applications**: Those using ImageResponse with attacker-controlled input (e.g., URL parameters) in social preview generation; fixed in latest release.

## Attack Vectors and Techniques

- **Browser-OS Exploit Chain**: Chaining Chrome renderer vulnerabilities (CVE-2026-85046, CVE-2026-87491) with a Windows ALPC elevation-of-privilege flaw (CVE-2026-85880) delivered via malicious websites to achieve sandbox escape and code execution.
- **Device Code Phishing (PhaaS)**: EvilTokens platform abused OAuth 2.0 device authorization flow at scale, using AI-generated lures and automation to compromise 12,000+ Microsoft 365 accounts across 10,000+ organizations.
- **Rogue External MFA Provider Registration**: Attackers with privileged access register a malicious external multi-factor authentication provider that intercepts user credentials during legitimate login flows.
- **Supply Chain Compromise via npm**: Malicious packages (e.g., "tw-pkgprobe-7731") masquerading as legitimate security tools exfiltrate credentials; TanStack npm attack stole OAuth tokens from a former employee's machine to access CrowdSec's GitHub repositories.
- **Unauthenticated Management Interface Exploitation**: Direct exploitation of internet-exposed management consoles (F5 BIG-IP APM, Check Point SMS, VeloCloud Orchestrator, Bifrost AI Gateway) without authentication.
- **AI-Driven Post-Exploitation Automation**: ClosedQuorum malware leverages Google Gemini, DeepSeek, Qwen, and Mistral models to autonomously decide lateral movement, persistence, and data collection actions.
- **Malicious OAuth Applications**: Attackers register deceptive OAuth apps to gain persistent access to Google Workspace and Microsoft 365 environments via user consent grants.
- **Disk Space Exhaustion Anti-Forensics**: BigDiskBuster tool fills disk capacity to block Microsoft Defender signature and platform updates, disabling protective capabilities.

## Threat Actor Activities

- **UTA0565 (Chinese-nexus)**: Conducted zero-day exploit chain attacks against Chrome and Windows on September 3–4, 2026, deploying CLEANGULP malware via fake websites. Demonstrates advanced exploit development and operational security.
- **ShinyHunters (Extortion Group)**: Claims responsibility for FBI breach via alleged Oracle PeopleSoft zero-day, advertising stolen agent and applicant data on dark web. Also claimed prior FBI breach in September 2026. Operates as a data theft and extortion collective.
- **Chinese-Speaking Threat Actor (Unnamed)**: Exploited vulnerabilities in ZyXEL GS1900 switches and WordPress to compromise 996 devices and exfiltrate 18,500+ records from backend databases, targeting government-adjacent entities.
- **EvilTokens Operators (PhaaS)**: Ran a device-code phishing-as-a-service platform leveraging AI at every attack stage. Compromised 12,000+ Microsoft accounts at 10,000+ organizations before coordinated takedown by Microsoft DCU, Health-ISAC, Cloudflare, Coinbase, OpenAI, Railway, SpyCloud, and Shadowserver.
- **Shai-Hulud (Supply Chain Actor)**: Executed TanStack npm supply chain attack, stealing OAuth token from former employee's computer to access and exfiltrate 170 private repositories from cybersecurity firm CrowdSec's GitHub organization.
- **Abdelhamid Naceri (Independent Researcher / Former Microsoft)**: Published BigDiskBuster zero-day PoC for Microsoft Defender update denial; previous Defender exploits attributed to this researcher have been used in real-world attacks.
- **twdepprobe7731 (npm Threat Actor)**: Published malicious package "tw-pkgprobe-7731" in mid-August 2026, posing as a Twilio bug-bounty probe to harvest developer credentials.