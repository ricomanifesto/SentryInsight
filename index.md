# Exploitation Report

The current threat landscape shows active exploitation across multiple critical vulnerabilities affecting enterprise infrastructure, with several zero-day vulnerabilities being exploited in the wild. CISA has issued federal patching orders for actively exploited n8n workflow automation platform vulnerabilities that allow remote code execution and credential exposure. Microsoft's March 2026 Patch Tuesday addressed 79-84 security flaws, including two publicly disclosed zero-day vulnerabilities. Additionally, supply chain attacks continue to target software development ecosystems through compromised npm packages and GitHub Actions, while ransomware groups maintain aggressive campaigns against healthcare infrastructure in the Oceania region.

## Active Exploitation Details

### n8n Workflow Automation Platform Vulnerabilities
- **Description**: Critical security flaws in the n8n workflow automation platform that enable remote code execution and exposure of stored credentials
- **Impact**: Attackers can achieve arbitrary command execution on affected systems and access sensitive stored credentials
- **Status**: Actively exploited in attacks; CISA has ordered federal agencies to patch immediately

### Microsoft Zero-Day Vulnerabilities
- **Description**: Two publicly disclosed zero-day vulnerabilities included in Microsoft's March 2026 Patch Tuesday
- **Impact**: Various impacts across Windows operating systems and Microsoft software components
- **Status**: Publicly known vulnerabilities with patches now available

### Elementor Ally WordPress Plugin SQL Injection
- **Description**: SQL injection vulnerability in the Ally WordPress plugin from Elementor used for web accessibility and usability
- **Impact**: Allows exploitation to steal sensitive data without authentication
- **Status**: Affects over 250,000 WordPress installations; patch status not specified

## Affected Systems and Products

- **n8n Workflow Automation Platform**: Critical vulnerabilities allowing RCE and credential exposure
- **Microsoft Windows**: Multiple versions affected by 79-84 security vulnerabilities including two zero-days
- **WordPress Sites**: 250,000+ installations using Elementor Ally plugin vulnerable to SQL injection
- **Xygeni GitHub Action**: Compromised via tag poisoning attack with active C2 implant
- **HPE Aruba Networking AOS-CX**: Multiple authentication and code execution vulnerabilities
- **SAP Enterprise Software**: Two critical flaws enabling arbitrary code execution
- **Stryker Medical Technology Systems**: Targeted by Iran-linked wiper malware attack
- **Healthcare Systems**: Government agencies and emergency clinics in Australia, New Zealand, and Tonga

## Attack Vectors and Techniques

- **Supply Chain Compromise**: Malicious npm packages (PhantomRaven campaign with 88 packages) and Rust crates targeting developer environments
- **GitHub Action Tag Poisoning**: Compromise of Xygeni's xygeni/xygeni-action through malicious tag manipulation
- **Zombie ZIP Technique**: New compression-based evasion method to bypass antivirus and EDR solutions
- **Mobile Malware Distribution**: BeatBanker Android malware distributed through fake Starlink apps on counterfeit Google Play Store sites
- **EDR Evasion**: BlackSanta EDR killer targeting HR departments with advanced detection bypass capabilities
- **Wiper Malware Attacks**: Destructive attacks against medical technology infrastructure
- **CI/CD Pipeline Exploitation**: Malicious packages designed to steal environment files and developer secrets

## Threat Actor Activities

- **INC Ransomware Group**: Actively targeting healthcare infrastructure across Oceania region, including government agencies and emergency clinics
- **UNC6426**: Leveraged compromised nx npm package to achieve complete AWS cloud environment breach within 72 hours
- **Handala (Iranian-linked)**: Pro-Palestinian hacktivist group claiming responsibility for wiper malware attack against Stryker medical technology company
- **PhantomRaven Campaign**: Ongoing supply-chain attacks through npm registry with dozens of malicious packages targeting JavaScript developers
- **Chinese Nexus Actors**: Shifting focus to Qatar amid Iranian conflict, demonstrating rapid pivoting capabilities in response to geopolitical events
- **Sednit (Russian-affiliated)**: Resurfaced with sophisticated new malware toolkit after years of using simple implants
- **Russian-speaking Threat Actor**: Over one year campaign targeting HR departments with BlackSanta EDR killer malware