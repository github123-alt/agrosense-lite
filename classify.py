import sys
import json
import torch
import torch.nn as nn
from torchvision import models, transforms
from huggingface_hub import hf_hub_download
from PIL import Image, UnidentifiedImageError
from advisory import get_advisory

__all__ = ["classify_leaf"]

REPO_ID = "Daksh159/plant-disease-mobilenetv2"

# Standard 38-class PlantVillage (augmented) ordering — alphabetical folder order,
# matching torchvision ImageFolder's default class indexing
CLASS_NAMES = [
    "Apple___Apple_scab", "Apple___Black_rot", "Apple___Cedar_apple_rust", "Apple___healthy",
    "Blueberry___healthy",
    "Cherry_(including_sour)___Powdery_mildew", "Cherry_(including_sour)___healthy",
    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot", "Corn_(maize)___Common_rust_",
    "Corn_(maize)___Northern_Leaf_Blight", "Corn_(maize)___healthy",
    "Grape___Black_rot", "Grape___Esca_(Black_Measles)",
    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)", "Grape___healthy",
    "Orange___Haunglongbing_(Citrus_greening)",
    "Peach___Bacterial_spot", "Peach___healthy",
    "Pepper,_bell___Bacterial_spot", "Pepper,_bell___healthy",
    "Potato___Early_blight", "Potato___Late_blight", "Potato___healthy",
    "Raspberry___healthy",
    "Soybean___healthy",
    "Squash___Powdery_mildew",
    "Strawberry___Leaf_scorch", "Strawberry___healthy",
    "Tomato___Bacterial_spot", "Tomato___Early_blight", "Tomato___Late_blight",
    "Tomato___Leaf_Mold", "Tomato___Septoria_leaf_spot",
    "Tomato___Spider_mites Two-spotted_spider_mite", "Tomato___Target_Spot",
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus", "Tomato___Tomato_mosaic_virus",
    "Tomato___healthy"
]

assert len(CLASS_NAMES) == 38, "Class list must have exactly 38 entries"

# --- Lazy model state ---
_model = None
_transform = None


def _load_model():
    """Download and initialise the model on first use."""
    global _model, _transform
    if _model is not None:
        return

    weights_path = hf_hub_download(repo_id=REPO_ID, filename="mobilenetv2_plant.pth")

    # Rebuild architecture exactly as trained
    model = models.mobilenet_v2(weights=None)
    model.classifier[1] = nn.Sequential(
        nn.Dropout(0.2),
        nn.Linear(model.classifier[1].in_features, 38)
    )
    model.load_state_dict(torch.load(weights_path, map_location="cpu", weights_only=True))
    model.eval()

    _model = model
    _transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])


def classify_leaf(image_path):
    """
    Classify a leaf image and return the top-3 predictions.

    Args:
        image_path (str): Path to the image file.

    Returns:
        list of dicts, each with keys: disease (str), confidence (float).
        Ordered from highest to lowest confidence.

    Raises:
        FileNotFoundError: If the image file does not exist.
        ValueError: If the file cannot be read as an image.
    """
    _load_model()

    try:
        img = Image.open(image_path).convert("RGB")
    except FileNotFoundError:
        raise FileNotFoundError(f"Image file not found: {image_path}")
    except UnidentifiedImageError:
        raise ValueError(f"File is not a valid image: {image_path}")

    x = _transform(img).unsqueeze(0)

    with torch.no_grad():
        preds = _model(x)
        probs = torch.softmax(preds, dim=1)[0]

    top3 = probs.topk(3)
    return [
        {"disease": CLASS_NAMES[idx], "confidence": float(conf)}
        for conf, idx in zip(top3.values, top3.indices)
    ]


if __name__ == "__main__":
    args = sys.argv[1:]
    if not args or args[0].startswith("-"):
        print("Usage: python classify.py <image_path> [--json]")
        sys.exit(1)

    image_path = args[0]
    use_json = "--json" in args

    results = classify_leaf(image_path)
    top = results[0]
    advisory = get_advisory(top["disease"])
    low_confidence = top["confidence"] < 0.70
    runner_up = results[1] if top["confidence"] < 0.75 and len(results) > 1 else None

    if use_json:
        output = {
            "prediction": top,
            "advisory": advisory,
            "low_confidence": low_confidence,
        }
        if runner_up:
            output["runner_up"] = runner_up
        print(json.dumps(output, indent=2))
    else:
        print(f"Image:      {image_path}")
        print(f"Predicted:  {top['disease']}")
        print(f"Confidence: {top['confidence']:.2%}")
        print(f"Condition:  {advisory['condition']}")
        print(f"Severity:   {advisory['severity']}")
        print(f"Advice:     {advisory['advice']}")

        if low_confidence:
            print(
                "\nNote: Confidence is low — consider taking another photo in better lighting."
                "\n      Consult a local agricultural officer before acting."
            )
        elif runner_up:
            print(f"\nRunner-up: {runner_up['disease']} ({runner_up['confidence']:.2%})")
