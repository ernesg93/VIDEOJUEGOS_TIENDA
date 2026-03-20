import os
import yaml
import uuid

# Define the base directory for observations
BASE_DIR = os.path.join(".", "shared-knowledge", "project", "VIDEOJUEGOS_TIENDA", "observations")

def ensure_dir():
    """Ensure the observations directory exists."""
    os.makedirs(BASE_DIR, exist_ok=True)

def save_observation(title, obs_type, content):
    """
    Save an observation to a YAML file.
    
    Args:
        title (str): Title of the observation
        obs_type (str): Type of observation (e.g., 'decision', 'bugfix')
        content (dict): Content dict with keys: What, Why, Where, Learned
    
    Returns:
        str: The ID of the saved observation
    """
    ensure_dir()
    obs_id = str(uuid.uuid4())
    observation = {
        "id": obs_id,
        "title": title,
        "type": obs_type,
        "content": content
    }
    file_path = os.path.join(BASE_DIR, f"{obs_id}.yaml")
    with open(file_path, 'w') as f:
        yaml.dump(observation, f, default_flow_style=False)
    return obs_id

def get_observation(obs_id):
    """
    Retrieve an observation by ID.
    
    Args:
        obs_id (str): The ID of the observation to retrieve
    
    Returns:
        dict: The observation data, or None if not found
    """
    file_path = os.path.join(BASE_DIR, f"{obs_id}.yaml")
    if not os.path.exists(file_path):
        return None
    with open(file_path, 'r') as f:
        return yaml.safe_load(f)

def main():
    # Test observation data
    test_title = "Test Observation"
    test_type = "decision"
    test_content = {
        "What": "This is a test observation to demonstrate the shared-knowledge functionality.",
        "Why": "To verify that we can save and retrieve observations correctly.",
        "Where": "./shared-knowledge/project/VIDEOJUEGOS_TIENDA/observations/",
        "Learned": "The basic file-based approach works for storing structured observations."
    }
    
    print("Saving test observation...")
    obs_id = save_observation(test_title, test_type, test_content)
    print(f"Observation saved with ID: {obs_id}")
    
    print("\nRetrieving observation by ID...")
    retrieved = get_observation(obs_id)
    if retrieved:
        print("Observation retrieved successfully!")
        print(f"Title: {retrieved['title']}")
        print(f"Type: {retrieved['type']}")
        print(f"Content: {retrieved['content']}")
    else:
        print("Failed to retrieve observation.")
    
    # Verify the file exists
    file_path = os.path.join(BASE_DIR, f"{obs_id}.yaml")
    if os.path.exists(file_path):
        print(f"\nObservation file exists at: {file_path}")
    else:
        print("\nObservation file does not exist.")

if __name__ == "__main__":
    main()