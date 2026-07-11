# AgroSense Lite — Smart Crop Advisory for Smallholder Farmers

> Submission for the IBM AI Builders Challenge with IBM Bob — Wildcard Track: *Intelligent Systems for the Future of Work*

## Problem Statement

Smallholder farmers in Nepal — and across much of the developing world — often lack timely, affordable access to expert agronomic guidance. A farmer noticing unusual spots on a crop leaf typically has no fast way to know whether it's a treatable fungal infection, a pest issue, or a nutrient deficiency, and by the time expert advice is available (if at all), yield loss has often already occurred. This gap costs smallholders income and food security, and it's exactly the kind of "future of work" problem where an intelligent system can meaningfully augment — not replace — human expertise (local agricultural officers, extension workers).

## What This Project Does

AgroSense Lite is a focused proof-of-concept: a farmer submits a photo of a crop leaf, and an IBM Bob–orchestrated pipeline:
1. Classifies the likely disease/condition from the image
2. Retrieves a plain-language, locally relevant advisory (what it is, what to do next, urgency level)
3. Returns the result in a simple, low-bandwidth-friendly format

This is a deliberately narrow slice of a larger AgroSense Nepal vision (which also includes weather-linked advisories and market price intelligence) — scoped to be fully built, tested, and demoed within the challenge timeline.

## Why It Matters

- **Economic impact:** Faster, correct diagnosis reduces crop loss and unnecessary pesticide spending for smallholder farmers.
- **Accessibility:** Designed for low-literacy, low-connectivity contexts — image in, plain advisory out.
- **Future of work fit:** Demonstrates how an AI-orchestrated system can extend the reach of scarce human expertise (agricultural extension officers) rather than replace it, letting one expert effectively support many more farmers.
- **Explainability:** The system surfaces *why* it reached a conclusion (visible symptoms matched), not just a black-box label, so farmers and extension workers can trust and verify it.

## Technical Approach

- **Core orchestration:** IBM Bob coordinates the pipeline from image intake → classification → advisory generation → response formatting
- **Classification:** [model/approach — e.g., vision model or IBM Bob-integrated tool for crop disease detection]
- **Advisory generation:** [how plain-language output is generated — e.g., structured knowledge base + IBM Bob reasoning]
- **Interface:** [e.g., simple web form / CLI / chatbot-style input for the demo]

## Architecture

```
[Farmer uploads photo]
        ↓
[IBM Bob orchestration]
        ↓
[Disease/condition classification]
        ↓
[Advisory lookup / generation]
        ↓
[Plain-language response to farmer]
```

## Current Status

- [ ] IBM SkillsBuild module completed
- [ ] IBM Bob access set up
- [ ] Classification component working
- [ ] Advisory generation working
- [ ] End-to-end pipeline tested
- [ ] Demo video recorded
- [ ] Final README polished

## Team

- Prayash Phuyal 

## Demo Video

https://youtube.com/shorts/JASPG2yTH10?feature=share

