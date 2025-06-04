# Exploitation Report

Below is a comprehensive account of all newly disclosed or actively exploited vulnerabilities and attack techniques referenced across the provided articles. This includes zero-days, recently patched issues, and exploitation methods in the wild. Where specific CVE IDs are unknown or unmentioned, the vulnerabilities are described using the details available.

• Cisco Identity Services Engine (ISE) and Customer Collaboration Platform (CCP) vulnerabilities with public exploit code (CVE IDs not provided)  
• Three (3) exploited Qualcomm security flaws (CVE IDs not provided)  
• A newly discovered critical 10-year-old Roundcube Webmail vulnerability (CVE ID not provided)  
• A new Google Chrome zero-day (CVE ID not provided), actively exploited in the wild  
• Multiple HPE StoreOnce vulnerabilities, including a remote authentication bypass flaw (CVE IDs not provided)  
• Various attacks leveraging misconfigured or vulnerable ASUS routers, potentially turning them into botnet nodes (no CVE specified)  

Other noteworthy exploitation avenues and techniques described (no explicit CVEs provided):  
• Kerberos AS-REP “roasting” attacks, targeting weak Active Directory configurations  
• Malicious open-source packages on PyPI, npm, and RubyGems draining cryptocurrency wallets and exfiltrating data  
• Social engineering and phishing campaigns (e.g., “vishing” attacks on Salesforce, malicious RAT distributions, and NFT airdrop scams)  

## Active Exploitation Details

1. Cisco ISE and CCP Vulnerabilities  
   • Attackers are exploiting three vulnerabilities in Cisco’s Identity Services Engine (ISE) and Customer Collaboration Platform (CCP).  
   • Public exploit code for these flaws is available, making exploitation more likely.  
   • Potential impact includes unauthorized access to network services, privilege escalation, and compromise of customer interaction services.

2. Qualcomm Exploited Security Flaws  
   • Qualcomm recently patched three critical security vulnerabilities actively exploited in the wild.  
   • Exploitation affects devices that rely on Qualcomm chipsets or firmware, though exact methods are not fully detailed.  
   • Mobile device manufacturers must still integrate the patches, leaving end-users potentially exposed.

3. Critical Roundcube Webmail Vulnerability (10-Year-Old Flaw)  
   • A high-impact bug in Roundcube has existed undetected for a decade.  
   • Authenticated users can run arbitrary malicious code.  
   • This can lead to full compromise of the webmail environment if exploited by insider threats or anyone able to gain (even limited) credentials.

4. Google Chrome Zero-Day  
   • Google released an out-of-band patch for a high-severity vulnerability under active exploitation.  
   • The flaw allows attackers to compromise Chrome users who visit malicious or compromised websites.  
   • Users are urged to update their browsers immediately.

5. HPE StoreOnce Authentication Bypass and Related Flaws  
   • HPE issued patches for eight StoreOnce issues, including a severe remote authentication bypass.  
   • While not explicitly confirmed as “actively exploited,” these vulnerabilities pose a high risk of unauthorized entry if left unpatched.  
   • Attackers could potentially seize control of backup infrastructure or exfiltrate sensitive backup data.

6. ASUS Router Botnet Exploitation  
   • Thousands of ASUS routers have been compromised, forming part of an emerging botnet.  
   • Although no specific CVE was cited, exploitation likely targets known router weaknesses or default misconfigurations.  
   • Attacks can lead to router hijacking, lateral movement inside home/office networks, and denial-of-service (DDoS) campaigns.

7. Kerberos AS-REP Roasting Attacks  
   • Attackers use missing Kerberos preauthentication (AS-REP) in Active Directory to retrieve password hashes.  
   • Weak or easily crackable passwords can be exposed quickly, enabling lateral movement.  
   • Though not tied to a specific CVE, this method is an ongoing, impactful exploitation tactic.

8. Malicious Software Supply Chain (PyPI, npm, Ruby)  
   • Threat actors publish malicious packages that steal crypto wallet contents, exfiltrate data, or delete local files.  
   • No specific CVEs are provided; the packages are trojanized from the outset.  
   • This highlights continuing software supply chain threats.

## Affected Systems and Products

• Cisco Identity Services Engine (ISE) and Customer Collaboration Platform (CCP)  
• Qualcomm-based devices (smartphones, tablets, IoT devices)  
• Roundcube Webmail deployments (all versions unpatched for the 10-year-old bug)  
• Google Chrome (all platforms prior to the latest emergency patch)  
• HPE StoreOnce backup and deduplication systems  
• ASUS routers (various models targeted, specifics unlisted)  
• Windows Active Directory environments susceptible to AS-REP roasting  
• Open-source package repositories (PyPI, npm, RubyGems) with malicious or trojanized packages

## Attack Vectors and Techniques

• Exploit Code for Cisco Products: Public code allows attackers to escalate privileges or execute arbitrary commands in both ISE and CCP.  
• Mobile Exploitation of Qualcomm Flaws: Attackers can compromise unpatched Android devices at firmware or driver levels.  
• Authentication Bypass in HPE StoreOnce: Remote exploitation bypasses normal login protections, enabling privileged actions on backup systems.  
• Drive-by Exploit of Chrome Zero-Day: Visiting malicious web pages with an outdated Chrome browser can trigger remote code execution.  
• Botnet Formation via ASUS Routers: Threat actors exploit router misconfigurations or unpatched flaws to conscript routers into DDoS or spam botnets.  
• Kerberos AS-REP Roasting: Attackers request encrypted TGT data for accounts not requiring preauthentication, then crack offline.  
• Malicious Software Supply Chain: Trojanized packages in PyPI, npm, and Ruby cause data theft, cryptojacking, or destruction of local data.  
• Phishing and Social Engineering: Employees and users are tricked via vishing or malicious websites into running harmful executables (e.g., NetSupport RAT, Chaos RAT).

## Threat Actor Activities

• Play Ransomware Gang: Responsible for compromises of over 900 organizations; however, no specific CVEs were referenced.  
• Hacker Compromising Hosting Accounts: Used illicit access to mine cryptocurrency, but details on exploited flaws remain undisclosed.  
• Malicious Supply Chain Actors: Releasing counterfeit open-source packages for crypto theft, code destruction, and data exfiltration.  
• Vishing Group UNC6040 (Fake Data Loader App): Targets Salesforce instances for data extortion, employing phone-based social engineering.  
• ASUS Router Botnet Operators: Leveraging router weaknesses to create a widely distributed malicious network.  
• Chrome Zero-Day Exploiters: Unknown threat actors actively targeting unpatched Chrome installations.  
• Roundcube Webmail Exploiters: Potentially insider or lateral attackers who can authenticate and escalate via the 10-year-old bug.

These vulnerabilities and exploitation techniques underscore the importance of continuous patching, strong password policies, vigilant monitoring of supply chain components, and security awareness training to defend against both zero-day exploits and known attack vectors.