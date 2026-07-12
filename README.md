# AgroSense Lite — Smart Crop Advisory for Smallholder Farmers

> Submission for the IBM AI Builders Challenge with IBM Bob — Wildcard Track: *Intelligent Systems for the Future of Work*

## Problem Statement

Smallholder farmers in Nepal — and across much of the developing world — often lack timely, affordable access to expert agronomic guidance. A farmer noticing unusual spots on a crop leaf typically has no fast way to know whether it's a treatable fungal infection, a pest issue, or a nutrient deficiency. By the time expert advice is available (if at all), yield loss has often already occurred.

This gap costs smallholders income and food security. It's exactly the kind of "future of work" problem where an intelligent system can meaningfully **augment — not replace** — human expertise like local agricultural officers and extension workers.

## What This Project Does

AgroSense Lite is a focused proof-of-concept. A farmer submits a photo of a crop leaf, and an IBM Bob–orchestrated pipeline:

1. **Classifies** the likely disease or condition from the image (38 classes, PlantVillage dataset)
2. **Retrieves** a plain-language advisory — what the condition is, how urgent it is, and what to do next
3. **Localises** the advice — high-risk crops include Nepal-specific seasonal notes and local institution references (e.g. Krishi Gyan Kendra)
4. **Flags uncertainty** — if the model's confidence is low, the farmer is told to seek a second opinion before acting

This is a deliberately narrow slice of a larger AgroSense Nepal vision (which also includes weather-linked advisories and market price intelligence) — scoped to be fully built, tested, and demoed within the challenge timeline.

## Why It Matters

- **Economic impact:** Faster, correct diagnosis reduces crop loss and unnecessary pesticide spending for smallholder farmers.
- **Accessibility:** Designed for low-literacy, low-connectivity contexts — image in, plain advisory out, no internet required after setup.
- **Future of work fit:** Demonstrates how an AI-orchestrated system can extend the reach of scarce human expertise, letting one agricultural officer effectively support many more farmers.
- **Responsible AI:** The system reports confidence scores and explicitly flags low-certainty results, so farmers and extension workers can decide when to act and when to verify.

## Technical Approach

| Component | What it does |
|---|---|
| **IBM Bob Skill** (`diagnose-crop`) | Orchestrates the full pipeline — takes an image path, calls the classifier, and presents results in plain language |
| **IBM Granite** (`granite.py`) | `ibm-granite/granite-3.3-2b-instruct` via Hugging Face — generates dynamic, contextual advisory text grounded on the disease knowledge base |
| **Classifier** (`classify.py`) | MobileNetV2 fine-tuned on PlantVillage (38 classes), served locally, returns top-3 predictions with confidence scores |
| **Advisory engine** (`advisory.py`) | Structured knowledge base mapping disease classes to condition, severity, Nepal-localised notes, and Granite-enhanced advice |
| **Output** | Human-readable CLI output or structured `--json` mode for Bob integration |

## Architecture

```
Farmer shares leaf photo
        │
        ▼
IBM Bob (diagnose-crop skill)
        │
        ▼
classify.py  ──►  MobileNetV2 model (Hugging Face)
        │
        ▼
advisory.py  ──►  Disease advisory + local note
        │
        ▼
Plain-language result to farmer
(Condition / Severity / What to do / Local tip)
```

## Usage

### Via IBM Bob (recommended)

Open a conversation with Bob and share a leaf image path. The `diagnose-crop` skill activates automatically:

```
I have a photo of my tomato plant at /photos/leaf.jpg — what disease does it have?
```

### Via CLI

```bash
# Install dependencies
pip install -r requirements.txt

# Run on an image (Granite-enhanced advice, default)
python classify.py test_leaf.jpg

# Skip Granite — use static advice only (faster, offline)
python classify.py test_leaf.jpg --no-granite

# Structured JSON output (for Bob integration)
python classify.py test_leaf.jpg --json
```

### Example output

```
Image:      test_diseased.jpg
Predicted:  Tomato___Late_blight
Confidence: 51.19%
Condition:  Late Blight
Severity:   Critical
Advice [granite]: Act immediately — remove and destroy all infected plants to
                  prevent the disease from spreading to healthy ones. During
                  Nepal's monsoon season (July–September), inspect your field
                  every few days and contact your local Krishi Gyan Kendra.
Local tip:  High risk in Nepal from July to September. Contact your local
            Krishi Gyan Kendra immediately.

Note: Confidence is low — consider taking another photo in better lighting.
      Consult a local agricultural officer before acting.
```

## Supported Crops

Apple · Blueberry · Cherry · Corn · Grape · Orange · Peach · Pepper · Potato · Raspberry · Soybean · Squash · Strawberry · Tomato

38 disease and healthy classes in total, covering the most common conditions in the PlantVillage dataset.

## Current Status

- [x] IBM SkillsBuild module completed
- [x] IBM Bob access set up
- [x] Classification component working
- [x] Advisory generation working
- [x] End-to-end pipeline tested
- [x] Demo video recorded
- [x] Final README polished

## Team

Prayash Phuyal

## Demo Video

[Watch on YouTube](https://youtube.com/shorts/JASPG2yTH10?feature=share)
