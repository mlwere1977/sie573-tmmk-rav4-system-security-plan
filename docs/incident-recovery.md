# Incident Response and Recovery

From SSP Sections 1.4 and 13.4 and the RMF Assessment's IR-4 strategy. The design principle: **contain locally before restoring, and never stop the whole JIT line for a problem confined to one cell or one vehicle.**

## Scenario A: supplier ransomware (Kojima-style, R-01)

| # | Phase | Action | Controls |
|:-:|---|---|---|
| 1 | **Detect** | Edge DMZ IDS, with remote probes in the OT networks, flags and logs suspicious activity. EDI anomaly rules in the SIEM catch volume drops and timeouts. | SI-4, SR-6 |
| 2 | **Contain** | On-site engineers isolate the affected zone at the internal firewalls, which stops lateral movement toward the Control and Floor VLANs | IR-4, SC-7 |
| 3 | **Report** | The ISSO escalates to the corporate SOC for joint containment. CIRCIA reporting applies once the final rule takes effect (72 h for incidents, 24 h for ransom payments). | IR-6 |
| 4 | **Sustain** | Active-active server groups and the redundant fiber ring keep unaffected cells running. JIT sequencing fails over to a buffered dataset. | CP-7, CP-8 |
| 5 | **Restore** | Compromised systems are rebuilt from nightly **WORM** backups, which ransomware cannot alter, then brought current from hourly file-level backups | CP-9 |
| 6 | **Verify** | Nodes are reflashed from registry images. Hashes are validated against the registry before the line is authorized to restart. | CP-10, CM-2 |
| 7 | **Improve** | Forensic timeline and lessons learned update the contingency plan and tune monitoring rules | CP-2, CP-4 |

## Scenario B: Final QA firmware hash mismatch (R-02)

```
Final QA hash ≠ registry hash
        │
        ├─► Vehicle auto-flagged and physically diverted to quarantine station
        ├─► Read/write frozen on the software-delivery segment for that build (no further OTA pushes)
        ├─► Incident ticket opened → enterprise SOC playbook
        ├─► Forensics: TPM boot/verification log + registry immutable changelog + signed-package hash
        │      → did the mismatch start in transit, at the TPM, or upstream in R&D signing?
        ├─► Unit reflashed from known-good signed image → re-verified against clean baseline hash
        └─► Findings fed into M-2 continuous-monitoring rules (closes the IR-4 feedback loop)

Containment target: 10–15 minutes · Scope: one vehicle + its local network drop, NOT the Floor VLAN
```

**Notified (RACI):** QA & Calibration Specialist (A/R for R-04, R for R-03) and Systems Security Engineer.

## Day-to-day security processes

1. **Patching:** tested before deployment. PLC and DCS firmware is updated in scheduled maintenance windows with a documented rollback plan, and compensating controls are used where no patch exists (SI-2).
2. **Monitoring:** Edge DMZ IDS with OT probes. OT-protocol-aware anomaly detection (e.g., Nozomi Guardian, Claroty CTD, Cisco Cyber Vision) is planned at the Control and Floor boundaries to flag unauthenticated PLC writes (SI-4, SI-4(2)).
3. **Change control:** every change to PLC logic, firewall rules, or software goes through formal change control and is tested in staging first (CM-3, CM-4).
4. **Backups:** nightly WORM plus hourly file-level backups (CP-9).
5. **Isolation:** zone-level isolation at the internal firewalls while the rest of the line runs (IR-4).
