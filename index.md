# Exploitation Report

# Comprehensive Exploitation Report - May 2025

## Summary of Critical Exploitation Activity

This report provides an analysis of recent exploitation activities, focusing on zero-day vulnerabilities, recently patched vulnerabilities that were exploited, new attack vectors, and notable threat actors. The report highlights vulnerabilities affecting major software and systems, including Microsoft products, Fortinet, SAP, and Intel CPUs, among others.

## Exploited Vulnerabilities

### Zero-Day Vulnerabilities

1. **CVE-2025-32756** - Fortinet FortiVoice Systems
   - **Description**: A critical remote code execution (RCE) vulnerability exploited as a zero-day.
   - **Impact**: Allows attackers to execute arbitrary code on vulnerable systems.
   - **Affected Systems**: Fortinet FortiVoice enterprise phone systems.
   - **Mitigation**: Apply the latest security patches released by Fortinet.

2. **CVE-2025-31324** - SAP NetWeaver
   - **Description**: A critical vulnerability exploited by China-linked APTs to breach critical systems.
   - **Impact**: Compromise of critical infrastructure networks.
   - **Affected Systems**: SAP NetWeaver servers.
   - **Mitigation**: Implement SAP's security updates immediately.

3. **Windows Zero-Day** - Browser-Led RCE
   - **Description**: A zero-day vulnerability in Windows exploited for remote code execution via browsers.
   - **Impact**: Allows attackers to execute code remotely.
   - **Affected Systems**: Windows operating systems.
   - **Mitigation**: Apply Microsoft's May 2025 Patch Tuesday updates.

### Recently Patched Vulnerabilities

1. **Azure DevOps Server** - CVSS 10 Bug
   - **Description**: A critical vulnerability with a CVSS score of 10 impacting Azure DevOps Server.
   - **Impact**: Potential for complete system compromise.
   - **Affected Systems**: Azure DevOps Server.
   - **Mitigation**: Apply the latest patches from Microsoft.

2. **Ivanti EPMM Vulnerabilities**
   - **Description**: Two vulnerabilities in Ivanti Endpoint Manager Mobile (EPMM) exploited for remote code execution.
   - **Impact**: Allows attackers to chain vulnerabilities for RCE.
   - **Affected Systems**: Ivanti EPMM software.
   - **Mitigation**: Update to the latest version as per Ivanti's advisories.

3. **Intel CPU Flaws** - Branch Privilege Injection
   - **Description**: A flaw in Intel CPUs allowing data leakage from privileged memory.
   - **Impact**: Potential exposure of sensitive data.
   - **Affected Systems**: All modern Intel CPUs.
   - **Mitigation**: Apply firmware updates and patches from Intel.

### New Attack Vectors and Techniques

- **Earth Ammit Campaigns**: Targeting drone supply chains via ERP systems in Taiwan and South Korea.
- **Horabot Malware**: Distributed via invoice-themed phishing emails targeting Latin American countries.
- **Malicious PyPI Package**: A package posing as a Solana tool, stealing source code upon download.

### Notable Threat Actors

- **Earth Ammit**: Engaged in cyber espionage targeting military and satellite sectors.
- **China-Linked APTs**: Exploiting SAP vulnerabilities to target critical infrastructure.
- **Konni (Opal Sleet, TA406)**: North Korean group targeting Ukrainian government entities.

## Recommendations for Mitigation

1. **Patch Management**: Regularly apply security patches from vendors like Microsoft, Fortinet, SAP, and Intel.
2. **Network Segmentation**: Isolate critical systems to limit the impact of potential breaches.
3. **Phishing Awareness**: Educate employees about phishing threats and implement email filtering solutions.
4. **Endpoint Protection**: Deploy advanced endpoint protection solutions to detect and mitigate malware.
5. **Regular Audits**: Conduct regular security audits and vulnerability assessments to identify and remediate weaknesses.

By staying informed and proactive, organizations can better protect themselves against the evolving threat landscape.

## Active Exploitation Details



## Affected Systems and Products



## Attack Vectors and Techniques



## Threat Actor Activities

 