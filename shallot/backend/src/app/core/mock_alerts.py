from datetime import datetime, timedelta
from typing import Any, Dict, List


def get_mock_alerts(limit: int = 5) -> List[Dict[str, Any]]:
    """Return sample Security Onion-style alerts for demo mode."""
    now = datetime.utcnow()
    alerts = [
        {
            "name": "ET TROJAN Suspicious PowerShell Encoded Command",
            "severity_label": "HIGH",
            "ruleid": "2024211",
            "eventid": "demo-evt-001",
            "source_ip": "10.10.20.15",
            "source_port": "54218",
            "destination_ip": "185.199.110.153",
            "destination_port": "443",
            "observer_name": "so-sensor-01",
            "timestamp": (now - timedelta(minutes=2)).isoformat() + "Z",
        },
        {
            "name": "ET POLICY DNS Query for Newly Observed Domain",
            "severity_label": "MEDIUM",
            "ruleid": "2019400",
            "eventid": "demo-evt-002",
            "source_ip": "10.10.30.44",
            "source_port": "53122",
            "destination_ip": "8.8.8.8",
            "destination_port": "53",
            "observer_name": "so-sensor-02",
            "timestamp": (now - timedelta(minutes=8)).isoformat() + "Z",
        },
        {
            "name": "SURICATA TLS Invalid Certificate Observed",
            "severity_label": "LOW",
            "ruleid": "2409001",
            "eventid": "demo-evt-003",
            "source_ip": "10.10.22.91",
            "source_port": "60331",
            "destination_ip": "172.67.71.206",
            "destination_port": "443",
            "observer_name": "so-sensor-01",
            "timestamp": (now - timedelta(minutes=15)).isoformat() + "Z",
        },
        {
            "name": "ET MALWARE Known C2 Beacon Pattern",
            "severity_label": "HIGH",
            "ruleid": "2035560",
            "eventid": "demo-evt-004",
            "source_ip": "10.10.40.11",
            "source_port": "49812",
            "destination_ip": "45.77.10.22",
            "destination_port": "8080",
            "observer_name": "so-sensor-03",
            "timestamp": (now - timedelta(minutes=24)).isoformat() + "Z",
        },
        {
            "name": "ET SCAN Potential SSH Brute Force Activity",
            "severity_label": "MEDIUM",
            "ruleid": "2001219",
            "eventid": "demo-evt-005",
            "source_ip": "203.0.113.19",
            "source_port": "51114",
            "destination_ip": "10.10.10.8",
            "destination_port": "22",
            "observer_name": "so-sensor-01",
            "timestamp": (now - timedelta(minutes=42)).isoformat() + "Z",
        },
    ]
    return alerts[:limit]


def format_alerts(alerts: List[Dict[str, Any]]) -> str:
    """Format alerts to match the existing frontend parser format."""
    if not alerts:
        return "No alerts found in the last 24 hours. Total events: 0"

    lines = [f"Found {len(alerts)} alerts in the last 24 hours:"]
    for alert in alerts:
        lines.extend(
            [
                "",
                f"[{alert['severity_label']}] - {alert['name']}",
                f"  ruleid: {alert['ruleid']}",
                f"  eventid: {alert['eventid']}",
                f"  source: {alert['source_ip']}:{alert['source_port']}",
                f"  destination: {alert['destination_ip']}:{alert['destination_port']}",
                f"  observer.name: {alert['observer_name']}",
                f"  timestamp: {alert['timestamp']}",
            ]
        )
    return "\n".join(lines)
