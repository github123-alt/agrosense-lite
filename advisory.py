"""
advisory.py

Plain-language advisory lookup for AgroSense Lite.
Takes a predicted disease class (as output by classify.py) and returns
farmer-friendly guidance: condition name, severity, and recommended action.

No external API required — fully offline, matching AgroSense's
low-connectivity design goal.
"""

ADVISORY_LOOKUP = {
    # --- Apple ---
    "Apple___Apple_scab": {
        "condition": "Apple Scab",
        "severity": "Moderate",
        "advice": "Dark, scabby spots on leaves and fruit. Remove and destroy fallen leaves to stop spread. Apply a fungicide spray early in the growing season if the problem continues."
    },
    "Apple___Black_rot": {
        "condition": "Black Rot",
        "severity": "High",
        "advice": "Causes dark, sunken spots on fruit and leaves. Prune out dead or infected branches. Remove mummified fruit from the tree and ground to prevent spread."
    },
    "Apple___Cedar_apple_rust": {
        "condition": "Cedar Apple Rust",
        "severity": "Moderate",
        "advice": "Orange-yellow spots on leaves. Remove nearby cedar/juniper trees if possible, as they host this disease. Fungicide can help if applied early."
    },
    "Apple___healthy": {
        "condition": "Healthy",
        "severity": "None",
        "advice": "Your apple leaf looks healthy. Keep monitoring regularly and maintain good watering and spacing between plants."
    },

    # --- Blueberry ---
    "Blueberry___healthy": {
        "condition": "Healthy",
        "severity": "None",
        "advice": "Your blueberry plant looks healthy. Continue regular care and monitoring."
    },

    # --- Cherry ---
    "Cherry_(including_sour)___Powdery_mildew": {
        "condition": "Powdery Mildew",
        "severity": "Moderate",
        "advice": "White, powdery coating on leaves. Improve air circulation by pruning crowded branches. Avoid overhead watering and apply fungicide if it spreads."
    },
    "Cherry_(including_sour)___healthy": {
        "condition": "Healthy",
        "severity": "None",
        "advice": "Your cherry tree looks healthy. Continue regular care and monitoring."
    },

    # --- Corn (maize) ---
    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot": {
        "condition": "Gray Leaf Spot",
        "severity": "Moderate",
        "advice": "Rectangular gray-brown lesions on leaves. Rotate crops and avoid planting corn in the same field back-to-back. Remove crop debris after harvest."
    },
    "Corn_(maize)___Common_rust_": {
        "condition": "Common Rust",
        "severity": "Moderate",
        "advice": "Reddish-brown raised spots (pustules) on leaves. Usually not severe unless infection is heavy and early. Resistant seed varieties help prevent this next season."
    },
    "Corn_(maize)___Northern_Leaf_Blight": {
        "condition": "Northern Leaf Blight",
        "severity": "High",
        "advice": "Long, gray-green, cigar-shaped lesions on leaves. Can significantly reduce yield if untreated. Rotate crops and consider resistant varieties next planting."
    },
    "Corn_(maize)___healthy": {
        "condition": "Healthy",
        "severity": "None",
        "advice": "Your corn plant looks healthy. Continue regular care and monitoring."
    },

    # --- Grape ---
    "Grape___Black_rot": {
        "condition": "Black Rot",
        "severity": "High",
        "advice": "Brown circular spots on leaves, fruit shrivels into hard black mummies. Remove infected fruit and leaves. Prune for better air circulation."
    },
    "Grape___Esca_(Black_Measles)": {
        "condition": "Esca (Black Measles)",
        "severity": "High",
        "advice": "Striped/tiger-like discoloration on leaves, dark spots on fruit. No cure once established — remove and destroy severely infected vines to protect the rest."
    },
    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)": {
        "condition": "Leaf Blight (Isariopsis Leaf Spot)",
        "severity": "Moderate",
        "advice": "Dark angular spots on leaves that can cause early leaf drop. Remove affected leaves and improve airflow around vines."
    },
    "Grape___healthy": {
        "condition": "Healthy",
        "severity": "None",
        "advice": "Your grape vine looks healthy. Continue regular care and monitoring."
    },

    # --- Orange ---
    "Orange___Haunglongbing_(Citrus_greening)": {
        "condition": "Citrus Greening (Huanglongbing)",
        "severity": "Severe",
        "advice": "Yellowing leaves in a blotchy pattern, bitter and misshapen fruit. No cure exists — remove and destroy infected trees to protect nearby healthy ones, and control psyllid insects that spread it."
    },

    # --- Peach ---
    "Peach___Bacterial_spot": {
        "condition": "Bacterial Spot",
        "severity": "Moderate",
        "advice": "Small dark spots on leaves and fruit, leaves may develop holes. Avoid overhead watering. Copper-based sprays can help reduce spread."
    },
    "Peach___healthy": {
        "condition": "Healthy",
        "severity": "None",
        "advice": "Your peach tree looks healthy. Continue regular care and monitoring."
    },

    # --- Pepper, bell ---
    "Pepper,_bell___Bacterial_spot": {
        "condition": "Bacterial Spot",
        "severity": "Moderate",
        "advice": "Small, dark, water-soaked spots on leaves and fruit. Avoid working in the field when leaves are wet. Rotate crops and use disease-free seed next season."
    },
    "Pepper,_bell___healthy": {
        "condition": "Healthy",
        "severity": "None",
        "advice": "Your pepper plant looks healthy. Continue regular care and monitoring."
    },

    # --- Potato ---
    "Potato___Early_blight": {
        "condition": "Early Blight",
        "severity": "Moderate",
        "advice": "Brown spots with rings, often on older leaves first. Remove affected leaves. Avoid overhead watering. Rotate crops next season."
    },
    "Potato___Late_blight": {
        "condition": "Late Blight",
        "severity": "Severe",
        "advice": "Fast-spreading disease that can destroy a whole field quickly. Remove and destroy infected plants immediately. This is the disease behind historic famines — act fast and consider contacting a local agriculture officer."
    },
    "Potato___healthy": {
        "condition": "Healthy",
        "severity": "None",
        "advice": "Your potato plant looks healthy. Continue regular care and monitoring."
    },

    # --- Raspberry ---
    "Raspberry___healthy": {
        "condition": "Healthy",
        "severity": "None",
        "advice": "Your raspberry plant looks healthy. Continue regular care and monitoring."
    },

    # --- Soybean ---
    "Soybean___healthy": {
        "condition": "Healthy",
        "severity": "None",
        "advice": "Your soybean plant looks healthy. Continue regular care and monitoring."
    },

    # --- Squash ---
    "Squash___Powdery_mildew": {
        "condition": "Powdery Mildew",
        "severity": "Moderate",
        "advice": "White, powdery coating on leaves, common in humid conditions. Improve spacing and airflow between plants. Apply fungicide if it spreads to most of the leaf surface."
    },

    # --- Strawberry ---
    "Strawberry___Leaf_scorch": {
        "condition": "Leaf Scorch",
        "severity": "Moderate",
        "advice": "Small purple spots that merge into larger scorched-looking patches. Remove infected leaves after harvest and avoid overhead watering."
    },
    "Strawberry___healthy": {
        "condition": "Healthy",
        "severity": "None",
        "advice": "Your strawberry plant looks healthy. Continue regular care and monitoring."
    },

    # --- Tomato ---
    "Tomato___Bacterial_spot": {
        "condition": "Bacterial Spot",
        "severity": "Moderate",
        "advice": "Small, dark, greasy-looking spots on leaves and fruit. Avoid overhead watering and working with wet plants. Use disease-free seed next season."
    },
    "Tomato___Early_blight": {
        "condition": "Early Blight",
        "severity": "Moderate",
        "advice": "Look for dark spots with rings on lower leaves. Remove affected leaves and avoid wetting leaves when watering."
    },
    "Tomato___Late_blight": {
        "condition": "Late Blight",
        "severity": "Severe",
        "advice": "Dark, water-soaked spots that spread quickly in wet weather. Remove infected plants right away to protect the rest of your field."
    },
    "Tomato___Leaf_Mold": {
        "condition": "Leaf Mold",
        "severity": "Moderate",
        "advice": "Yellow spots on top of leaves with fuzzy mold underneath. Common in humid, poorly ventilated conditions. Improve airflow and reduce leaf wetness."
    },
    "Tomato___Septoria_leaf_spot": {
        "condition": "Septoria Leaf Spot",
        "severity": "Moderate",
        "advice": "Small circular spots with dark borders and light centers, mostly on lower leaves. Remove infected leaves early and avoid overhead watering."
    },
    "Tomato___Spider_mites Two-spotted_spider_mite": {
        "condition": "Spider Mites (Two-Spotted)",
        "severity": "Moderate",
        "advice": "Tiny yellow or bronze speckling on leaves, sometimes fine webbing visible. Spray plants with water to dislodge mites, or use insecticidal soap if severe."
    },
    "Tomato___Target_Spot": {
        "condition": "Target Spot",
        "severity": "Moderate",
        "advice": "Brown spots with concentric rings, resembling a target. Remove infected leaves and avoid overcrowding plants to improve airflow."
    },
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus": {
        "condition": "Tomato Yellow Leaf Curl Virus",
        "severity": "Severe",
        "advice": "Leaves curl upward and turn yellow, plant growth stunted. Spread by whiteflies — control whitefly populations and remove infected plants to prevent further spread."
    },
    "Tomato___Tomato_mosaic_virus": {
        "condition": "Tomato Mosaic Virus",
        "severity": "High",
        "advice": "Mottled light and dark green pattern on leaves, distorted growth. No cure — remove and destroy infected plants. Wash hands and tools after handling to avoid spreading it."
    },
    "Tomato___healthy": {
        "condition": "Healthy",
        "severity": "None",
        "advice": "Your tomato plant looks healthy. Keep up good care."
    },
}


def get_advisory(predicted_class):
    """
    Look up plain-language advisory info for a predicted disease class.

    Args:
        predicted_class (str): class label as returned by classify.py,
            e.g. "Tomato___Late_blight"

    Returns:
        dict with keys: condition, severity, advice
    """
    return ADVISORY_LOOKUP.get(predicted_class, {
        "condition": predicted_class.replace("___", " - ").replace("_", " "),
        "severity": "Unknown",
        "advice": "Disease detected, but detailed advice isn't available yet for this specific condition. Please consult a local agricultural extension officer for guidance."
    })


if __name__ == "__main__":
    # Quick manual test
    test_classes = ["Apple___healthy", "Potato___Late_blight", "Tomato___Tomato_mosaic_virus"]
    for cls in test_classes:
        result = get_advisory(cls)
        print(f"\nClass: {cls}")
        print(f"Condition: {result['condition']}")
        print(f"Severity: {result['severity']}")
        print(f"Advice: {result['advice']}")
