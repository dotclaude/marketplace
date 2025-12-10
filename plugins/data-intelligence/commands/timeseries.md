---
model: claude-sonnet-4-0
allowed-tools: Task, Bash, Read, Write
argument-hint: <requirement> [focus]
description: Time series analysis, forecasting, and anomaly detection
---

# Timeseries Command

Time series analysis, forecasting, and anomaly detection

## Arguments

**$1 (Required)**: requirement

**$2 (Optional)**: focus

## Examples

```bash
/timeseries "Forecast API traffic" forecasting
/timeseries "Detect metric anomalies" anomaly-detection
```

Invoke the timeseries-specialist agent with: $ARGUMENTS
