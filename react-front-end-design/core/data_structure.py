import os

# Define the directory structure as a nested dictionary
project_structure = {
    "scripts": {
        "public": {
            "index.html": "",
            "favicon.ico": "",
            "assets": {
                "images": {},
                "fonts": {}
            }
        },
        "src": {
            "App.tsx": "",
            "index.tsx": "",
            "components": {
                "Button": {
                    "Button.tsx": "",
                    "Button.test.tsx": "",
                    "Button.stories.tsx": ""
                },
                "Modal": {
                    "Modal.tsx": "",
                    "Modal.test.tsx": "",
                    "Modal.stories.tsx": ""
                },
                "Navbar": {
                    "Navbar.tsx": "",
                    "Navbar.test.tsx": "",
                    "Navbar.stories.tsx": ""
                }
            },
            "features": {
                "auth": {
                    "authSlice.ts": "",
                    "Login.tsx": "",
                    "Signup.tsx": ""
                },
                "dashboard": {
                    "Dashboard.tsx": "",
                    "Dashboard.test.tsx": "",
                    "widgets": {
                        "Widget1.tsx": "",
                        "Widget2.tsx": ""
                    }
                }
            },
            "redux": {
                "store.ts": "",
                "middleware.ts": ""
            },
            "services": {
                "api.ts": "",
                "mockData.ts": ""
            },
            "styles": {
                "global.css": "",
                "themes": {
                    "dark.css": "",
                    "light.css": ""
                }
            },
            "tests": {
                "utils": {
                    "renderWithRedux.tsx": "",
                    "mockServer.ts": ""
                },
                "setupTests.ts": ""
            }
        },
        ".storybook": {
            "main.js": "",
            "preview.js": "",
            "stories": {
                "Button.stories.tsx": "",
                "Modal.stories.tsx": "",
                "Navbar.stories.tsx": ""
            }
        }
    }
}


def create_structure(base_path, structure):
    """
    Recursively creates directories and files based on a nested dictionary structure.
    
    Args:
        base_path (str): The base path where the structure should be created.
        structure (dict): The nested dictionary representing the structure.
    """
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):  # If the value is a dictionary, create a folder
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)  # Recursively create sub-structure
        else:  # If the value is not a dictionary, create a file
            with open(path, "w") as file:
                file.write(content)


# Create the project structure in the current directory
base_directory = "project_framework"
os.makedirs(base_directory, exist_ok=True)
create_structure(base_directory, project_structure)

print(f"Project structure created in {os.path.abspath(base_directory)}")
