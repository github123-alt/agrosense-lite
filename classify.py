import sys
import torch
import torch.nn as nn
from torchvision import models, transforms
from huggingface_hub import hf_hub_download
from PIL import Image
from advisory import get_advisory

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

# --- Download model weights ---
weights_path = hf_hub_download(repo_id=REPO_ID, filename="mobilenetv2_plant.pth")

# --- Rebuild architecture exactly as trained ---
model = models.mobilenet_v2(pretrained=False)
model.classifier[1] = nn.Sequential(
    nn.Dropout(0.2),
    nn.Linear(model.classifier[1].in_features, 38)
)

model.load_state_dict(torch.load(weights_path, map_location="cpu"))
model.eval()

# --- Preprocessing ---
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])

def classify_leaf(image_path):
    img = Image.open(image_path).convert("RGB")
    x = transform(img).unsqueeze(0)

    with torch.no_grad():
        preds = model(x)
        probs = torch.softmax(preds, dim=1)[0]
        index = probs.argmax().item()

    return {
        "disease": CLASS_NAMES[index],
        "confidence": float(probs[index])
    }

if __name__ == "__main__":
    image_path = sys.argv[1] if len(sys.argv) > 1 else "test_leaf.jpg"

    result = classify_leaf(image_path)
    advisory = get_advisory(result["disease"])

    print(f"Image: {image_path}")
    print(f"Predicted: {result['disease']}")
    print(f"Confidence: {result['confidence']:.2%}")
    print(f"Condition: {advisory['condition']}")
    print(f"Severity: {advisory['severity']}")
    print(f"Advice: {advisory['advice']}")
