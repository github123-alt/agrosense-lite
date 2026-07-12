---
name: diagnose-crop
description: Use when a farmer or user shares a crop leaf image path and wants to know what disease it has and what to do about it.
---

# Diagnose Crop Disease

Follow these steps in order.

## Step 1 — Get the image path
If the user has not already provided an image path, ask them for it using `ask_followup_question`.

## Step 2 — Run the classifier
Run the classifier using `execute_command`:
```
python classify.py <image_path> --json
```
Use the project root (the directory containing `classify.py`) as the working directory.

## Step 3 — Parse the JSON output
The command returns a JSON object with this shape:
```json
{
  "prediction": { "disease": "...", "confidence": 0.0 },
  "advisory": {
    "condition": "...",
    "severity": "...",
    "advice": "...",
    "local_note": "...",
    "advice_source": "granite | static"
  },
  "low_confidence": false,
  "runner_up": { "disease": "...", "confidence": 0.0 }
}
```
`local_note` and `advice_source` are optional — they are only present for certain disease classes.

## Step 4 — Present the result to the farmer
Format the result in clear, plain language. Use this structure:

**Diagnosis:** {advisory.condition}
**Severity:** {advisory.severity}
**What to do:** {advisory.advice}

If `advisory.local_note` is present, add:
> **Local tip:** {advisory.local_note}

If `low_confidence` is true, add:
> "Note: The model is not fully certain about this result (confidence: {confidence}%). Please take another photo in good lighting and consult a local agricultural officer before acting."

If `runner_up` is present and confidence is below 75%, add:
> "Another possibility: {runner_up.disease} ({runner_up.confidence}%)"

## Step 5 — Offer next steps
Ask the user if they want to:
- Diagnose another leaf
- Get more detail about the disease
- Know what season or weather conditions to watch out for
