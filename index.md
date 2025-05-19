# Exploitation Report

# Comprehensive Exploitation Activity Report

## Summary of Critical Exploitation Activity

This report provides an analysis of recent cybersecurity threats and vulnerabilities that have been actively exploited. The focus is on zero-day vulnerabilities, recently patched vulnerabilities that were exploited, new attack vectors, and notable threat actors. The report also includes recommendations for mitigation.

## Exploited Vulnerabilities

### Zero-Day Vulnerabilities

1. **VMware ESXi and Microsoft SharePoint Zero-Days**
   - **Source**: [Hackers exploit VMware ESXi, Microsoft SharePoint zero-days at Pwn2Own](https://www.bleepingcomputer.com/news/security/hackers-exploit-vmware-esxi-microsoft-sharepoint-zero-days-at-pwn2own/)
   - **Details**: During Pwn2Own Berlin 2025, zero-day vulnerabilities in VMware ESXi and Microsoft SharePoint were exploited. These vulnerabilities allowed attackers to execute arbitrary code on the affected systems.
   - **Affected Systems**: VMware ESXi, Microsoft SharePoint
   - **Mitigation**: Organizations should apply patches released by VMware and Microsoft as soon as they are available and monitor for any unusual activity on these platforms.

2. **Chat App Zero-Day Exploited by Turkish APT**
   - **Source**: [Turkish APT Exploits Chat App Zero-Day to Spy on Iraqi Kurds](https://www.darkreading.com/cyberattacks-data-breaches/turkish-apt-exploits-chat-app-zero-day-spy-iraqi-kurds)
   - **Details**: A zero-day vulnerability in a chat application was exploited by the threat actor group Marbled Dust or Sea Turtle to spy on military targets.
   - **Affected Systems**: Specific chat application used by Iraqi Kurds
   - **Mitigation**: Users should update to the latest version of the chat application and apply any security patches provided by the vendor.

### Recently Patched Vulnerabilities

1. **Chrome Zero-Day**
   - **Source**: [CISA tags recently patched Chrome bug as actively exploited](https://www.bleepingcomputer.com/news/security/cisa-tags-recently-patched-chrome-bug-as-actively-exploited-zero-day/)
   - **Details**: A high-severity vulnerability in the Chrome web browser was actively exploited in the wild before being patched.
   - **Affected Systems**: Google Chrome
   - **Mitigation**: Users should update Chrome to the latest version immediately to protect against this vulnerability.

### New Attack Vectors and Techniques

1. **Defendnot Tool**
   - **Source**: [New 'Defendnot' tool tricks Windows into disabling Microsoft Defender](https://www.bleepingcomputer.com/news/microsoft/new-defendnot-tool-tricks-windows-into-disabling-microsoft-defender/)
   - **Details**: The 'Defendnot' tool disables Microsoft Defender by registering a fake antivirus product, even when no real AV is installed.
   - **Affected Systems**: Windows devices
   - **Mitigation**: Organizations should ensure that Microsoft Defender is configured correctly and monitor for unauthorized changes to antivirus settings.

2. **Dynamic DNS as a Cyberattack Facilitator**
   - **Source**: [Dynamic DNS Emerges as Go-to Cyberattack Facilitator](https://www.darkreading.com/threat-intelligence/dynamic-dns-cyberattack-facilitator)
   - **Details**: Threat actors are using dynamic DNS services to obfuscate their activities and impersonate well-known brands.
   - **Mitigation**: Implement DNS filtering and monitoring to detect and block suspicious DNS activity.

3. **Fileless Remcos RAT via LNK Files and MSHTA**
   - **Source**: [Fileless Remcos RAT Delivered via LNK Files and MSHTA in PowerShell-Based Attacks](https://thehackernews.com/2025/05/fileless-remcos-rat-delivered-via-lnk.html)
   - **Details**: A new malware campaign uses a PowerShell-based shellcode loader to deploy Remcos RAT, delivered via LNK files and MSHTA.
   - **Mitigation**: Disable the execution of scripts via MSHTA and monitor for suspicious PowerShell activity.

### Notable Threat Actors

1. **Marbled Dust/Sea Turtle**
   - **Activity**: Exploited a chat app zero-day to spy on Iraqi Kurds.
   - **Mitigation**: Organizations should enhance their threat intelligence capabilities to detect and respond to activities by this group.

2. **Scattered Spider and Other Phishers**
   - **Activity**: Using dynamic DNS services to facilitate cyberattacks.
   - **Mitigation**: Strengthen phishing defenses and educate users about the risks of dynamic DNS.

## Recommendations for Mitigation

- **Patch Management**: Ensure all systems are up-to-date with the latest security patches, especially for critical software like VMware ESXi, Microsoft SharePoint, and Google Chrome.
- **Endpoint Protection**: Use advanced endpoint protection solutions to detect and block malicious tools like 'Defendnot' and Remcos RAT.
- **Network Security**: Implement DNS filtering and monitoring to detect and block malicious domains and dynamic DNS abuse.
- **User Education**: Conduct regular security awareness training to educate users about phishing, social engineering, and the risks of unauthorized software.
- **Threat Intelligence**: Enhance threat intelligence capabilities to detect and respond to activities by known threat actors like Marbled Dust and Scattered Spider.

By following these recommendations, organizations can better protect themselves against the current landscape of cybersecurity threats and vulnerabilities.

## Active Exploitation Details



## Affected Systems and Products



## Attack Vectors and Techniques



## Threat Actor Activities

 